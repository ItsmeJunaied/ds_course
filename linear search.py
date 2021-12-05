size=int(input("Enter number: "))
list=[]
for i in range(size):
    elem=int(input("Enter elements: "))
    list.append(elem)
print(list)

targetval=int(input("choose your target: "))
condition=False
for i in list:
    if i==targetval:
        print("Target value index is: ",list.index(i))
        condition = True
        break
if condition== False:
    print("Element not found")
