# 这个是之前在Pycharm里面写的代码,可能有运行错误,因为是直接粘贴过来的,但在Pycharm里全部成功运行

## 练习代码
### 9月17日
print("hello world")
print("hello python")

print("##########")
print("白日依山尽")
 #变量

 base,incr = 20.7,50

 print("未来第一个月的播放总量:", base+incr)
 print("未来第二个月的播放总量:", base+incr+incr)

 s1 = "hello"
 s2 = 'python'
 s3 = """
 hello:
     欢迎大家
     天天开心哦
 """
 print(s1)
 print(s2)
 print(s1)
 print(type(s1))
 print(type(s2))
 print(type(s3))

 msg = ('it\' very good')
 print(msg)
 print ("\t欢迎大家\n\t天天开心哦")

 s1 = "\t人生苦短""我用python"",ok"
 print(s1)

 mgs1 = "人生苦短"
 mgs2 = "我用python"
 print("\t要说:"+mgs1+","+mgs2)

 s1 = "大家好"",我是中国人"",今年十七岁"",就读于软件工程"
 print(s1)

name = "人"
age = 18
pro = "软件工程"
print("大家好,我是"+name+",今年"+str(age)+"岁,我学习的专业是"+pro)
print("大家好,我是%s,今年%s岁,我学习的专业是%s"%(name,age,pro))
print(f"大家好,我是{name},今年{age}岁,我学习的专业是{pro}")
### 9月18日
name = input("请输入你的姓名:")
age = input("请输入你的年龄:")
print(f"你的姓名是{name},年龄为{age}")

total =10000
password = input("你的银行卡密码为:")
print(f"密码正确,{password}")
num = input("请输入取款金额:")
print(f"取款后银行卡金额为:{total-int(num) }")

total =10000
password = input("你的银行卡密码为:")
print(f"密码正确,{password}")
num = int(input("请输入取款金额:"))
print(f"取款后银行卡金额为:{total-num }")

first = input("输入的一个数字")
second = input("输入第二个数字")
print(f"两个数字的和为{int(first)+int(second)}")

first = int(input("输入的一个数字"))
second = int(input("输入第二个数字"))
print(f"两个数字的和为{first+second}")

print("10+4=",10+4)
print("10**4=",10**4)

x = float(input("请输入x的值:"))
y=  float(input("请输入y的值:"))
print("x+y=",x+y)
print("x-y=",x-y)

x = float(input("第一个数为:"))
y = float(input("第二个数为:"))
z = float(input("第三个数为:"))
print(f"{(x+y+z)/3}")

shang = float(input("上底为:"))
xia = float(input("下底为:"))
gao = float(input("高为:"))
print(f"梯形的面积为{((shang+xia)*gao)/2}")

r = float(input("圆的半径为:"))
print(f"圆的面积为{3.14*r**2},圆的周长为{3.14*2*r}")

d1 = float(input("输入体重:"))
d2 = float(input("输入身高:"))
print(f"BMI={d1/((d2/100)**2)}")

num=85
num+=10
print("num +=10后,num=",num)

num/=10
print("num /=10后,num=",num)

num%=10
print("num %=10,num=",num)

num//=10
print("num //=10,num=",num)

num%=10
print("num %=10,num=",num)

print("100==100吗:",100==100)
print("'100'='100'吗:","100"=="100")
print("100!=100吗:",100!=100)
print("100<=100吗:",100<=100)
print("100>=100吗:",100>=100)


n = int(input("请输入一个整数"))
print(f"{n}在10-20之间:",n>=10 and n<=20)

n = int(input("请输入一个整数"))
print(f"{n}在10-20之间:",n<10 or n>20)

score = 688
if score > 680:
    print("恭喜你可以去清华读书")
    print("哈哈哈")

ok_account= "18888888"
ok_password = "666888"
account = input("输入您的B站账号:")
password = input("输入您的B站密码:")
if account == ok_account and password == ok_password:
    print("登陆成功")
    print("登录B站首页")
if account != ok_account or password != ok_password:
    print("登陆失败")

ok_account= "18888888"
ok_password = "666888"
account = input("输入您的B站账号:")
password = input("输入您的B站密码:")
if account == ok_account and password == ok_password:
    print("登陆成功")
    print("登录B站首页")
else:
    print("登陆失败")

year =int( input("请输入需要判断的年份:"))
if (year % 100!=0 and year%4 == 0) or(year % 400==0):
    print(f"{year}是闰年")
else:
    print(f"{year}是平年")


