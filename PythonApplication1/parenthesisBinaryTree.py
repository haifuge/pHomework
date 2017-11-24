class Node:
    lt=None
    rt=None
    info=0
    def __init__(self, _info):
        self.info=_info

def generateMinParenthesisBinaryTree(n):
    i=1
    t=None
    p=None
    while n>0:
        node = Node(i)
        if t==None:
            t=node
            p=t
        else:
            p.rt = node
            p = node
        n-=1
    return t

def findNextLexicoOrder(lo):
    y=0
    x=0
    i=-1
    while lo[i]==')':
        i-=1
    y=abs(i)
    while lo[i]=='(':
        i-=1
        x+=1
        if abs(i)==len(lo):
            return None
    x-=1
    k=y-x
    lo[i]='('
    i+=1
    for j in range(k):
        lo[i+j]=')'
    i=i+k
    while i<-1:
        lo[i]='('
        lo[i+1]=')'
        i+=2
    return ''.join(lo)

def generateTreeByLexioOrder(lo):
    if len(lo)==0 or lo[0]!='(':
        return None
    s=[]
    k=1
    t=None
    child=0 # 0 no visit, 1 left child visit
    for i in range(len(lo)):
        if lo[i]=='(':
            node=Node(k)
            s.append(node)
            k+=1
            p=node
            if t==None:
                t=p
                q=p
            else:
                if child==0:
                    q.lt=p
                elif child==1:
                    q.rt=p
                q=p
            child=0
        elif lo[i]==')':
            if child==0:
                child=1
            elif child==1:
                while True:
                    if len(s)==0:
                        break
                    q=s.pop()
                    if len(s)>0:
                        rtptr=s[-1].rt
                    else:
                        rtptr=None
                    if len(s)==0 or q!=rtptr:
                        break
                if len(s)>0:
                    q=s.pop()
    return t

def printLR(t, n):
    L=[0]*n
    R=[0]*n
    s=[]
    p=t
    while p!=None or len(s)>0:
        if p!=None:
            if p.lt!=None:
                L[p.info-1]=p.lt.info
            else:
                L[p.info-1]=0
            if p.rt!=None:
                R[p.info-1]=p.rt.info
            else:
                R[p.info-1]=0
            s.append(p)

            if p.lt!=None:
                p=p.lt
            else:
                p=p.rt
        else:
            while True:
                q=s.pop()
                if len(s)>0:
                    rtptr=s[-1].rt
                else:
                    rtptr=None
                if len(s)==0 or q!=rtptr:
                    break
            p=rtptr

    for i in range(n):
        print('L['+str(i+1)+'] = '+str(L[i])+', R['+str(i+1)+'] = '+str(R[i]))

def main():
    n=input('Enter n node:')
    n=int(n)
    lo=''
    for i in range(n):
        lo+='()'
    #lo='()(())'
    k=1
    print(lo)
    t=generateTreeByLexioOrder(lo)
    print('the '+str(k)+': ')
    printLR(t, n)

    while lo!=None:
        lo=findNextLexicoOrder(list(lo))
        if lo!=None:
            k+=1
            print(lo)
            t=generateTreeByLexioOrder(lo)
            print('the '+str(k)+': ')
            printLR(t, n)
    print('total '+str(k)+' strs')


def generateTree(n):
    L=[0]*(n+1)
    R=[0]*(n+1)
    for i in range(1, n):
        R[i]=i+1
    return L, R

def nextTree(L, R):
    rightMost=0
    parent=0
    for i in range(1, len(R)):
        if R[i]!=0 and R[R[i]]==0:
            if rightMost<R[i]:
                rightMost=R[i]
                parent=i

    if parent==0:
        return False
    i=parent
    if L[i]==0:
        L[i]=R[i]
        temp=R[i]
        R[i]=0
        if L[temp]!=0:
            j=1
            while R[j]!=0:
                j=R[j]
            R[j]=L[temp]
            L[temp]=0
            temp=R[j]
            while L[temp]!=0:
                R[temp]=L[temp]
                L[temp]=0
                temp=R[temp]
    else:
        temp=L[i]
        while R[temp]!=0:
            temp=R[temp]
        R[temp]=R[i]
        temp=R[i]
        R[i]=0
        if L[temp]!=0:
            j=1
            while R[j]!=0:
                j=R[j]
            R[j]=L[temp]
            L[temp]=0
            temp=R[j]
            while L[temp]!=0:
                R[temp]=L[temp]
                L[temp]=0
                temp=R[temp]
    return [L, R]
if __name__=='__main__':
    # main()
    #lo1 = '()()()()'
    #while lo1!=None:
    #    lo1=findNextLexicoOrder(list(lo1))
    #    if lo1!=None:
    #        print(lo1)
    n=input('Enter a number:')
    L, R = generateTree(int(n))
    print(L)
    print(R)
    print('-----------------')
    n=nextTree(L, R)
    count=1
    while n!=False:
        L=n[0]
        R=n[1]
        print(L)
        print(R)
        print('-----------------')
        n=nextTree(L, R)
        count+=1
    print(count)

