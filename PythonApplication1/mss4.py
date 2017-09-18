
def runmss4():
    n=input('enter a number (q to stop): ')
    count=0
    while True:
        ans=[]
        queue=[]
        count=0
        if n=='q':
            print('mss of inputs is 0, start position of is 0, and last position of mss is 0.')
            print('maximum subsequence product is 0.')
            break;
        while n != 'q':
            n=int(n)
            queue.append(n)
            count=count+1
            n=input('enter a number (q to stop): ')
        print(queue)
        mss4(queue, 0, count-1)
        maxproduct=mss3(queue, 0, count-1)
        print('maximum subsequence product is {}.'.format(maxproduct))
        n=input('enter a number (q to stop): ')
    
    

def mss4(a, p1, p2):
    maxsum = sum = 0
    last = first =0
    firsti=0
    i=p1
    while i <= p2:
        sum= sum+a[i]
        if sum> maxsum:
            maxsum=sum
            first=firsti
            last=i
        elif sum < 0:
            sum=0
            firsti=i+1
        i=i+1
    print('mss of inputs is {}, start position of is {}, and last position of mss is {}'.format(maxsum, first, last))


def mss3(a, p1, p2):
    if len(a)==0:
        return 0
    maxproduct=0
    if p1 == p2:
        if a[p1] > 0:
            maxproduct = a[p1]
        else:
            maxproduct=0
    else:
        m=int((p1+p2)/2)
        L=mss3(a, p1, m)
        R=mss3(a, m+1, p2)
        pplt=0
        pnlt=0
        pprt=0
        pnrt=0
        p=1
        for i in range(m, p1-1, -1):
            p=p*a[i]
            if p>0:
                if p>pplt:
                    pplt=p
            else:
                if p < pnlt:
                    pnlt=p
        p=1
        for i in range(m+1, p2+1):
            p=p*a[i]
            if p>0:
                if p>pprt:
                    pprt=p
            else:
                if p < pnrt:
                    pnrt=p
        ppt=0
        if pplt==0 and pprt==0:
            ppt=0
        elif pplt==0:
            ppt=pprt
        elif pprt==0:
            ppt=pplt
        else:
            ppt=pplt*pprt
        pnt=0
        if pnlt!=0 or pnrt!=0:
            pnt=pnlt*pnrt
        maxproduct=max(L, R, ppt, pnt)
    return maxproduct