num =int(input("输入数字:"))
#### 字符串--数字类型
if num%2==0:
    print(f"{num}为偶数")
else:
    print(f"{num}为奇数")

age =int(input("请输入你的年龄"))
if age>=18:
    print("已成年")
else:
    print("未成年")

score =int(input("请输入你的分数"))
if score >= 60:
    print("及格啦")
else:
    print("未合格哦")

num =int(input("输入一个数字"))
if num>0:
    print(f"{num}为正数")
elif num<0:
    print(f"{num}为负数")
else:
    print(f"{num}为0")

username = input("输入你的用户名:")
password = input("输入你的密码:")

  ####为什么加双引号:input输出的是字符串,字符串要加引号(比较的是文本)
if username == "root" and password == "547527":
    print("登陆成功")
elif username == "root" and password == "547527":
    print("登陆成功")
elif username == "zhangsan" and password == "123456":
    print("登陆成功")
else:
    print("登陆失败,用户名或密码错误")


score =int(input("输入你的考试分数"))
if score >= 85:
    print("优秀")
elif score >= 60 and score <= 85:
    print("合格")

sum = int(input("输入你的购买金额"))
if sum>=500:
    print(f"应付款{sum*0.8}")
elif sum>=300 and sum<=500:
    print(f"应付款{sum*0.9}")
elif sum>=100 and sum<=200:
    print(f"应付款{sum*0.95}")
else:
    print(f"应付款{sum}")

a = int(input("输入第一条边:"))
b = int(input("输入第二条边:"))
c = int(input("输入第三条边:"))

if a + b >c and b + c > a and a + c > b:
    if a == b and b == c:
        print(f"{a} {b} {c}这个三角形是等边三角形")
    elif a == b or b == c or a == c:
        print(f"{a} {b} {c}这个三角形是等腰三角形")
    else:
        print(f"{a} {b} {c}这个三角形是普通三角形")
else:
    print(f"{a} {b} {c}这三个边长不能构成三角形")

a = int(input("输入年度电量"))
if a <2880:
    print(f"电费为{a*0.4883}")
elif a >=2880 and a<=4800:
    print(f"电费为{2880*0.4883+(a-2880)*0.5383}")
else:
    print(f"电费为{2880*0.4883+(4800-2880)*0.5383+(a-4800)*0.7883}")
### 9月19日
day = input("今天星期几(1-7):")
match day:
    case "1":
        print("周一:工作会议日")
    case "2":
        print("周二:学习培训日")
    case "3":
        print("周三:项目开发日")
    case "4":
        print("周四:代码审查日")
    case "5":
        print("周五:总结规划日")
    case "6"|"7":
        print("周末:放松休息")
    case _:
        print("输入有误")

num1 = float(input("请输入第一个数:"))
num2 = float(input("请输入第二个数:"))
oper = input("请输入运算符:")
match oper:
    case "+":
        print(f"{num1}+{num2}={num1+num2}")
    case "_":
        print(f"{num1}-{num2}={num1-num2}")
    case "*":
        print(f"{num1}*{num2}={num1*num2}")
    case "/" if num2!=0:
        print(f"{num1}//{num2}={num1/num2}")
        print(f"{num1}/{num2}={num1/num2}")
    case _:
        print("操作不支持")

act = input("玩家输入指令:")
match act:
    case "上"|"w"|"W":
        print("角色向上移动")
    case "下"|"s"|"S":
        print("角色向下移动")
    case "左"|"a"|"A":
        print("角色向左移动")
    case "右"|"d"|"D":
        print("角色向右移动")
    case "跳"|" ":
        print("角色跳跃")
    case "攻击"|"j"|"J":
        print("角色发动攻击")
    case "退出"|"esc"|"ESC":
        print("角色退出游戏")

i = 0
while i<10:
    print("人生苦短,我用python")
    i += 1
else:
    print("循环正常结束")

total = 0
i = 1
while i <= 100:
    if i % 2 == 0:
        total += i
    i += 1
print(f"累加之和等于:{total}")

total = 0
i = 0
while i<=100:
  total += i
  i += 2
print(f"累加数字之和为{total}")

msg = input("请输入需要遍历的字符串")
for s in msg:
    print(f"元素:{s}")
else:
    print("遍历结束")

total = 0

for i in range(1,101,2):
     total += i
print("1-100之间的奇数和为:",total)

total = 0

for i in range(100,501):
     if i%3==0  :
        total += i
print("100-500之间的所有3的倍数和为:",total)

