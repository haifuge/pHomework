
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
    
def modifiedRobson(t):
    pass

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
            print(p.info)
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
        print(p.info)
        if predp.info!='-1':
            if predp!=None:
                print('predp: '+predp.info, end=', ')
            if top!=None:
                print('top: '+top.info, end=', ')
            if stack!=None:
                print('stack: '+stack.info, end=', ')
                if stack.rt!=None:
                    print('rt of stack: '+stack.rt.info, end=', ')
                if stack.lt!=None:
                    print('lt of stack: '+stack.lt.info, end=', ')
                    if stack.lt.rt!=None:
                        print('rt of lt of stack: '+stack.lt.rt.info, end=', ')
            print()
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
            if stack==None:
                stack=p
            elif stack.rt==None:
                temp=stack
                stack=p
                stack.lt=temp.lt
                temp.lt=None
            elif stack.rt!=None:
                temp=stack
                stack=p
                stack.lt=temp
            while predp.rt==None or predp.lt==None or predp==top:
                # track back from right child
                if predp==top:
                    top=None
                    if stack!=None and stack.rt!=None:
                        top=stack.rt
                        stack.rt=None
                    # right leaf node
                    if p.lt==None and p.rt==None:
                        temp=stack
                        stack=p
                        stack.rt=temp.rt
                        temp.rt=None
                        if temp.lt!=None:
                            stack.lt=temp.lt
                            temp.lt=None
                    temp=predp.lt
                    predp.lt=predp.rt
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
                    return
            # find predp has both left child and right child
            # since top is None, predp must be tracked back from left child
            if top!=None:
                stack.rt=top
                #avail=top
                #stack.rt=avail
                #avail=None
            top=predp
            p=predp.rt


def main():
    t=create()
    #preorderTraversal(t)
    robsonTraversal(t)

if __name__=='__main__':
    main()

