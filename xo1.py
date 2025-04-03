a=['_','_','_']
b=['_','_','_']
c=['_','_','_']
d=['_','_','_']
num=0
ch=[]
chance='X'
def again():
 global num,chance,ch,a,b,c,d
 choice=input('Do you want to play a game again:')
 if (choice=='y')or(choice=='Y')or(choice=='yes')or(choice=='Yes'):
   print("Well all the best :)")
   chance='X'
   num=0
   ch.clear()
   a.clear()
   b.clear()
   c.clear()
   a+=d
   b+=d
   c+=d   
   intro()
   tic_tac_toe()
 else:
   print("OK BYE!")
   chance=2
def draw():
 global a,b,c,chance,num
 if ('_'not in a)and('_'not in b)and('_'not in c):
  print("=-=-=-=-=-=Game Draw=-=-=-=-=-=")
  chance=1
  num=9
  again()
 else:
  pass
def intro():
 print("Following is the way to number the boxes")
 print('1,2,3')
 print('4,5,6')
 print('7,8,9')
 print(a)
 print(b)
 print(c)
 print('X starts first')
def x_win():
 global a,b,c,chance,num
 for i in range(0,3):
  if a[i]==b[i]==c[i]=='X':
   print("X Won")
   a.clear()
   b.clear()
   c.clear()
   a+=d
   b+=d
   c+=d
   chance=1
   num=9
   break
 if ('O'not in a)and('_'not in a):
  print("X Won")
  a.clear()
  a+=d
  chance=1
  num=9
 elif ('O'not in b)and('_'not in b):
  print("X Won")
  b.clear()
  b+=d
  chance=1
  num=9
 elif ('O'not in c)and('_'not in c):
  print("X Won")
  c.clear()
  c+=d
  chance=1
  num=9
 elif(a[0]==b[1]==c[2]=='X'):
  print("X Won")
  a.clear()
  a+=d
  chance=1
  num=9
 elif(c[0]==b[1]==a[2]=='X'):
  print("X Won")
  a.clear()
  a+=d
  chance=1
  num=9
 else:
   pass
def o_win():
 global a,b,c,chance,num
 for i in range(0,3):
  if (a[i]==b[i]==c[i]=='O'):
   print("O Won")
   a.clear()
   b.clear()
   c.clear()
   a+=d
   b+=d
   c+=d
   chance=1
   num=9
   break 
 if ('X'not in a)and('_'not in a):
  print("O Won")
  a.clear()
  a+=d
  chance=1
  num=9
 elif ('X'not in b)and('_'not in b):
  print("O Won")
  b.clear()
  b+=d
  chance=1
  num=9
 elif ('X'not in c)and('_'not in c):
  print("O Won")
  c.clear()
  c+=d
  chance=1 
 elif(a[0]==b[1]==c[2]=='O'):
  print("O Won")
  a.clear()
  a+=d
  chance=1
  num=9
 elif(c[0]==b[1]==a[2]=='O'):
  print("O Won")
  a.clear()
  a+=d
  chance=1
  num=9
 else:
   pass
def x():
 global chance,ch,dr,a,b,c
 while chance=='X':
  print('X chance')
  print('1,2,3')
  print('4,5,6')
  print('7,8,9')
  n=int(input("Enter your Box:"))
  if n in ch:
   print("That box is not available")
   continue
  else:
   if n not in ch:
    if (n>0)and(n<=3):
     a[n-1]='X'
     ch.append(n)
     chance='Y'
    elif(n>3)and(n<=6):
     b[n-4]='X'
     ch.append(n)
     chance='Y'
    elif(n>6)and(n<=9):
     c[n-7]='X'
     ch.append(n)
     chance='Y'
    else:
     print("Enter a number between 1-9")
   else:
    print("That box is not available") 
   print(a)
   print(b)
   print(c) 
def o():
 global chance,ch,dr,a,b,c
 while chance=='Y':
  print('O chance')
  print('1,2,3')
  print('4,5,6')
  print('7,8,9')
  n=int(input("Enter your Box:"))
  if n in ch:
   print("That box is not available")
   continue
  else:
   if n not in ch:
    if (n>0)and(n<=3):
     a[n-1]='O'
     ch.append(n)
     chance='X'
    elif(n>3)and(n<=6):
     b[n-4]='O'
     ch.append(n)
     chance='X'
    elif(n>6)and(n<=9):
     c[n-7]='O'
     ch.append(n)
     chance='X'
    else:
     print("Enter a number between 1-9")
   else:
    print("That box is not available") 
   print(a)
   print(b)
   print(c) 
def tic_tac_toe():
 global num,chance,ch,a,b,c,d
 while (chance=='X')or(chance=='Y'):
  while chance!=1:
   while num<9:
    x_win()
    o_win()
    if (num%2==0):
     x()
    else:
     o()
    num+=1    
   else:
    x_win()
    o_win()
    draw()
  else:
   again()
intro()   
tic_tac_toe()   





