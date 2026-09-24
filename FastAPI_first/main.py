from datetime import datetime
from fastapi import FastAPI, Path, Query, HTTPException, Depends  # 2、导入 Depends
from pydantic import BaseModel, Field
from sqlalchemy import DateTime, func, String, Float, select
from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.testing.schema import mapped_column
from starlette.responses import HTMLResponse, FileResponse
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

# 创建 FastAPI 实例
app = FastAPI()

"""
ORM 建表
"""

# 1. 创建异步引擎
ASYNC_DATABASE_URL = "mysql+aiomysql://root:root@localhost:3306/FastAPI_first?charset=utf8"
async_engine = create_async_engine(
    ASYNC_DATABASE_URL,
    echo=True,  # 可选，输出 SQL 日志
    pool_size=10,  # 设置连接池活跃的连接数
    max_overflow=20  # 允许额外的连接数
)


# 2. 定义模型类： 基类 + 表对应的模型类
# 基类：创建时间、更新时间：书籍表：id、书名、作者、价格、出版社
class Base(DeclarativeBase):
    create_time: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now(), default=func.now(),
                                                  comment="创建时间")
    update_time: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now(), default=func.now(),
                                                  onupdate=func.now(), comment="修改时间")


class Book(Base):
    __tablename__ = "book"

    id: Mapped[int] = mapped_column(primary_key=True, comment="书籍ID")
    book_name: Mapped[str] = mapped_column(String(255), comment="书名")
    author: Mapped[str] = mapped_column(String(255), comment="作者")
    price: Mapped[float] = mapped_column(Float, comment="价格")
    publisher: Mapped[str] = mapped_column(String(255), comment="出版社")


# 3. 建表：定义函数表 → FastAPI 启动的时候调用建表的函数
async def create_tables():
    # 获取异步引擎，创建事务 - 建表
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)  # Base 模型类的元数据创建


@app.on_event("startup")
async def startup_event():
    await create_tables()


"""
ORM 在路由中使用 ORM
"""
# 需求：查询功能的接口，查询图书 → 依赖注入：创建依赖项获取数据库会话 + Depends 注入路由处理函数
AsyncSessionLocal = async_sessionmaker(
    bind=async_engine,  # 绑定数据库引擎
    class_=AsyncSession,  # 指定会话类
    expire_on_commit=False,  # 提交后会话不过期，不会重新查询数据库
)


# 依赖项
async def get_database():
    async with AsyncSessionLocal() as session:
        try:
            yield session  # 返回数据库会话给路由处理函数
            await session.commit()  # 提交事务
        except Exception:
            await session.rollback()  # 有异常，回滚
            raise
        finally:
            await session.close()  # 关闭会话


# @app.get("/book/books")
# async def get_book_list(db: AsyncSession = Depends(get_database)):
#     # 查询
#     result = await db.execute(select(Book))
#     book = result.scalars().all()
#     return book

"""
数据库操作 - 查询

核心语句：await db.execute(select(模型类))，返回一个 JSON 对象

▶️获取所有数据
    scalars().all()

▶️获取单条数据
    scalars().all().first()
    get(模型类，主键)
"""


@app.get("/book/books")
async def get_book_list(db: AsyncSession = Depends(get_database)):
    # 查询
    # result = await db.execute(select(Book)) # 查询 → 返回一个 ORM 独享
    # book = result.scalars().all() # 获取所有数据
    # book = result.scalars().first() # 获取第一条数据
    book = await db.get(Book, 3)  # 获取单挑数据 → 根据主键来获取
    return book


"""
数据库操作 - 查询条件

select(模型类).where(条件, 条件2, ...)
"""


# 需求：路径参数 书籍ID
@app.get("/book/get_book/{book_id}")
async def get_book_list(book_id: int, db: AsyncSession = Depends(get_database)):
    result = await db.execute(select(Book).where(Book.id == book_id))
    book = result.scalar_one_or_none()
    return book


# 需求：条件 价格大于等于200
# @app.get("/book/search_book")
# async def get_search_book(db: AsyncSession = Depends(get_database)):
#     result = await db.execute(select(Book).where(Book.price >= 200))
#     books = result.scalars().all()
#     return books


# 需求：作者以 曹 开头 % _
@app.get("/book/search_book")
async def get_search_book(db: AsyncSession = Depends(get_database)):
    # like() 模糊查询：% 任意个字符；_ 一个单个字符
    # result = await db.execute(select(Book).where(Book.author.like("曹_")))

    # & | ~ 或与非
    # result = await db.execute(select(Book).where((Book.author.like("曹%")) | (Book.price > 100)))

    # 需求：书籍id列表，数据库里面的id如果在 书籍id列表里面 就返回
    # in_() 包含
    id_list = [1, 3, 5, 7]
    result = await db.execute(select(Book).where(Book.id.in_(id_list)))
    books = result.scalars().all()
    return books


"""
数据库操作 - 聚合查询

聚合计算：func.方法(模型类.属性)
▶️count：统计数量
▶️avg：求平均值
▶️max：求最大值
▶️min：求最小值
▶️sum：求和
"""


@app.get("/book/count")
async def get_count(db: AsyncSession = Depends(get_database)):
    # 聚合查询 select( func.方法名(模型类.属性) )
    # result = await db.execute(select(func.count(Book.id)))
    # result = await db.execute(select(func.max(Book.price)))
    # result = await db.execute(select(func.sum(Book.price)))
    result = await db.execute(select(func.avg(Book.price)))
    num = result.scalar()  # 用来提取一个数值 → 标量值
    return num


