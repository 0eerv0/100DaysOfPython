# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
un_names = name1 + name2
lower_un = un_names.lower()
t = lower_un.count('t')
r = lower_un.count('r')
u = lower_un.count('u')
e = lower_un.count('e')
first_num = t + r + u + e
l = lower_un.count('l')
o = lower_un.count('o')
v = lower_un.count('v')
e = lower_un.count('e')
second_num = l + o + v + e
score = int(str(first_num) + str(second_num))