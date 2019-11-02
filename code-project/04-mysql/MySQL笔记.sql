-- 数据库操作
    -- 连接数据库：mysql -uroot -p
    -- 退出数据库：exit;\q;quit;

    -- 显示数据库版本：select version():
    select version();

    -- 显示当前时间：select now();
    select now();

    -- 查看所有数据库：show databases;
    show databases;

    -- 创建数据库：create database 数据库名 charset=utf8;
    create database student charset=utf8;

    -- 查看创建数据库的过程：show crate database 数据库名;
    show create database student;

    -- 使用数据库： use 数据库名;
    use student;

    -- 查看使用的数据库：select database();
    select database();

    -- 删除数据库：drop database 数据库名；
    drop database student;

-- 数据表操作
    -- 创建数据表: create table 表名 (字段名 类型 约束[, 字段名 类型 约束])
    -- 约束：
        -- 主键：primary key
        -- 非空：not null
        -- 自动增长：auto_increment
        -- 默认值：default

    -- 实例：创建学生表
    create table student (
        id int unsigned not null primary key auto_increment,
        name varchar(30) not null,
        age tinyint not null default 0,
        high decimal(5, 2),
        gender enum("男", "女", "保密", "中性") default "保密",
        cls_id int unsigned
    );

    -- 实例：创建班级表
    create table class (
        id int unsigned not null primary key auto_increment,
        classname varchar(30) not null
    );

    -- 删除数据表：drop table 表名;

    -- 查看创建表的语句：show create table 表名;
    show create table student;

    -- 查看创建数据表的结构：desc 表名;
    desc student;

    -- 添加字段
    -- alter table 表名 add 字段名 类型 约束;
    alter table student add birthday datetime;

    -- 修改字段：不重命名版
    -- alter table 表名 modify 字段名 类型 约束;
    alter table student modify birthday date;

    -- 修改字段：重命名版
    -- alter table 表名 change 字段名 字段新名 类型 约束;
    alter table student change hign high decimal(5, 2);

    -- 删除字段
    -- alter table student drop 字段名;
    alter table student drop high;

-- 数据操作：增删改查

    -- 增加
        -- 全列插入：未指明插入的具体字段，需要按照表结构的字段全部插入
        -- insert into 数据表名 values ();
            -- 主键自动增长，插入时需要占位：0 null default
            -- 枚举类型可使用数字下表标记，从1开始
        insert into class values (0, "菜鸟班");
        insert into student values (0, '老王', 21, 1, 1, "2019-05-18");

        -- 部分列插入：指明插入的字段
        -- insert into 数据表名(字段1, ...) values (值1, ...);
        insert into class(classname) values ("中级班");
        insert into student(name, age, cls_id, birthday) values ('小李', 15, 2, "2009-10-23");

        -- 多行插入
        -- 部分列多行插入：insert into 数据表名(字段1, ...) values (值1, ...) (值1, ...) (值1, ...);
        -- 全列多行插入：insert into 数据表名 values () () ();

    -- 删除
        -- delete from 表名 where 条件;
        delete from student;  # 禁用，会清空表
        delete from student where id = 3;

        -- 删除：修改标记记录的值
        update student set isdelete=1 where id = 1;

    -- 修改
        -- update 数据表名 set 字段1=值1, 字段2=值2,... where 条件；
        update student set gender = 1;  # 全部修改
        update student set gender = 2 where id = 2;
        update student set gender = 2, cls_id = 1 where id = 2;

    -- 查询
        -- 查询所有记录：select * from 表名;
        select * from student;

        -- 指定条件查询：select * from 表名 where 条件;
        select * from student where id = 1;

        -- 查询指定列：select 字段1, 字段2 from 表名;
        select name, gender from student;
        select name, gender from student where id = 1;

        -- 指定别名：select 字段1 as 别名, 字段2 as 别名 from 表名;
        select name as 姓名, gender as 性别 from student;