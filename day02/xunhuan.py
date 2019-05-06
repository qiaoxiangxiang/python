# 
#   range 函数 正常默认参数有三个  range(1,10,1)
#   参数一  从1开始走 
#   参数二  走到10的前一位停（类似于 i<10 1，2，3，4，5，6，7，8，9 停）
#   参数三 分几步走 默认1 是 一步一步走 ，若为2 两步一走  
#   列如： range(1,10,2) 走的步数是 5 步  10/2 = 5；每次打印值为 1，3，5，7，9  

num = 0;
for i in range(1,10,2):
  print(str(i));
  num+=1;
print(str(num)+"次");

# 打印乘法口诀表
# end = ""  禁止换行
for i in range(1,10):
  for j in range(1,i+1):
    print(str(j)+"X"+str(i)+"="+str(i*j)+" ",end="")
  print("")

# while 循环
# continue 退出本轮循环
# break 退出整个循环
z = 0;
oushu = "";
jishu = "";
while z < 20:
  z+=1;
  if z%2 == 0:
    oushu = oushu + str(z) + ","
  else:
    jishu = jishu + str(z) + ","
print("奇数为"+jishu);
print("偶数为"+oushu);