total =0
for i in range(102,501,3):
    # 此时起始数据不可以为100,即如果起始数据不是倍数,就会把不符合的数据加进去
    #                         注意!!! 先找到区间中第一个符合的数据放到range的开头
    total += i
print("100-500间所有3的倍数之和为:",total)
print("*")
#### 自带换行效果,每次执行都会输出在新的一行中
print("*",end="")
#### end表示的是每一次输出以什么结束,默认\n,表示换行
m = int(input("请输入长方形的长度:"))
n = int(input("请输入长方形的宽度:"))
for j in range(n):
    for i in range(m):
        print("*",end=" ")
    print()
### 9月20日
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i}={j*i}",end="\t")
    print()

for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="\t")
    print()

for i in range(1,7):
    for j in range(1,i+1):
        print(f"{j}",end="\t")
    print()

for i in range(1,9):
    for j in range(1,9):
        if (i+j) % 2 == 0:
            print("黑",end="\t")
        else:
            print("白",end="\t")
    print()

while True:
    username = input("请输入你的用户名:")
    password = input("请输入你的密码:")
    if username == "" or password == "":
        print("输入的用户名和密码不能为空.请重新输入")
        continue
    if username == "admin" and password == "666888":
        print("登陆成功")
        break
    elif username == "zhangsan" and password == "123456":
        print("登陆成功")
        break
    elif username == "taoge" and password == "888666":
        print("登陆成功")
        break
    else:
        print("登陆失败")

count = 0
while count < 5:
    username = input("请输入你的用户名:")
    password = input("请输入你的密码:")
    if (username == "admin" and password == "666888") or (username == "zhangsan" and password == "123456") or (username == "taoge" and password == "888666"):
        print("登陆成功")
        break
    else:
        count += 1
        remain=5-count
        print("密码错误,还有{remain}次机会")
else:
    print("五次全部错误,不允许操作")

count = 0
while True:
    if count >=5:
        print("5次全部输入错误，不允许再操作！")
        break
    username = input("请输入用户名：")
    password = input("请输入密码：")
    if (username == "admin" and password == "666888") or (username == "zhangsan" and password == "123456") or (username == "taoge" and password == "888666"):
        print("登录成功！")
        break
    else:
        count += 1
        print(f"账号或密码错误，剩余{5-count}次机会")

import random
random_number = random.randint(1, 100)
while True:
    num=int(input("请输入一个数字:"))
    if num > random_number:
        print("大了")
    elif num < random_number:
        print("小了")
    else:
        print("对啦 666")
        break
print("随机生成的数字是:",random_number)

total = 0
for num in range(5,5001,5):
    total+= num
print(total)

s =[56,90,88,65,90,"A","hello",True]
print(type(s))
print(s[0])
print(s[-8])
s[5]="abc"
print(s)
for x in s:
    print(x,end=" ")

s = ["A","B","C","D","E","F","G","H","I","J"]
print(s[0:5:1])
print(type(s[0:5:1]))
print(s[:5:1])
print(s[:5])
print(s[:-2:1])


s =[5,45,67,8,44,23,56,87,11]
s.append(1) 
最后一项后面加
print(s)
s.insert(2,80) 
第三项后面加
print(s)
s.remove(67) 
移除第一个出现的67
print(s)
e=s.pop(1) 
移除第二个是什么
print(e)
print(s)
s.sort() 
排序
print(s)
s.reverse() 
反转
print(s)

num_list = []
for i in range(10):
    num = int(input("请输入一个有效数字:"))
    num_list.append(num)
print ("数字列表",num_list)
num_list.sort()
print("排序后的数字列表",num_list)
print("最小值:",num_list[0])
print("最大值:",num_list[-1])
print("平均值:",sum(num_list)/len(num_list))

num_list1 = [19,23,54,64,875,20,109,232,123,54]
num_list2 = [55,80,72,35,60,123,54,29,91]
#### 合并 去除重复记录
for num in num_list2:
    num_list1.append(num)
print("合并后的原始列表",num_list1)
new_list = []
for num in num_list1:
    # 判断其中是否存在num元素
    if num not in new_list:
        new_list.append(num)
print("去除重复元素后的列表:",new_list)
new_list.sort()
print("排序后的不重复列表:",new_list)

num_list1 = [19,23,54,64,875,20,109,232,123,54]
num_list2 = [55,80,72,35,60,123,54,29,91]
合并 去除重复记录
num_list = num_list1+num_list2
print("合并后的原始列表",num_list)
new_list = []
for num in num_list:
    # 判断其中是否存在num元素
    if num not in new_list:
        new_list.append(num)
