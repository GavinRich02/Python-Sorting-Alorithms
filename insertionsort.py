import random

comparisons=0

def sort(list):
    global comparisons
    index=1
    compareindex=0
    templist=[]

    while True:
        #print(list,index)
        if compareindex<index and compareindex>=0 and len(list)>0:
            tempval=list[index]
            while list[index]<list[compareindex]:
                if compareindex>=0:
                    tempval=list[index]
                    compareindex-=1
                    comparisons+=1
                else:
                    break
            list.pop(index)
            list.insert(compareindex+1,tempval)

            index+=1
            compareindex=index-1
            comparisons+=1
            
            if index>len(list)-1:
                break
        else:
            index+=1
            compareindex=index-1
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