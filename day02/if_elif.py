# 练习14岁以下的 身高在1.5m 以下的 半票 14岁及14岁以上 1.5m及1.5m以上 全票
# shengao = float(input("请输入你的身高(m)"));
# age = int(input("请输入你的年龄"));
# if(shengao < 0 and shengao > 4):
#   print("请输入正确身高");
# elif age <0 :
#   print("请输入你的年龄")
# elif(shengao < 1.5 and age < 14):
#   print("你是半票");
# else:
#   print("你是全票");

import easygui as gui;
fieldsname = ["请输入您的身高","请输入您的年龄"];
xinxi = gui.multenterbox(msg="请输入身高和年龄",title="请输入信息",fields = fieldsname);
while True:
  if(xinxi == None):
    break;
  errmsg = "";
  for i in range(len(fieldsname)):
    if xinxi[i] == '':
      errmsg = fieldsname[i];
      break;
  if(errmsg == ""):
    msgtxt = "";
    if(float(xinxi[0]) < 1.5 and int(xinxi[1]) < 14):
      msgtxt = "半票";
    else:
      msgtxt = "全票";
    gui.msgbox(msg="您是"+msgtxt,title="购买票况",ok_button="确定");
    break;

  xinxi = gui.multenterbox(msg = errmsg,title = "请输入信息",fields = fieldsname,values = xinxi)
