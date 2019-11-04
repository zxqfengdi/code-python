-- 数据的准备
	-- 创建一个数据库
    create database python_test charset=utf8mb4;

	-- 使用一个数据库
	use python_test;

	-- 显示使用的当前数据是哪个?
	select database();

	-- 创建一个数据表
	-- students表
	create table students(
	    id int unsigned not null auto_increment primary key,
	    name varchar(30) default '',
	    age tinyint unsigned default 0,
	    hight decimal(5, 2),
	    gender enum('男', '女', '中性', '保密') default '保密',
	    cls_id int unsigned default 0,
	    is_delete bit default 0
	);


	-- classes表
    create table classes(
        id int unsigned not null primary key auto_increment,
        classname varchar(30) not null
    );

-- 查询
	-- 查询所有字段
	-- select * from 表名;
    select * from students;
    select * from classes;

	-- 查询指定字段
	-- select 列1,列2,... from 表名;
    select name, age from students;
	
	-- 使用as给字段起别名
	-- select 字段 as 名字.... from 表名;
    select name as 姓名, age as 年龄 from students;

	-- select 表名.字段 .... from 表名;
    select students.name, students.age, students.cls_id from students;

	-- 可以通过as给表起别名
	-- select 别名.字段 .... from 表名 as 别名;
    select s.name, s.age, s.cls_id from students as s;

	-- 消除重复行
	-- distinct 字段
    select gender from students;
    select distinct gender from students;

-- 条件查询 where子句
	-- 比较运算符：> < >= <= = != <>

		-- select .... from 表名 where .....
		-- >
		-- 查询大于18岁的信息
        select * from students where age > 18;

		-- <
		-- 查询小于18岁的信息
        select * from students where age < 18;

		-- >=
		-- <=
		-- 查询小于或者等于18岁的信息
        select * from students where age <= 18;
        select * from students where age >= 18;

		-- =
		-- 查询年龄为18岁的所有学生的名字
        select name from students where age = 18;

		-- != 或者 <>
        select * from students where age != 18;
        select * from students where age <> 18;

	-- 逻辑运算符: and or not
		-- and                                                         s
		-- 18到28之间的所有学生信息
		select * from students where age > 18 and age < 28;
		-- 18岁以上的女性
        select * from students where age > 18 and gender = '女';
        select * from students where age > 18 and gender = 2;

		-- or
		-- 18以上或者身高查过180(包含)以上
        select * from students where age > 18 or hight >= 180;

		-- not
		-- 不在18岁以上的女性这个范围内的信息
		select * from students where not (age > 18 and gender = 2);

		-- 年龄不是小于或者等于18 并且是女性
        select * from students where (not age <= 18) and gender = 2;

	-- 模糊查询: like rlike
		-- like
		-- % 替换任意个
		-- _ 替换1个
		-- 查询姓名中 以 "小" 开始的名字
        select name from students where name like '小%';

		-- 查询姓名中有 "小" 所有的名字
        select name from students where name like '%小%';

		-- 查询有2个字的名字
        select name from students where name like '__';

		-- 查询有3个字的名字
        select name from students where name like '___';

		-- 查询至少有2个字的名字
        select name from students where name like '__%';

		-- rlike 正则
		-- 查询以 周开始的姓名
		select name from students where name rlike '^周';

		-- 查询以 周开始、伦结尾的姓名
        select name from students where name rlike '^周.*伦$';

	-- 范围查询: in, not in, between and, not between and
		-- in (1, 3, 8)表示在一个非连续的范围内
		-- 查询 年龄为18或34的姓名
		select name, age from students where age = 18 or age = 34;
        select name, age from students where age in (18, 34);

		-- not in 不非连续的范围之内
		-- 年龄不是 18、34岁之间的信息
        select name, age from students where age not in (18, 34);

		-- between ... and ...表示在一个连续的范围内
		-- 查询 年龄在18到34之间的的信息
        select name, age from students where age between 18 and 34;

		-- not between ... and ...表示不在一个连续的范围内
		-- 查询 年龄不在在18到34之间的的信息
        select name, age from students where age not between 18 and 34;

	-- 空判断
		-- 判空is null
		-- 查询身高为空的信息
		select * from students where hight is null;

		-- 判非空is not null
        select * from students where hight is not null;

-- 排序
	-- order by 字段
	-- asc从小到大排列，即升序
	-- desc从大到小排序，即降序

	-- 查询年龄在18到34岁之间的男性，按照年龄从小到到排序
    select * from students where (age between 18 and 34 ) and gender = 1 order by age;

	-- 查询年龄在18到34岁之间的女性，身高从高到矮排序
    select * from students where (age between 18 and 34) and gender = 2 order by hight desc;

	-- order by 多个字段
	-- 查询年龄在18到34岁之间的女性，身高从高到矮排序, 如果身高相同的情况下按照年龄从小到大排序
    select * from students where (age between 18 and 34) and gender = 2 order by hight desc, id desc;

	-- 查询年龄在18到34岁之间的女性，身高从高到矮排序, 如果身高相同的情况下按照年龄从小到大排序,
	-- 如果年龄也相同那么按照id从大到小排序
    select * from students where (age between 18 and 34) and gender = 2 order by hight desc, age, id desc;

	-- 按照年龄从小到大、身高从高到矮的排序
    select * from students order by age, hight desc;

