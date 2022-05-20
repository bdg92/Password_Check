password = "qwert"

n = 1
s = 1
while n >= 1:
  check = input("Enter Password")
  if check == password:
    print("Welcome to CloudyML Course")
    n = 0
  elif check != password:
    print("Wrong password")
    s +=1
    if s==4:
      print("One Last trial Left")
    elif s == 5:
      break