"""
数据库操作 - 分页查询

分页查询：select().offset().limit()
▶️offset：跳过的记录数
▶️limit：返回的记录数
"""


@app.get("/books/get_books")
async def get_book_list_page(page: int = 1, page_size: int = 2, db: AsyncSession = Depends(get_database)):
    # (页面 - 1) * 每页数量
    skip = (page - 1) * page_size
    # offset 跳过的记录数； limit：每页的记录数；
    stmt = select(Book).offset(skip).limit(page_size)
    result = await db.execute(stmt)
    books = result.scalars().all()
    return books


"""
数据库操作 - 新增

核心步骤：定义 ORM 对象 → 添加对象到事务：add(对象) → commit 提交到数据库
"""


# 需求：用户输入图书信息(id, 书名, 作者, 价格, 出版社) → 新增
# 用户输入 → 参数 → 请求体
class BookBase(BaseModel):
    id: int
    book_name: str
    author: str
    price: float
    publisher: str


@app.post("/book/add_book")
async def add_book(book: BookBase, db: AsyncSession = Depends(get_database)):
    # ORM 对象 → add → commit
    book_obj = Book(**book.__dict__)
    db.add(book_obj)
    await db.commit()
    return book


"""
数据库操作 - 更新

核心步骤：查询 get → 属性重新赋值 → commit 提交到数据库
"""


# 需求：修改图书的信息：先查再改
# 设计思路：路径参数数据id：作用是查找；请求体参数：作用是新数据(书名、作者、价格、出版社)
class BookUpdate(BaseModel):
    book_name: str
    author: str
    price: float
    publisher: str


@app.put("/book/update_book/{book_id}")
async def update_book(book_id: int, data: BookUpdate, db: AsyncSession = Depends(get_database)):
    # 1. 查找图书
    db_book = await db.get(Book, book_id)

    # 如果未找到 抛出异常
    if db_book is None:
        raise HTTPException(status_code=404, detail="查无此书")

    # 2. 找到了则修改：重新赋值
    db_book.book_name = data.book_name
    db_book.author = data.author
    db_book.price = data.price
    db_book.publisher = data.publisher

    # 3. 提交到数据库
    await db.commit()
    return db_book


# ============================================================================================================
# 分页参数逻辑共用：新闻列表和用户列表(依赖注入)
# 1、依赖项
async def common_parameters(
        skip: int = Query(0, ge=0),
        limit: int = Query(10, le=60)
):
    return {"skip": skip, "limit": limit}


# (中间件)是从下往上执行的 中间件的修饰符示例：@app.middleware("http")
@app.middleware("http")
async def middleware1(request, call_next):
    print("中间件1 start")
    response = await call_next(request)
    print("中间件1 end")
    return response


@app.middleware("http")
async def middleware2(request, call_next):
    print("中间件2 start")
    response = await call_next(request)
    print("中间件2 end")
    return response


@app.get("/")
async def root():
    return {"message": "Hello World"}


# 访问 /hello 响应结果 msg: 你好 FastAPI
@app.get("/hello")
async def get_hello():
    return {"msg": "你好 FastAPI"}


@app.get("/book/{id}")
async def get_book(id: int = Path(..., gt=0, lt=101, description="书籍id，取值范围[1, 100]")):
    return {"id": id, "title": f"这是第{id}本书"}


# 需求：查找书籍的作者，路径参数 name，长度范围 2-10
@app.get("/author/{name}")
async def get_name(name: str = Path(..., min_length=2, max_length=10, description="作者姓名，长度[2, 10]")):
    return {"msg": f"这是{name}的信息"}


# 需求 查询新闻 → 分页，skip：跳过的记录数，  limit：返回的记录数 10
# @app.get("/news/news_list")
# async def get_news_list(skip: int = Query(0, description="跳过的记录数", lt=100),
#                         limit: int = Query(10, description="返回的记录数")):
#     return {"skip": skip, "limit": limit}

# 3、声明依赖项 → 依赖注入
@app.get("/news/news_list")
async def get_news_list(commons=Depends(common_parameters)):
    return commons


# 注册：用户名和密码 → str
class User(BaseModel):
    username: str = Field(default="张三", min_length=2, max_length=10, description="用户名长度要求[2, 10]")
    password: str = Field(min_length=3, max_length=20)


@app.post("/register")
async def register(user: User):
    return user


# 接口 响应 HTML 代码
@app.get("/html", response_class=HTMLResponse)
async def get_html():
    return "<h1>这是一级标题</h1>"


# 接口：返回一张图片内容
@app.get("/file")
async def get_file():
    path = "files/photo.jpg"
    return FileResponse(path)


# 需求：定义一个新闻的接口 → 响应数据格式 id、title、content
class News(BaseModel):
    id: int
    title: str
    content: str


# @app.get("/news/{id}", response_model=News)
# async def get_news(id: int):
#     return {
#         "id": id,
#         "title": f"这是第{id}本书",
#         "content": "这是一本好书"
#     }

# 需求：按id查询新闻 → 1 - 6
@app.get("/news/{id}")
async def get_news(id: int):
    id_list = [1, 2, 3, 4, 5, 6]
    if id not in id_list:
        raise HTTPException(status_code=404, detail="您查找的新闻不存在")
    return {
        "id": id,
    }


@app.get("/user/user_list")
async def get_user_list(commons=Depends(common_parameters)):
    return commons
