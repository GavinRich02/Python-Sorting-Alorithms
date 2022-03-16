import random

comparisons=0

def bubblesort(list):
    index=0
    compareindex=1
    changes=0
    global comparisons

    for i in range(len(list)):
        while compareindex<=len(list)-1:
            if list[index]>list[compareindex]:
                tempval=list[compareindex]
                list[compareindex]=list[index]
                list[index]=tempval
                changes+=1
            index+=1
            compareindex+=1
            comparisons+=1
        index=0
        compareindex=1
        if changes==0:
            break
        else:
            changes=0
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

print(bubblesort(list))

print("\nLength: "+str(len(list))+" Comparisons: "+str(comparisons)+" Ratio: "+str(float(comparisons)/len(list))+"\n")