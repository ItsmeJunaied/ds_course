def shiftLeft(source,k):
    for i in range(0,len(source)):
        if(i-k)<=0:
            source[i-k]=source[i]

    for i in range(len(source)-k,len(source)):
            source[i]=0
            #return
source=[10,20,30,40,50,60]
k=3
shiftLeft(source,k)
print(source)

#%%___________________________________________

def shiftRight(source1,k):
    for i in range(0,len(source1)):
        if(i-k)>=k:
            source1[i]=0

    for i in range(0,len(source1)-k):
            source1[i]=0

source1=[10,20,30,40,50,60]
k=3
shiftRight(source1,k)
print(source1)
'''_________________________________________'''
def rotateLeft(source2,k):
    i=0
    list=[]
    while i>k:
        list.append(source2[])
        i+=1
    list.append(source2[])
    i+=1



source2 = [10, 20, 30, 40, 50, 60]
k = 3
rotateLeft(source2,k)
print(source2)

def resize(circ,start,size):

    resizedCirc=[0]*(len(circ)+2)

    index_circ=start

    index_resizedCirc=start

    i=0

    while(i<size):

        resizedCirc[index_resizedCirc]=circ[index_circ]

        index_circ=(index_circ+1)%len(circ)

        index_resizedCirc=(index_resizedCirc+1)%len(resizedCirc)

        i=i+1

    return resizedCirc



circ=[20,30,40,50,10] #creating a circular array with start 4 and size 5

circ=resize(circ,4,5)

print(circ)

