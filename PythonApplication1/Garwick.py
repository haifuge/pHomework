import numpy as np
import copy
class Stack:
    Base=0
    Top=0
    OldTop=0
    NewBase=0
    used=0
    def __init__(self, base, n):
        self.Base=base
        self.OldTop=n+base-1
        self.Top=self.OldTop
        self.used=n
    def increase(self):
        return self.Top-self.OldTop
class MStack:
    Base=0
    Top=0
    OldTop=0
    NewBase=0
    used=0
    def __init__(self, base, n):
        self.Base=base
        self.OldTop=base-n+1
        self.Top=self.OldTop
        self.used=n
    def increase(self):
        return self.OldTop-self.Top

def testGarwick():
    capacity=input('Input capacity: ')
    capacity=int(capacity)
    #mainStack=[' ' for n in range(capacity)]
    mainStack=['*']*capacity
    print('main stack is '+str(mainStack))
    n=input('Input number of stack: ')
    n=int(n)
    volume=round(capacity/n)
    stacks=[]
    for i in range(n-1):
        base=i*volume
        inputs=input('Initialize '+ str(i)+ ' stack: ')
        ssize=0
        if inputs=='':
            ssize=0
        else:
            inputs=inputs.strip().split(' ')
            ssize=len(inputs)
        s=Stack(base, ssize)
        for j in range(len(inputs)):
            p=j+s.Base
            mainStack[p]=inputs[j]
        stacks.append(s)
    base=(n-1)*volume
    inputs=input('Initialize '+ str(n-1)+ ' stack: ')
    ssize=0
    if inputs=='':
        ssize=0
    else:
        inputs=inputs.strip().split(' ')
        ssize=len(inputs)
    s=Stack(base, ssize)
    for j in range(len(inputs)):
            p=j+s.Base
            mainStack[p]=inputs[j]
    stacks.append(s)

    print(mainStack)
    for s in stacks:
        print('base: '+str(s.Base)+', top: '+str(s.Top))
    Garwick(stacks, mainStack)


def Garwick(stacks, mainStack):
    overflows=0
    moves=0
    rou=input('Input sigma： ')
    rou=float(rou)
    sn=len(stacks)
    while True:
        n=input('input stack number and a letter: ')
        if n[0]=='q':
            break;
        n=n.split(' ')
        c=n[2]
        p=int(n[0])
        n=int(n[1])
        if p>=len(stacks) or p<0:
            print('input wrong stack number.')
        else:
            s=stacks[p]
            nexts=0
            if p==len(stacks)-1:
                nexts=len(mainStack)
            else:
                nexts=stacks[p+1].Base
            # top add n for later calculation
            if s.Top+n<nexts:
                for i in range(1, n+1):
                    s.Top=s.Top+1
                    mainStack[s.Top]=c
                s.used=s.used+n
            else:
                overflows=overflows+1
                totalIncrease=0
                totalUsed=0
                remain=0
                # calculate total used, increase
                for s in stacks:
                    totalIncrease=totalIncrease+s.increase()
                    totalUsed=totalUsed+s.used
                totalIncrease=totalIncrease+n
                totalUsed=totalUsed+n
                remain=len(mainStack)-totalUsed
                if remain<0:
                    print('Main stack overflows. Program quit.')
                    break;
                delta=0
                nextPosition=0
                for i in range(0, len(stacks)-1):
                    s=stacks[i]
                    s.NewBase=nextPosition
                    if p==i:
                        alc=remain*0.1/sn+remain*rou*(s.increase()+n)/totalIncrease*0.9+remain*(1-rou)*(s.used+n)/totalUsed*0.9
                    else:
                        alc=remain*0.1/sn+remain*rou*s.increase()/totalIncrease*0.9+remain*(1-rou)*s.used/totalUsed*0.9
                    print('alc: ',alc)
                    alc=alc+delta
                    delta=alc-int(alc)
                    print('delta: ', int(alc))
                    if p==i:
                        nextPosition=nextPosition+int(alc)+s.used+n
                    else:
                        nextPosition=nextPosition+int(alc)+s.used
                stacks[-1].NewBase=nextPosition

                # movev stacks from second stack
                i=1
                while i<len(stacks):
                    s=stacks[i]
                    # move left
                    if s.Base > s.NewBase:
                        for j in range(s.used):#(s.used-1, -1, -1):
                            mainStack[s.NewBase+j]=mainStack[s.Base+j]
                            mainStack[s.Base+j] = '*'
                            moves=moves+1
                        s.Base=s.NewBase
                        s.Top=s.Base+s.used-1
                    elif s.Base<s.NewBase:
                        # move right
                        # find k that move left
                        k=-1
                        if i+1==len(stacks):
                            k=i
                        else:
                            for j in range(i, len(stacks)-1):
                                if stacks[j].Base>stacks[j].NewBase:
                                    k=j
                                    break
                        if k==-1:
                            k=len(stacks)-1
                        # move stacks[i:k]
                        for j in range(k, i-1, -1):
                            s=stacks[j]
                            for l in range(s.used-1, -1, -1):
                                mainStack[s.NewBase+l]=mainStack[s.Base+l]
                                mainStack[s.Base+l]='*'
                                moves=moves+1
                            s.Base=s.NewBase
                            s.Top=s.Base+s.used-1
                        i=k
                    i=i+1
                s=stacks[p]
                for i in range(n):
                    s.Top=s.Top+1
                    mainStack[s.Top]=c
                s.OldTop=s.Top
                s.used=s.used+n
                for s in stacks:
                    s.OldTop=s.Top
            print(mainStack)
            for s in stacks:
                print('base: '+str(s.Base)+', top: '+str(s.Top))
            print('overflow: '+str(overflows)+', move:'+str(moves))