print("去除重复元素后的列表:",new_list)
new_list.sort()
print("排序后的不重复列表:",new_list)

num_list = []
for i in range(1,21):
    num_list.append(i**2)
print(num_list)
num_list = [i**2 for i in range(1,21)]
print(num_list)
num_list = [12,32,45,77,80,92,33,57,97,110,111,112]
new_list = [i**2 for i in num_list if i%2==0]
print(new_list)

list1 = ['M','A','C','E','F','G','H','N','I']
list2 = ['X','Z','T','D','G']
list3 = ['W','S','A','D','E','F','G']
num_list = list1 + list2 + list3
print(num_list)
new_list = []
for num in num_list:
    if num not in new_list:
        new_list.append(num)
print("去除重复元素后的序列:", new_list)
### 9月21日
s = "hello-python"
print(s[4])
print(s[-8])
for i in s:
    print(i)
#### 切片
print(s[0:5:1])
print(s[:5:1])
print(s[:5:])
print(s[:5])
print(s[6:12:1])
print(s[6::1])
print(s[6:])
print(s[-1:-7:-1])
print(s[::-1])
from operator import index

s = "hello-python-hello-world"
index = s.find("-")
print(index)
c = s.count("o")
print(c)
sl = s.lower()
print(sl)
slist = s.split("-")
print(slist)
ss = s.strip()
print(ss)
sr = s.replace("-", "")
print(sr)
print(s.startswith("python"))
print(s.endswith("python"))

print(s)

#### 元组-tuple 元素可以重复,有序,不可修改
#### 定义
t1 = (80,95,78,50,76,80,85,20)
print(t1)
print(type(t1))
#### 索引
print(t1[0])
print(t1[-1])
#### 切片
print(t1[0:5:1])
#### count统计个数
print(t1.count(80))
#### index获取元素的索引(第一个元素的位置)
print(t1.index(80))
 注意:如果定义单元素的元组,单个元素之后要加逗号
t2 = ()
print(t2)
print(type(t2))

t3 = (100,)
print(t3)


#### 元组tuple的组包与解包
组包
t1 = (5,5,7,9,6,8,9)
t2 t(t1)
print(t2)
基础解包
a,b,c,d,e,f,g = t1
print(a,b,c,d,e,f,g)
扩展解包(*包括其他所有元素)
a,b,*c,d = t1
print(a)
print(*c)

*other,last2,last1 = t1
print(*other)

a=10 b=20交换
a = 10
b = 20
t = b,a
a,b = t 解包
a,b = b,a
print(a)
print(b)

a = 100 b = 200 c = 300
a =100
b = 200
c = 300
a,b,c = c,a,b
print(a,b,c)

students = (
    ("S001","王林",85,92,78),
    ("S002","李木碗",92,88,95),
    ("S003","十三",78,85,82),
    ("S004","曾牛",88,79,91),
    ("S005","周一",95,96,89),
    ("S006","王卓",76,82,77),
    ("S007","红蝶",89,91,94),
    ("S008","徐立国",75,69,82),
    ("S009","许木",86,89,98),
    ("S010","遁天",66,59,72)
)
计算每个人总分,各科平均分  {avg:.1f}--保留一位小数 f为float

print("学号\t\t姓名\t\t语文\t\t数学\t\t英语\t\t总分\t\t平均分")
方式一
for s in students:
    total = s[2]+s[3]+s[4]
    avg = total/3
    print(f"{s[0]} \t {s[1]} \t {s[2]} \t {s[3]} \t {s[4]} \t {total} \t {avg:.1f}")
方式二  元素解包
for id,name,chi,math,eng in students:
    total = chi+math+eng
    avg = total/3
    print(f"{id} \t {name} \t {chi} \t {math} \t {eng} \t {total} \t {avg:.1f}")

统计各科最低分,最高分,平均分
1各科成绩列表
chi_scores= [s[2] for s in students]
math_scores= [s[3] for s in students]
eng_scores= [s[4] for s in students]

2.计算
print(f"语文最低分:{min(chi_scores)},最高分:{max(chi_scores)},平均分:{sum(chi_scores)/len(chi_scores)}")
print(f"数学最低分:{min(math_scores)},最高分:{max(math_scores)},平均分:{sum(math_scores)/len(math_scores)}")
print(f"英语最低分:{min(eng_scores)},最高分:{max(eng_scores)},平均分:{sum(eng_scores)/len(eng_scores)}")

