
import easygui as gui;


#单独弹框 一个按钮
OK = gui.msgbox(msg="今天过得好吗？",title="早安问候",ok_button="还不错");
print(OK);


#两个按钮  是或非
isok = gui.ccbox(msg="还想玩吗？",title="亲还玩吗？",choices=("还想玩一次","不想玩了"));
if(isok):
    print("我去买票");
else:
    print("那我们走吧");


#多个选项
xuan = gui.buttonbox(msg="你想吃什么水果？",title="选水果",choices=("香蕉","橘子","苹果"));
print(xuan);


#choicebox 选择列表 属单选   multchoicebox() 选择列表 属多选
msg = "选择你喜欢的一种业余生活"
title = ""
choicess_list = ["看书","游泳","骑自行车","玩游戏"]

radio = gui.choicebox(msg, title ,choices=choicess_list);
cheboxs = gui.multchoicebox(msg="请选择你爱吃哪些水果?",title="",choices=("西瓜","香蕉","苹果","梨"));

print(radio);
print(cheboxs);


# 弹框内输入框 输入框 enterbox单行输入  interbox 单行输入 只能输入数字且可限制大小
#enterbox(msg='Enter something.', title=' ', default='', strip=True, image=None, root=None)
#单行输入框  default 是现实默认文字
qiaohua = gui.enterbox(msg="请说出心里话",title="悄悄话",default="只有我们两人知道的");
print(qiaohua);

#integerbox(msg='', title=' ', default='', lowerbound=0, upperbound=99, image=None, root=None, **invalidKeywordArguments)
#lowerbound 限定的最小值  upperbound 限定的最大值  default 默认值
shuShuzi = gui.integerbox(msg = "考了多少分",title = "考试分数",lowerbound = 0,upperbound = 100);
print(shuShuzi);

#多行输入框
#multenterbox(msg='Fill in values for the fields.', title=' ', fields=(), values=())
fieldsName = ["*你爱的人的名字","*爱到什么程度","*为什么爱她","*爱的承诺"];
values = gui.multenterbox(msg = "请输入您的信息",title = "爱情信息",fields = fieldsName);
while True:
    errmsg = '';
    if(values == None):
        break;
    #for in 循环
    #for i in fieldsName   i值不是下标，而是数组中的值
    #for i in fieldsName  要使i值为下标，需写成 for i in range(len(fieldsName))
    # range(len(数组名称))  获取下标的方法
    for  i in range(len(values)):
        print(fieldsName[i])
        if(values[i]):
            print(values[i])
        else:
            errmsg = "请认真填写"+fieldsName[i];
            break;
    if(errmsg == ''):
        break;
    values = gui.multenterbox(msg = errmsg ,title = "爱情信息",fields = fieldsName,values = values);
            

print(values);

#passwordbox  只有输入密码一个输入框 *号显示
#enterbox 也可做密码输入，不过是数字显示
#multpasswordbox 输入用户名、密码
#passwordbox(msg='Enter your password.', title=' ', default='', image=None, root=None)
#multpasswordbox(msg='Fill in values for the fields.', title=' ', fields=(), values=())
passwordnum = gui.passwordbox(msg="请输入密码",title="输入密码");
YHpassword = gui.multpasswordbox(msg="用户登录接口",title="请输入用户民和密码",fields=("用户名","密码"));
print(passwordnum);
print(YHpassword);
