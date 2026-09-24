create database news_app;

create table news_category
(
    id         int unsigned primary key auto_increment comment '分类ID',
    name       varchar(50) comment '',
    sort_order int comment '',
    create_at  datetime comment '创建时间',
    update_at  datetime comment '更新时间'
) comment '新闻分类表';

insert into news_category (id, name, sort_order, create_at, update_at)
values (2, '社会', 2, now(), now()),
       (3, '国内', 3, now(), now()),
       (4, '国际', 4, now(), now()),
       (5, '娱乐', 5, now(), now()),
       (6, '体育', 6, now(), now()),
       (7, '科技', 7, now(), now()),
       (8, '财经', 8, now(), now());

create table news
(
    id           int unsigned auto_increment primary key,
    title        varchar(255),
    description  varchar(500),
    content      text,
    image        varchar(255),
    author       varchar(50),
    category_id  int unsigned,
    views        int unsigned default 0,
    publish_time timestamp,
    create_at    timestamp,
    update_at    timestamp
);
