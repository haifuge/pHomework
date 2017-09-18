# bag contains object with 0 predecessor
bag=[]
# set of initial objects
s=[]
# output array
output=[]
# count of predecessor of object i
ncount=[]
# successor of object j
successors=[]
total=0
def topoSort(n):
    global output
    global bag
    global s
    global ncount
    global successors
    global total
    output=[]
    bag=[]
    s=[]
    ncount=[]
    successors=[]
    total=0
    for i in range(n):
        s.append(i+1)
        ncount.append(0)
        successors.append([])
    ncount.append(0)
    successors.append([])

    pair=input('Enter pairs (# #, 0 0 to quit): ')
    while pair != '0 0':
        p=pair.split(' ')
        ncount[int(p[1])]=ncount[int(p[1])]+1
        successors[int(p[0])].insert(0, int(p[1]))
        pair=input('Enter pairs (# #, 0 0 to quit): ')

    # initialize bag    
    for i in range(1, n+1):
        if ncount[i]==0:
            s.remove(i)
            bag.append(i)
    topsorts()
    print('Total toposorts is {}.'.format(total))

def topsorts():
    global total
    if len(bag)>0:
        k=0
        while len(bag)>k:
            # output a object from bag
            t=bag[k]
            bag.remove(t)
            # input into output array
            output.append(t)
            for i in range(len(successors[t])):
                ncount[successors[t][i]]=ncount[successors[t][i]]-1
                if ncount[successors[t][i]]==0:
                    s.remove(successors[t][i])
                    bag.append(successors[t][i])
            topsorts()
            output.remove(t)
            # reverse
            for i in range(len(successors[t])):
                ncount[successors[t][i]]=ncount[successors[t][i]]+1
                if ncount[successors[t][i]]==1:
                    s.insert(successors[t][i]-1, successors[t][i])
                    bag.remove(successors[t][i])
            bag.insert(k,t)
            k=k+1
    else:
        total=total+1
        print(output)

n=input('Enter n: ')
n=int(n)
while n>0:
    topoSort(n)
    n=input('Enter n: ')
    n=int(n)
