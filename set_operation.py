n=int(input("Set Operation (1=Union, 2=Intersection,3=Complement, 4=Difference, 5=Cross Product):"))
m=input("A:")[1:-1].split(",")
l=[]
k=[]
o=[]
l= [(int(i)) for i in m]

if n==1 or n==2 or n==4 or n==5:
  p=input("B:")[1:-1].split(",")
  if(len(p)==0):
    k=[]
  else:
    k= [(int(i)) for i in p]

if n==1: 
  for i in k:
    if i not in l:
      l+=[i]
  print(f"A U B:{l}")
elif n==2:
  for i in k:
    if i  in l:
      o+=[i]
  print(f"A ∩ B:{o}")
elif n==3:
  p=input("Universal Set, U:")[1:-1].split(",")
  k= [(int(i)) for i in p]
  flag=True
  for i in l:
    if i not in k:
      print("Error: First Set Containing Elements that are not a Partof the Universal Set.")
      flag=False
      break
  if flag==True:
    for i in l:
     if i in k:
        k.remove(i)
    print(f"A’ :{k}")
elif n==4:
  for i in k:
    if i in l:
      l.remove(i)
  print(f"A – B:{l}")
elif n==5:
  if len(l)>0 and len(k)>0:
    for i in l:
      for j in k:
        a=[i]+[j]
        o.append(a)
    print(f"A X B:{o}")
  else:
    if len(k)==0:
      for i in l:
        a=[i]+["None"]
        o.append(a)
    if len(l)==0:
      for i in k:
        a=["None"]+[i]
        o.append(a)
    print(f"A X B:{o}")