def testModifiedGarwick():
    capacity=input('Input capacity: ')
    capacity=int(capacity)
    #mainStack=[' ' for n in range(capacity)]
    mainStack=['*']*capacity
    print('main stack is '+str(mainStack))
    n=input('Input number of stack: ')
    n=int(n)
    volume=round(capacity/n)
    stacks=[]
    for i in range(n-1):
        base=i*volume
        inputs=input('Initialize '+ str(i)+ ' stack: ')
        ssize=0
        if inputs=='':
            ssize=0
        else:
            inputs=inputs.strip().split(' ')
            ssize=len(inputs)
        if i%2==0:
            s=Stack(base, ssize)
            for j in range(ssize):
                p=j+s.Base
                mainStack[p]=inputs[j]
            stacks.append(s)
        else:
            base=base+volume-1
            s=MStack(base, ssize)
            for j in range(ssize):
                p=s.Base-j
                mainStack[p]=inputs[j]
            stacks.append(s)
    base=(n-1)*volume
    inputs=input('Initialize '+ str(n-1)+ ' stack: ')
    ssize=0
    if inputs=='':
        ssize=0
    else:
        inputs=inputs.strip().split(' ')
        ssize=len(inputs)
    if (n-1)%2==0:
        s=Stack(base, ssize)
        for j in range(ssize):
                p=j+s.Base
                mainStack[p]=inputs[j]
        stacks.append(s)
    else:
        s=MStack(len(mainStack)-1, ssize)
        for j in range(ssize):
            p=s.Base-j
            mainStack[p]=inputs[j]
        stacks.append(s)

    print(mainStack)
    for s in stacks:
        print('base: '+str(s.Base)+', top: '+str(s.Top))
    ModifiedGarwick(stacks, mainStack)

