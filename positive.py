List_1 = []
for i in range (5):
    num = int(input("Enter the numbers in list 1 ="))
    List_1.append(num)
    i+=1

print(List_1)

print("The positive numbers are-")
for j in range(5):
  if List_1[j]>=0 :
   print (List_1[j])
   j +=1


List_2 = []
for i in range (5):
    num = int(input("Enter the numbers in list 2 ="))
    List_2.append(num)
    i+=1

print(List_2)

print("The positive numbers are-")
for j in range(5):
  if List_2[j]>=0 :
   print (List_2[j])
   j +=1