优秀学生90分
方式一
print("优秀学生如下(平均分>90):")
for s in students:
    total = s[2]+s[3]+s[4]
    avg = total/3
    if avg > 90:
        print(f"学号:{s[0]},姓名:{s[1]},平均分:{avg:.1f}")
方式二
print("优秀学生如下(平均分>90):")
for id,name,chi,math,eng in students:
    total = chi+math+eng
    avg = total/3
    if avg > 90:
        print(f"学号:{id},姓名:{name},平均分:{avg:.1f}")

#### 集合set
s1 ={5,3,2,0,9,12,43,64,22,5,0}
print(s1)
print(type(s1))

s2 = set()
print(s2)
print(type(s2))

s1 = {100,200,300,400,500,600,700,800}
print(s1)
#### add()添加元素到集合
s1.add(1200)
print(s1)
#### remove() 移除指定元素
s1.remove(200)
print(s1)
#### e = pop() 随机删除并返回
e = s1.pop()
print(e)
print(s1)
#### 清空集合
s1.clear()
print(s1)

s2 = {"A","B","C","D","E","X","Y"}
s3 = {"C","E","Y","Z"}
 difference() 求两个集合的差集 存在于第一个,不在第二个
print(s2.difference(s3))
print(s3.difference(s2))
 union() 并集
print(s2.union(s3))
 intersection() 交集
print(s2.intersection(s3))

