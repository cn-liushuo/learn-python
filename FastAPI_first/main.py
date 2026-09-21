from fastapi import FastAPI, Path, Query
from pydantic import BaseModel, Field
from starlette.responses import HTMLResponse, FileResponse

# 创建 FastAPI 实例
app = FastAPI()


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
@app.get("/news/news_list")
async def get_news_list(skip: int = Query(0, description="跳过的记录数", lt=100),
                        limit: int = Query(10, description="返回的记录数")):
    return {"skip": skip, "limit": limit}


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

@app.get("/news/{id}", response_model=News)
async def get_news(id: int):
    return {
        "id": id,
        "title": f"这是第{id}本书",
        "content": "这是一本好书"
    }
