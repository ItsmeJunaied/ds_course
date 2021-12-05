def rightShift(source,k):
    temp=[]
    for i in range(k-1,len(source)):
        temp.append(source[i])
    print(temp)
    i=len(source)-1 #pointer at the last index of source
    print(i)
    while(i>=k):

        source[i]=source[i-k]  #shifting elements k places to the right

        i=i-1

    i=0
    j=0
    while(i<k):

        source[i]=temp[j] #setting first k values to 0

        i=i+1
        j=j+1



a=[10,20,30,40,50]

rightShift(a,3)

print(a)
print("__________________________")
def printForward(c,start,size):

    index=start

    i=0

    while(i<size):

        print(c[index])

        index=(index+1)%len(c)

        i=i+1



circularArray=[40,50,0,0,0,0,0,0,10,20,30] #creating a circular array with start 8 and size 5

printForward(circularArray,8,5)
print("__________________________")

def resize(circ,start,size):
    resizeCirc=[]*(len(circ)+2)
    index_circ= start
    index_resizeCirc= start
    i=0
    while(i<size):
        resizeCirc[index_resizeCirc]=circ[index_circ]
        index_circ=(index_circ+1)%(len(circ))
        index_resizeCirc=(index_resizeCirc+1)%len(resizeCirc)
        i+=1
    return resizeCirc



circ = [20, 30, 40, 50, 10]  # creating a circular array with start 4 and size 5

circ = resize(circ, 4, 5)
print(circ)
print("__________________________")