def ModifiedGarwick(stacks, mainStack):
    overflows=0
    moves=0
    rou=input('Input sigma： ')
    rou=float(rou)
    sn=len(stacks)
    while True:
        n=input('input stack number and a letter: ')
        if n[0]=='q':
            break;
        n=n.split(' ')
        c=n[2]
        p=int(n[0])
        n=int(n[1])
        if p>=len(stacks) or p<0:
            print('input wrong stack number.')
        else:
            s=stacks[p]
            nexts=0
            inserted=False
            if p%2==0:
                if p==len(stacks)-1:
                    nexts=len(mainStack)
                else:
                    nexts=stacks[p+1].Top
                if s.Top+n<nexts:
                    for i in range(n):
                        s.Top=s.Top+1
                        mainStack[s.Top]=c
                    s.used=s.used+n
                    inserted=True
            else:
                nexts=stacks[p-1].Top
                if s.Top-n>nexts:
                    for i in range(n):
                        s.Top=s.Top-1
                        mainStack[s.Top]=c
                    s.used=s.used+n
                    inserted=True
            # overflow
            if not inserted:
                overflows=overflows+1
                totalIncrease=0
                totalUsed=0
                remain=0
                # calculate total used, increase
                for s in stacks:
                    totalIncrease=totalIncrease+s.increase()
                    totalUsed=totalUsed+s.used
                totalIncrease=totalIncrease+n
                totalUsed=totalUsed+n
                remain=len(mainStack)-totalUsed
                if remain<0:
                    print('Main stack overflows. Program quit.')
                    break;
                delta=0
                # calculate alloc[0]
                s=stacks[0]
                nextPosition=0
                for i in range(0, len(stacks)-1):
                    s=stacks[i]
                    if p==i:
                        alc=remain*0.1/sn+remain*rou*(s.increase()+n)/totalIncrease*0.9+remain*(1-rou)*(s.used+n)/totalUsed*0.9
                    else:
                        alc=remain*0.1/sn+remain*rou*s.increase()/totalIncrease*0.9+remain*(1-rou)*s.used/totalUsed*0.9
                    print('alc: ',alc)
                    alc=alc+delta
                    delta=alc-int(alc)
                    print('delta: ', int(alc))
                    if i%2==0:
                        s.NewBase=nextPosition
                        nextPosition=nextPosition+int(alc)+s.used
                        if p==i:
                            nextPosition=nextPosition+n
                    else:
                        s.NewBase=nextPosition+int(alc)+s.used-1
                        if p==i:
                            s.NewBase=s.NewBase+n
                        nextPosition=s.NewBase+1
                        s.top=s.NewBase-s.used+1
                if len(stacks)%2==1:
                    stacks[-1].NewBase=nextPosition
                else:
                    stacks[-1].NewBase=len(mainStack)-1


                # movev stacks
                i=1
                while i<len(stacks):
                    s=stacks[i]
                    # move left
                    if s.Base > s.NewBase:
                        if i%2==0:
                            for j in range(s.used):
                                mainStack[s.NewBase+j]=mainStack[s.Base+j]
                                mainStack[s.Base+j] = '*'
                                moves=moves+1
                            s.Base=s.NewBase
                            s.Top=s.Base+s.used-1
                        else:
                            for j in range(s.used-1, -1, -1):
                                mainStack[s.NewBase-j]=mainStack[s.Base-j]
                                mainStack[s.Base-j] = '*'
                                moves=moves+1
                            s.Base=s.NewBase
                            s.Top=s.Base-s.used+1
                    elif s.Base<s.NewBase:
                        # move right
                        # find k that move left
                        k=-1
                        if i+1==len(stacks):
                            k=i
                        else:
                            # do not care odd or even, as long as newbase < base, move left
                            for j in range(i, len(stacks)-1):
                                if stacks[j].Base>stacks[j].NewBase:
                                    k=j
                                    break
                        if k==-1:
                            k=len(stacks)-1
                            # if len(stacks) is even, last stack doesn't need to move, so we need move from the last second.
                            if len(stacks)%2==0:
                                k=k-1
                        # move stacks[i:k]
                        for j in range(k, i-1, -1):
                            s=stacks[j]
                            if j%2==0:
                                for l in range(s.used-1, -1, -1):
                                    mainStack[s.NewBase+l]=mainStack[s.Base+l]
                                    mainStack[s.Base+l]='*'
                                    moves=moves+1
                                s.Base=s.NewBase
                                s.Top=s.Base+s.used-1
                            else:
                                for l in range(s.used):
                                    mainStack[s.NewBase-l]=mainStack[s.Base-l]
                                    mainStack[s.Base-l]='*'
                                    moves=moves+1
                                s.Base=s.NewBase
                                s.Top=s.Base-s.used+1
                        i=k
                    i=i+1
                s=stacks[p]
                # add new c to stack
                if p%2==0:
                    for i in range(n):
                        s.Top=s.Top+1
                        mainStack[s.Top]=c
                else:
                    for i in range(n):
                        s.Top=s.Top-1
                        mainStack[s.Top]=c
                s.OldTop=s.Top
                s.used=s.used+n
                for s in stacks:
                    s.OldTop=s.Top
            print(mainStack)
            for s in stacks:
                print('base: '+str(s.Base)+', top: '+str(s.Top))
            print('overflow: '+str(overflows)+', move:'+str(moves))
    
