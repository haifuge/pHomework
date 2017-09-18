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
    rou=0.5
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
                # calculate alloc
                s=stacks[0]
                if p==0:
                    alc=remain*0.1+remain*rou*(s.increase()+n)/totalIncrease*0.9+remain*(1-rou)*(s.used+n)/totalUsed*0.9
                else:
                    alc=remain*0.1+remain*rou*s.increase()/totalIncrease*0.9+remain*(1-rou)*s.used/totalUsed*0.9
                delta=alc-int(alc)
                if p==0:
                    nextPosition=int(alc)+s.Top+1+n
                else:
                    nextPosition=int(alc)+s.Top+1
                for i in range(1, len(stacks)-1):
                    s=stacks[i]
                    s.NewBase=nextPosition
                    if p==i:
                        alc=remain*0.1+remain*rou*(s.increase()+n)/totalIncrease*0.9+remain*(1-rou)*(s.used+n)/totalUsed*0.9
                    else:
                        alc=remain*0.1+remain*rou*s.increase()/totalIncrease*0.9+remain*(1-rou)*s.used/totalUsed*0.9
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
                        for j in range(s.used-1, -1, -1):
                            mainStack[s.NewBase+j]=mainStack[s.Base+j]
                            mainStack[s.Base+j] = '*'
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
            print(mainStack)
            for s in stacks:
                print('base: '+str(s.Base)+', top: '+str(s.Top))

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
        inputs=inputs.strip().split(' ')
        if i%2==0:
            s=Stack(base, len(inputs))
            for j in range(len(inputs)):
                p=j+s.Base
                mainStack[p]=inputs[j]
            stacks.append(s)
        else:
            base=base+volume-1
            s=MStack(base, len(inputs))
            for j in range(len(inputs)):
                p=s.Base-j
                mainStack[p]=inputs[j]
            stacks.append(s)
    base=(n-1)*volume
    inputs=input('Initialize '+ str(n-1)+ ' stack: ')
    inputs=inputs.strip().split(' ')
    if (n-1)%2==0:
        s=Stack(base, len(inputs))
        for j in range(len(inputs)):
                p=j+s.Base
                mainStack[p]=inputs[j]
        stacks.append(s)
    else:
        s=MStack(len(mainStack)-1, len(inputs))
        for j in range(len(inputs)):
            p=s.Base-j
            mainStack[p]=inputs[j]
        stacks.append(s)

    print(mainStack)
    for s in stacks:
        print('base: '+str(s.Base)+', top: '+str(s.Top))
    ModifiedGarwick(stacks, mainStack)

def ModifiedGarwick(stacks, mainStack):
    rou=0.5
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
            inserted=0
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
                    inserted=1
            else:
                nexts=stacks[p-1].Top
                if s.Top-n>nexts:
                    for i in range(n):
                        s.Top=s.Top-1
                        mainStack[s.Top]=c
                    s.used=s.used+n
                    inserted=1
            # overflow
            if inserted==0:
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
                if p==0:
                    alc=remain*0.1+remain*rou*(s.increase()+n)/totalIncrease*0.9+remain*(1-rou)*(s.used+n)/totalUsed*0.9
                else:
                    alc=remain*0.1+remain*rou*s.increase()/totalIncrease*0.9+remain*(1-rou)*s.used/totalUsed*0.9
                delta=alc-int(alc)
                if p==0:
                    nextPosition=int(alc)+s.Top+1+n
                else:
                    nextPosition=int(alc)+s.Top+1
                for i in range(1, len(stacks)-1):
                    s=stacks[i]
                    if p==i:
                        alc=remain*0.1+remain*rou*(s.increase()+n)/totalIncrease*0.9+remain*(1-rou)*(s.used+n)/totalUsed*0.9
                    else:
                        alc=remain*0.1+remain*rou*s.increase()/totalIncrease*0.9+remain*(1-rou)*s.used/totalUsed*0.9
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
                        for j in range(s.used-1, -1, -1):
                            mainStack[s.NewBase+j]=mainStack[s.Base+j]
                            mainStack[s.Base+j] = '*'
                        s.Base=s.NewBase
                        s.Top=s.Base+s.used-1
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
                                s.Base=s.NewBase
                                s.Top=s.Base+s.used-1
                            else:
                                for l in range(s.used):
                                    mainStack[s.NewBase-l]=mainStack[s.Base-l]
                                    mainStack[s.Base-l]='*'
                                s.Base=s.NewBase
                                s.Top=s.Base-s.used+1
                        i=k
                    i=i+1
                s=stacks[p]
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
            print(mainStack)
            for s in stacks:
                print('base: '+str(s.Base)+', top: '+str(s.Top))