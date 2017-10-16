
class node:
    info=''
    lt=None
    rt=None
    def __init__(self, _info):
        self.info=_info

def create():
    f=open('robsontreedata')
    lines=f.readlines()
    k=0
    if lines[0][0]=='0':
        return None
    else:
        root=node(str(k))
        s=[]
        k=k+1
        p=root
        l=1
        while (p!=None or len(s)>0) and l<len(lines):
            ns=lines[l][:-1].split(' ')
            l=l+1
            if ns[1]=='1':
                nd=node(str(k))
                p.rt=nd
                s.insert(0, nd)
            else:
                p.rt=None
            if ns[0]=='1':
                nd=node(str(k))
                p.lt=nd
                s.insert(0, nd)
            else:
                p.lt=None
            if len(s)>0:
                p=s.pop(0)
                p.info=str(k)
                k=k+1
            else:
                break
    return root
    
def preorderCreate():
    f=open('robsontreedata')
    lines=f.readlines()
    if lines[0][0]=='0':
        return None
    else:
        k=0
        root=node(str(k))
        l=0
        s=[]
        p=root
        while p!=None or len(s)>0:
            if p!=None:
                p.info=str(k)
                k+=1
                s.append(p)
                l+=1
                if(lines[l][0]=='1'):
                    p.lt=node('')
                if lines[l][2]=='1':
                    p.rt=node('')
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
    return root

def preTraverseTreeRecuresion(t):
    if t==None:
        return
    else:
        print(t.info)
        if t.lt!=None:
            preTraverseTreeRecuresion(t.lt)
        if t.rt!=None:
            preTraverseTreeRecuresion(t.rt)

def preorderTraversal(t):
    p=t
    s=[]
    while p!=None or len(s)>0:
        if p!=None:
            print('current point: '+p.info, end =', ')
            if p.lt!=None:
                print('left child: '+p.lt.info, end='. ')
            else:
                print('left child: None', end='. ')
            if p.rt!=None:
                print('right child: '+p.rt.info, end='. ')
            else:
                print('right child: None', end='. ')
            print()
            s.insert(0, p)
            if p.lt!=None:
                p=p.lt
            else:
                p=p.rt
        else:
            while True:
                q=s.pop(0)
                if len(s)>0:
                    rtptr=s[0].rt
                else:
                    rtptr=None
                if len(s)>0 and q is rtptr:
                    pass
                else:
                    break
            p=rtptr

def robsonTraversal(t):
    top = None
    stack = None
    predp=node('-1')
    avail=None
    p=t
    while p!=None:
        printPointInfo(p, stack, predp, top)
        if p.lt!=None:
            temp=p.lt
            p.lt=predp
            predp=p
            p=temp
        elif p.rt!=None:
            temp=p.rt
            p.rt=predp
            predp=p
            p=temp
        else:
            avail=p
            while predp.rt==None or predp.lt==None or predp==top:
                # track back from right child
                if predp==top:
                    top=None
                    if stack!=None:
                        top=stack.rt
                        stack.rt=None
                        temp=stack
                        stack=stack.lt
                        temp.lt=None
                    temp=predp.rt
                    predp.rt=p
                    p=predp
                    predp=temp                    
                # track back by left child
                elif predp.lt!=None:
                    temp=predp.lt
                    predp.lt=p
                    p=predp
                    predp=temp
                elif predp.rt!=None:
                    # track back by right child
                    temp=predp.rt
                    predp.rt=p
                    p=predp
                    predp=temp
                else:
                    # track back to node(-1),  
                    preorderTraversal(t)
                    return
            # find predp has both left child and right child
            # since top is None, predp must be tracked back from left child
            if top!=None:
                avail.rt=top
                avail.lt=stack
                stack=avail
            top=predp
            temp=predp.rt
            predp=top.lt
            top.lt=p
            top.rt=predp
            predp=top
            p=temp
            

def printPointInfo(p, stack, predp, top):
    print('current node: '+p.info, end='. ')
    print('predp node: '+predp.info, end='. ')
    if top!=None:
        print('top: '+top.info, end='. ')
    else:
        print('top: None', end='. ')
    if p.lt!=None:
        print('left child: '+p.lt.info, end='. ')
    else:
        print('left child: None', end='. ')
    if p.rt!=None:
        print('right child: '+p.rt.info, end='. ')
    else:
        print('right child: None', end='. ')
    s=stack
    while s!=None:
        print('stack: '+s.info+', rt of stack: '+s.rt.info, end=', ')
        s=s.lt
    print()
    s=stack
    p=predp
    q=top
    print('path back: ', end='');
    while p.info!='-1':
        print(p.info, end='->')
        if p==q:
            p=p.rt
            if s!=None:
                q=s.rt
                s=s.lt
        else:
            if p.lt!=None:
                p=p.lt
            elif p.rt!=None:
                p=p.rt

    print()
    


def main():
    #t=create()
    t=preorderCreate()
    preorderTraversal(t)
    #preorderTraversal(t)
    robsonTraversal(t)
    preorderTraversal(t)

if __name__=='__main__':
    main()

