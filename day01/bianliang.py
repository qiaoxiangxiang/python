static = 99;
static = static + 99;
print(static);
str = "abc";
strs = str;
str = 'ABC';
print(strs);

a = 10;
b = 20;
# c = a;
# a = b;
# b = c;
a,b = b,a;
print(a , b );

num = int(input());
if num >= 90 and num<100:
    print("优秀");
else:
    if num >= 80 and num < 90:
        print("中等");
    else: 
        if num < 80:
            print("差等");