def Garwick1000(stacks, mainStack, spurts, rou):
    overflows=0
    moves=0
    sn=len(stacks)
    isfull=False
    m=0
    randS=stackFrequency(1000)
    while not isfull:
        c='1'
        #p=np.random.randint(0, sn)
        if m>=1000:
            break

        p=randS[m]
        m=m+1
        n=1
        for spu in range(spurts):
            s=stacks[p]
            nexts=0
            if p==len(stacks)-1:
                nexts=len(mainStack)
            else:
                nexts=stacks[p+1].Base
            # top add n for later calculation
            if s.Top+n<nexts:
                for i in range(1, n+1):
                    s.Top=s.Top+1
                    mainStack[s.Top]=c
                s.used=s.used+n
            else:
                overflows=overflows+1
                totalIncrease=0
                totalUsed=0
                remain=0
                # calculate total used, increase
                for s in stacks:
                    totalIncrease=totalIncrease+s.increase()
                    totalUsed=totalUsed+s.used
                totalIncrease=totalIncrease+n
                totalUsed=totalUsed+n
                remain=len(mainStack)-totalUsed
                if remain<0:
                    #print('Main stack is full...')
                    isfull=True
                    break;
                delta=0
                nextPosition=0
                for i in range(0, len(stacks)-1):
                    s=stacks[i]
                    s.NewBase=nextPosition
                    if p==i:
                        alc=remain*0.1/sn+remain*rou*(s.increase()+n)/totalIncrease*0.9+remain*(1-rou)*(s.used+n)/totalUsed*0.9
                    else:
                        alc=remain*0.1/sn+remain*rou*s.increase()/totalIncrease*0.9+remain*(1-rou)*s.used/totalUsed*0.9
                    alc=alc+delta
                    delta=alc-int(alc)
                    if p==i:
                        nextPosition=nextPosition+int(alc)+s.used+n
                    else:
                        nextPosition=nextPosition+int(alc)+s.used
                stacks[-1].NewBase=nextPosition

                # movev stacks
                i=1
                while i<len(stacks):
                    s=stacks[i]
                    # move left
                    if s.Base > s.NewBase:
                        for j in range(s.used):#(s.used-1, -1, -1):
                            mainStack[s.NewBase+j]=mainStack[s.Base+j]
                            mainStack[s.Base+j] = '*'
                            moves=moves+1
                        s.Base=s.NewBase
                        s.Top=s.Base+s.used-1
                    elif s.Base<s.NewBase:
                        # move right
                        # find k that move left
                        k=-1
                        if i+1==len(stacks):
                            k=i
                        else:
                            for j in range(i, len(stacks)-1):
                                if stacks[j].Base>stacks[j].NewBase:
                                    k=j
                                    break
                        if k==-1:
                            k=len(stacks)-1
                        # move stacks[i:k]
                        for j in range(k, i-1, -1):
                            s=stacks[j]
                            for l in range(s.used-1, -1, -1):
                                mainStack[s.NewBase+l]=mainStack[s.Base+l]
                                mainStack[s.Base+l]='*'
                                moves=moves+1
                            s.Base=s.NewBase
                            s.Top=s.Base+s.used-1
                        i=k
                    i=i+1
                s=stacks[p]
                for i in range(n):
                    s.Top=s.Top+1
                    mainStack[s.Top]=c
                s.OldTop=s.Top
                s.used=s.used+n
                for s in stacks:
                    s.OldTop=s.Top
    return overflows, moves