football_set = {"王林", "曾牛", "徐立国", "通天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}
basketball_set = {"张铁", "墨居仁", "王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}
french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子", "红蝶", "厉飞雨", "韩立", "曾牛"}
art_set = {"通天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}
 #1.法语和艺术同时选择
选择法语和艺术
a =french_set.intersection(football_set)
print(f"同时选择了法语和艺术的学生右:{a}")
方式二 &--交集
a2 =french_set&art_set
print(f"同时选取法语和艺术的学生右:{a2}")
   同时选了四个
all_set = football_set & basketball_set & french_set & art_set
print(f"全部选了的学生:{all_set}")
3.选了足球没有选篮球 求差集
方法一
fb_set=football_set.difference(basketball_set)
print(f"选了足球没有选篮球的:{fb_set}")
方法二  -
fb_set2=football_set-basketball_set
print(f"选了足球没有选篮球的:{fb_set2}")
方式三 集合推导式---快速构建集合,语法{要往集合中添加的数据 for s in set1 if 条件}
fb_set3={s for s in football_set if s not in basketball_set}
print(f"选了足球没有选篮球的:{fb_set3}")
4.统计每一个学生选择的课程数量
4.1获取学生名单 并集(|) 自动去重
all_set=football_set|basketball_set|french_set|art_set
all_list = football_set.union(basketball_set).union(french_set).union(art_set)
4.1 获取每一个学生选择的课程数量  学生名字出现了多少次就选了几门课  set不可出现重复,list可以出现重复
all_list = [*football_set,*basketball_set,*french_set,*art_set]
for s in all_set:
    print(f"{s}选修了{all_list.count(s)}门课程")
### 9月22日
#### 定义字典
字典名称={key:value...} key不可重复 若重复后面覆盖前面 key必须为不可变类型(str,int,float,tuple)不能是list,set,dict
dict1 = {"王林":670,"利姆湾":608,"徐立国":580,"韩立":680}
print(dict1)
print(type(dict1))
print(dict1["利姆湾"])
dict1["利姆湾"]=688
print(dict1)
dict1 = {"王林":670,"利姆湾":608,"徐立国":580,"韩立":680}
print(dict1)
#### 添加
dict1["涛哥"]=550
print(dict1)
#### 修改
dict1["涛哥"]=620
print(dict1)
#### 查询
print(dict1["涛哥"])
print(dict1.get("涛哥"))
print(dict1.keys())
print(dict1.values())
print(dict1.items())
#### 删除
score = dict1.pop("徐立国")
print(score)
print(dict1)
del dict1["韩立"]
print(dict1)
#### 遍历
for k  in dict1.keys():
    print(f"{k}:{dict1[k]}")
for items in dict1.items():
    print(f"{items[0]}:{items[1]}")
rom curses.textpad import rectangle 案例
    shopping_cart = {}
    menu = """########购物车系统##########       1.添加购物车      #
      2.修改购物车      #
      3.删除购物车      #
      4.查询购物车      #
      5.退出购物车      #
    #########################
    """# 制作菜单
print("欢迎使用购物车管理系统")
print(menu)
执行的具体操作
choice = input("请选择你要执行的操作(1-5)")
match choice:
添加购物车
    case "1":
        goods_name = input("请输入商品名称")
        goods_price= float(input("请输入商品价格"))
        goods_num= int(input("请输入商品数量"))
        if goods_name in shopping_cart:
            print("该商品已经存在,请重新选择")
        else:
            shopping_cart[goods_name] = {"price":goods_price,"num":goods_num}
            print("商品添加完毕")
修改购物车
    case "2":
        goods_name = input("请输入要修改商品名称")
        goods_price = float(input("请输入最新商品价格"))
        goods_num = int(input("请输入最新商品数量"))
        # 如果商品不存在,提示错误信息,重新选择
        if goods_name not in shopping_cart:
            print("商品不存在,请重新选择")
        else:
            shopping_cart[goods_name] = {"price":goods_price,"num":goods_num}
            print("商品修改完毕")
删除购物车
    case "3":
        goods_name = input("请输入要删除商品名称")
        if goods_name not in shopping_cart:
            print("该商品不存在,重新选择")
        else:
            del shopping_cart[goods_name]
            print("商品删除完毕")
查询购物车
    case "4":
        for goods_name in shopping_cart.keys():
            goods_info=shopping_cart[goods_name]
            print(f"商品名称:{goods_name},商品价格:{goods_info['price']},商品数量:{goods_info['num']}")
    case "5":
        print("bye")
        running=False
    case _:
        print("非法操作")
### 9月23日
#### 函数定义  1.并不会执行,在调用时才会执行  2.先定义再调用def out_line():
print("-------------------")
print("-------------------")
#### 函数调用
      # out_line() 函数的参数和返回值1
def circle_area(r):
    area=3.14*r*r
    return area
area=circle_area(10)
print(area)
def rectangle_area(l,w):
    print(rectangle_area(20,10))
#### 返回值多个 逗号分隔 多个返回值封存到元组中
def circle_area_len(r):
    return 3.14*r*r,2*3.14*r
    al = circle_area_len(10)
    print(print(type(al)))
    #解包
    def circle_area_len(r):
        return round(3.14*r*r,1),round(2*3.14*r,1)
        al = circle_area_len(10)
        print(print(type(al)))
        area,len = circle_area_len(10)
        print(area)
        print(len) 
        def triangle_area(b,h):
            return b*h/2
print("底长为30,高度为20的三角形面积为:",rectangle_area(30,20))


def count_aeiou(s):
    num = 0
    for w in s:
        if w in 'aeiouAEIOU':
            num += 1
            return num
            print(count_aeiou("hello python hello world"))
            def calc_score(score_list):
                max_s = max(score_list)
                min_s = min(score_list)
                avg_s = round(sum(score_list) / len(score_list),1)
                return max_s, min_s, avg_s
                s_list = [123,456,334,556,556,776,766]
                max_s, min_s, avg_s = calc_score(s_list)
                print("最高分:", max_s)
                print("最低分:", min_s)
                print("平均分:", avg_s)
### 9月24日
#### 函数说明文档(Docstring)
"""

"""
#### 解释函数的功能,参数,返回值等
#### 查看函数说明文档:help函数 eg.help(circle_area_len)
鼠标悬浮在函数上,自动显示

#### 函数的嵌套调用:在一个函数中,又调用另一个函数
def function_a():
    print("a...before")
    function_b()
    print("a...after")

def function_b():
    print("b...before")
    function_c()
    print("b...after")

def function_c():
    print("c...")

function_a()
print("函数调用完毕")
1.算三角形面积
def triangle_area(b,h):
    return b*h/2
print("底长为 30 ,高度为 20 的三角形面积:",triangle_area(30,20))
2.计算传入的字符串中元音字母的个数 aeiouAEIOU
def count_aeiou(s):
    num = 0
    for w in s:
         if w in 'aeiou':           num += 1
     return num
 print(count_aeiou("hello python hello world"))
 
 3.计算传入的班级学院高考成绩列表中最高分,最低分,平均分(保留一位小数)
 def calc_score(score_list):
     max_s = max(score_list)
     min_s = min(score_list)
     avg_s = round(sum(score_list)/len(score_list),1)
     return max_s, min_s, avg_s
 s_list = [123,456,334,556,556,776,766]
 max_s, min_s, avg_s = calc_score(s_list)
 print("最高分:",max_s)
 print("最低分:",min_s)
 print("平均分:",avg_s)
