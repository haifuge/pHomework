import numpy as np

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

def strahlerNumer(L, R, k):
    if L[k]==0 and R[k]==0:
        return 1
    else:
        l=0
        r=0
        if L[k]!=0:
            l=strahlerNumer(L, R, L[k])
        if R[k]!=0:
            r=strahlerNumer(L, R, R[k])
        if l==r:
            return l+1
        else:
            return max(l, r)


def prunningNumber(L, R, k):
    pass


def main():
    n=input('Enter a number:')
    n=int(n)
    c=int(np.floor(np.log2(n))+1)
    st=np.zeros((n-1)*c, dtype=np.int).reshape((n-1),c)
    pt=np.zeros((n-1)*c, dtype=np.int).reshape((n-1),c)
    for i in range(2, n+1):
        L, R = generateTree(i)
        sn=strahlerNumer(L, R, 1)
        st[i-2][sn-1]=st[i-2][sn-1]+1
        #pn=prunningNumber(L, R)
        #pt[i-2][sn-1]=pt[i-2][sn-1]+1
        n=nextTree(L, R)
        while n!=False:
            L=n[0]
            R=n[1]
            sn=strahlerNumer(L, R, 1)
            st[i-2][sn-1]=st[i-2][sn-1]+1
            #pn=prunningNumber(L, R)
            #pt[i-2][sn-1]=pt[i-2][sn-1]+1
            n=nextTree(L, R)
    # print table header
    print('Strahler table of {0}'.format(len(L)-1))
    for i in range(c+1):
        if i==0:
            print('N', end='')
        else:
            print('{:8d}'.format(i), end='')
    print()
    # print strahler table
    for i in range(len(L)-2):
        for j in range(c+1):
            if j==0:
                print(i+2, end='')
            else:
                print('{:8d}'.format(st[i][j-1]), end='')
        print()
    # print prunning table
    print('Prunning table of {0}'.format(len(L)-1))
    #for i in range(c+1):
    #    if i==0:
        #    print('N', end='')
        #else:
        #    print('{:8d}'.format(i), end='')

    #for i in range(n-1):
    #    for j in range(c+1):
    #        if j==0:
            #    print(i+2, end='')
            #else:
            #    print('{:8d}'.format(st[i][j-1]), end='')

if __name__=='__main__':
    main()
    print()