def stackFrequency(arrSize):
    stackP=[2**i for i in range(9, -1, -1)]
    total=sum(stackP)
    for i in range(len(stackP)-1):
        stackP[i+1]=stackP[i]+stackP[i+1]
    rand=[]
    for j in range(arrSize):
        n=np.random.randint(1, total+1)
        for i in range(10):
            if n<=stackP[i]:
                rand.append(i)
                break
    return rand


def testGarwick1000():
    capacity=1000
    #mainStack=[' ' for n in range(capacity)]
    mainStack=['*']*capacity
    n=10
    volume=round(capacity/n)
    stacks=[]
    #for i in range(n):
    #    base=i*volume
    #    s=Stack(base, 0)
    #    stacks.append(s)

    for i in range(n-1):
        base=i*volume
        ssize=0
        if i%2==0:
            s=Stack(base, ssize)
            for j in range(ssize):
                p=j+s.Base
                mainStack[p]=inputs[j]
            stacks.append(s)
        else:
            base=base+volume-1
            s=MStack(base, ssize)
            for j in range(ssize):
                p=s.Base-j
                mainStack[p]=inputs[j]
            stacks.append(s)
    base=(n-1)*volume

    ssize=0
    if (n-1)%2==0:
        s=Stack(base, ssize)
        for j in range(ssize):
            p=j+s.Base
            mainStack[p]=inputs[j]
        stacks.append(s)
    else:
        s=MStack(len(mainStack)-1, ssize)
        for j in range(ssize):
            p=s.Base-j
            mainStack[p]=inputs[j]
        stacks.append(s)

    results=[]
    sigma=[1, 0.5, 0]
    spurts=[1, 20, 50]
    for spu in spurts:
        for s in sigma:
            results=[]
            for i in range(10):
                #overflows, moves = Garwick1000(copy.deepcopy(stacks), copy.deepcopy(mainStack), spu , s)
                overflows, moves = modifiedGarwick1000(copy.deepcopy(stacks), copy.deepcopy(mainStack), spu , s)
                results.append([overflows, moves])
            print(results)
            print('spurt: '+str(spu)+', sigma: '+str(s)+', mean overflow: '+str(np.mean(results, axis=0)))


