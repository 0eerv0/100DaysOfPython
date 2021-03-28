# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
sum = 0
nr = 0
for a in student_heights:
  sum += a
print(f"sum of heights = {sum}")
for i in student_heights:
  nr +=1
print(f"number of students = {nr}")
average = round(sum / nr)
print(f"The average of heights is: {average}")



