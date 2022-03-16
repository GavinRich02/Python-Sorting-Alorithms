import random

comparisons=0

def sort(list):
    global comparisons
    index=0
    compareindex=1
    tempval=0
    while True:
        if index<len(list)-1 and compareindex<len(list):
            print(list[index],list[compareindex])
            if list[index]>list[compareindex]:
                tempval=list[compareindex]
                list[compareindex]=list[index]
                list[index]=tempval
                compareindex+=1
            else:
                compareindex+=1
            comparisons+=1
        elif compareindex==len(list):
            index+=1
            compareindex=index+1
        else:
            break
    return list


list=[]

for i in range(random.randint(2,100)):
    while True:
        num=random.randint(0,100)
        if num in list:
            continue
        else:
            list.append(num)
            break

list=sort(list)
print(list)

print("\nLength: "+str(len(list))+" Comparisons: "+str(comparisons)+" Ratio: "+str(float(comparisons)/len(list))+"\n")