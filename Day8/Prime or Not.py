#Write your code below this line ๐
def prime_checker(number):
  is_prime = True
  for i in range(2, number):
    if number % i == 0:
      is_prime = False
  if is_prime == True:
    print("Number is Prime")
  elif is_prime == False:
    print("Number is Not Prime")
#Write your code above this line ๐
    
#Do NOT change any of the code below๐
n = int(input("Check this number: "))
prime_checker(number=n)