-- 聚合函数：count, max, min, sum, avg, round
	-- count：总数
	-- 查询男性有多少人，女性有多少人
    select count(*) as 男性 from students where gender = 1;
    select count(*) as 男性 from students where gender = 2;

	-- max：最大值
	-- 查询最大的年龄
    select max(age) from students;

	-- 查询女性的最高 身高
    select max(hight) from students where gender = 2;

	-- min：最小值
    select min(age) from students;

	-- sum
	-- 计算所有人的年龄总和
    select sum(age) from students;

	-- avg
	-- 计算平均年龄
    select avg(age) from students;

	-- 计算平均年龄 sum(age)/count(*)
    select sum(age) / count(*) from students;

	-- 四舍五入 round(123.23 , 1) 保留1位小数
	-- 计算所有人的平均年龄，保留2位小数
    select round(avg(age), 2) from students;

	-- 计算男性的平均身高 保留2位小数
	select round(avg(hight), 2) from students where gender = 1;

-- 分组

	-- group by
	-- 按照性别分组,查询所有的性别
    select gender from students group by gender;

	-- 计算每种性别中的人数
    select gender, count(*) from students group by gender;

	-- 计算男性的人数
    select gender, count(*) from students where gender = 1 group by gender;

    -- 查看分组内的内容
	-- group_concat(...)
	-- 查询同种性别中的姓名
    select gender, group_concat(name) from students group by gender;
    select gender, group_concat(name, "_", age, "_", id) from students group by gender;

	-- having
	-- 查询平均年龄超过30岁的性别，以及姓名 having avg(age) > 30
    select gender, group_concat(name) from students group by gender having avg(age) > 30;
	
	-- 查询每种性别中的人数多于2个的信息
    select gender, group_concat(name) from students group by gender having count(*) > 2;

-- 分页
	-- limit start, count：规律---> limit count * (页数 - 1), count
	-- 限制查询出来的数据个数
    select * from students limit 2;

	-- 查询前5个数据
    select * from students limit 0, 5;

	-- 查询id 6-10（包含）的书序
    select * from students limit 5, 5;

	-- 每页显示2个，第1个页面
    select * from students limit 0, 2;

	-- 每页显示2个，第2个页面
    select * from students limit 2, 2;

	-- 每页显示2个，第3个页面
    select * from students limit 4, 2;

	-- 每页显示2个，第4个页面
	select * from students limit 6, 2;

	-- 每页显示2个，显示第6页的信息, 按照年龄从小到大排序
	select * from students limit 10, 2;

-- 连接查询
	-- inner join ... on

	-- select ... from 表A inner join 表B;
    select * from students inner join classes;

	-- 查询 有能够对应班级的学生以及班级信息
    select * from students inner join classes on students.cls_id = classes.id;

	-- 按照要求显示姓名、班级
    select students.*, classes.classname from students inner join classes on students.cls_id = classes.id;
    select students.name, classes.classname from students inner join classes on students.cls_id = classes.id;

	-- 给数据表起名字
    select s.name, c.classname from students as s inner join classes as c on s.cls_id = c.id;

	-- 查询 有能够对应班级的学生以及班级信息，显示学生的所有信息，只显示班级名称
    select s.*, c.classname from students as s inner join classes as c on s.cls_id = c.id;
	
	-- 在以上的查询中，将班级姓名显示在第1列
    select c.classname, s.* from students as s inner join classes as c on s.cls_id = c.id;

	-- 查询 有能够对应班级的学生以及班级信息, 按照班级进行排序
    select c.classname, s.* from students as s inner join classes as c on s.cls_id = c.id order by c.classname;

	-- 当时同一个班级的时候，按照学生的id进行从小到大排序
    select c.classname, s.* from students as s inner join classes as c on s.cls_id = c.id order by c.classname, s.id;

	-- left join
	-- 查询每位学生对应的班级信息
    select * from students as s left join classes as c on s.cls_id = c.id;

	-- 查询没有对应班级信息的学生
	-- select ... from xxx as s left join xxx as c on..... where .....
	-- select ... from xxx as s left join xxx as c on..... having .....

	-- right join   on
	-- 将数据表名字互换位置，用left join完成

-- 自关联
	-- 省级联动 url:http://demo.lanrenzhijia.com/2014/city0605/
	-- 查询所有省份
    select * from areas where pid is null;

	-- 查询出山东省有哪些市
    select id from areas where aname = '山东省';
    select * from areas where id = 370000;

    select city.* from areas as city inner join areas as province on city.pid = province.id where province.aname = '山东省';

	-- 查询出青岛市有哪些县城
    select * from areas where id = 370200;

-- 子查询
	-- 标量子查询
	-- 查询出高于平均身高的信息
	select * from students where age > (select avg(age) from students);

	-- 查询最高的男生信息
    select * from students where hight = (select max(hight) from students);

	-- 列级子查询
	-- 查询学生的班级号能够对应的学生信息
	select * from students where cls_id in (select id from classes);
