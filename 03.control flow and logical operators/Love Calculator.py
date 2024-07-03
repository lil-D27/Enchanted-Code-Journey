print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

n1_LS = name1.lower()
n2_LS = name2.lower()

t=n1_LS.count("t")+n2_LS.count("t")
r=n1_LS.count("r")+n2_LS.count("r")
u=n1_LS.count("u")+n2_LS.count("u")
e1=n1_LS.count("e")+n2_LS.count("e")
true=t+r+u+e1

l=n1_LS.count("l")+n2_LS.count("l")
o=n1_LS.count("o")+n2_LS.count("o")
v=n1_LS.count("v")+n2_LS.count("v")
e2=n1_LS.count("e")+n2_LS.count("e")
love=l+o+v+e2

total = str(true)+str(love)
Total=int(total)

if Total < 10 or Total < 90:
  print(f"Your score is {Total}, you go together like coke and mentos.")
elif Total > 40 and Total < 50:
  print(f"Your score is {Total}, you are alright together.")
else:
  print(f"Your score is {Total}")