def modifiedGarwick1000(stacks, mainStack, spurts, rou):
    overflows=0
    moves=0
    sn=len(stacks)
    isfull=False
    m=0
    randS=stackFrequency(1000)
    while not isfull:
        c='1'
        n=1
        #p=np.random.randint(0, sn)
        p=randS[m]
        for spu in range(spurts):
            if m>=1000:
                isfull=True
                break
            m=m+1
            s=stacks[p]
            nexts=0
            inserted=False
            if p%2==0:
                if p==len(stacks)-1:
                    nexts=len(mainStack)
                else:
                    nexts=stacks[p+1].Top
                if s.Top+n<nexts:
                    for i in range(n):
                        s.Top=s.Top+1
                        mainStack[s.Top]=c
                    s.used=s.used+n
                    inserted=True
            else:
                nexts=stacks[p-1].Top
                if s.Top-n>nexts:
                    for i in range(n):
                        s.Top=s.Top-1
                        mainStack[s.Top]=c
                    s.used=s.used+n
                    inserted=True
            # overflow
            if not inserted:
                overflows=overflows+1
                totalIncrease=0
                totalUsed=0
                remain=0
                # calculate total used, increase
                for s in stacks:
                    totalIncrease=totalIncrease+s.increase()
                    totalUsed=totalUsed+s.used
                totalUsed=totalUsed+n
                totalIncrease=totalIncrease+1
                remain=len(mainStack)-totalUsed
                if remain<=0:
                    #print('Main stack is full...')
                    isfull=True
                    break;
                delta=0
                nextPosition=0
                for i in range(0, len(stacks)-1):
                    s=stacks[i]
                    if p==i:
                        alc=remain*0.1/sn+remain*rou*(s.increase()+n)/totalIncrease*0.9+remain*(1-rou)*(s.used+n)/totalUsed*0.9
                    else:
                        alc=remain*0.1/sn+remain*rou*s.increase()/totalIncrease*0.9+remain*(1-rou)*s.used/totalUsed*0.9
                    alc=alc+delta
                    delta=alc-int(alc)
                    if i%2==0:
                        s.NewBase=nextPosition
                        nextPosition=nextPosition+int(alc)+s.used
                        if p==i:
                            nextPosition=nextPosition+n
                    else:
                        s.NewBase=nextPosition+int(alc)+s.used-1
                        if p==i:
                            s.NewBase=s.NewBase+n
                        nextPosition=s.NewBase+1
                        s.top=s.NewBase-s.used+1
                if len(stacks)%2==1:
                    stacks[-1].NewBase=nextPosition
                else:
                    stacks[-1].NewBase=len(mainStack)-1
                # movev stacks
                i=1
                while i<len(stacks):
                    s=stacks[i]
                    # move left
                    if s.Base > s.NewBase:
                        if i%2==0:
                            for j in range(s.used):
                                mainStack[s.NewBase+j]=mainStack[s.Base+j]
                                mainStack[s.Base+j] = '*'
                                moves=moves+1
                            s.Base=s.NewBase
                            s.Top=s.Base+s.used-1
                        else:
                            for j in range(s.used-1, -1, -1):
                                mainStack[s.NewBase-j]=mainStack[s.Base-j]
                                mainStack[s.Base-j] = '*'
                                moves=moves+1
                            s.Base=s.NewBase
                            s.Top=s.Base-s.used+1
                    elif s.Base<s.NewBase:
                        # move right
                        # find k that move left
                        k=-1
                        if i+1==len(stacks):
                            k=i
                        else:
                            # do not care odd or even, as long as newbase < base, move left
                            for j in range(i, len(stacks)-1):
                                if stacks[j].Base>stacks[j].NewBase:
                                    k=j
                                    break
                        if k==-1:
                            k=len(stacks)-1
                            # if len(stacks) is even, last stack doesn't need to move, so we need move from the last second.
                            if len(stacks)%2==0:
                                k=k-1
                        # move stacks[i:k]
                        for j in range(k, i-1, -1):
                            s=stacks[j]
                            if j%2==0:
                                for l in range(s.used-1, -1, -1):
                                    mainStack[s.NewBase+l]=mainStack[s.Base+l]
                                    mainStack[s.Base+l]='*'
                                    moves=moves+1
                                s.Base=s.NewBase
                                s.Top=s.Base+s.used-1
                            else:
                                for l in range(s.used):
                                    mainStack[s.NewBase-l]=mainStack[s.Base-l]
                                    mainStack[s.Base-l]='*'
                                    moves=moves+1
                                s.Base=s.NewBase
                                s.Top=s.Base-s.used+1
                        i=k
                    i=i+1
                s=stacks[p]
                # add new c to stack
                if p%2==0:
                    for i in range(n):
                        s.Top=s.Top+1
                        mainStack[s.Top]=c
                else:
                    for i in range(n):
                        s.Top=s.Top-1
                        mainStack[s.Top]=c
                s.OldTop=s.Top
                s.used=s.used+n
                for s in stacks:
                    s.OldTop=s.Top
    return overflows, moves