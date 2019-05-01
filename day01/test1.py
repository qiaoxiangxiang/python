
# input 输入框复习
# number = input("您的微信号是: ");
# name = input("您的名字是: ");
# age = input("您的年龄是：");
# print("他的微信号是",number+",他的名字是 ",name+",他今年",age);

#  小练习  计算一人的体指
strong = float(input("您的体重是(kg)： "));
shengao = float(input("您的身高是(m)： "));
tizhi = strong/(shengao*shengao);
fanwei = '';

if(tizhi >=28):
  fanwei = '肥胖';
else:
  if(24.0 <= tizhi < 27.9):
    fanwei = "过重";
  else:
    if(18.5 <= tizhi < 23.9):
      fanwei = "正常";
    else:
      if(tizhi <= 18.4):
        fanwei = "偏瘦";
        
print("您的体指是："+str(tizhi),fanwei)         

