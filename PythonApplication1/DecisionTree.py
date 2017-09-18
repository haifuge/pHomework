import numpy as np
import copy

data=[]
decision = []
attributes = []
attributeValue=[]
HA=0.0
total=0
def readData():
    global data
    f=open('C:\MLData\DecisionTree.txt')
    for line in f.readlines():
        data.append(line.replace('\n','').split(' '))

def initialzeData():
    global data
    global attributes
    global decision
    global attributeValue
    global HA
    global total
    total=len(data)-1
    attributes=copy.copy(data[0])
    print(attributes)
    
    for row in data[1:len(data)]:
        for i in range(1, len(row)):
            if int(row[i])>3:
                row[i]=1
            else:
                row[i]=0
    print(data)
    decision=[0, 1] # 0 dislike, 1 like
    attributeValue=[0, 1] # 0 dislike, 1 like

    target = []
    for i in range(1, len(data)):
        target.append(data[i][len(data[i])-1])
    HA=calculateHA(target)
    print(HA)

def makingTree():
    readData()
    initialzeData()
    rowSet=[]
    for i in range(1, len(data)):
        rowSet.append(i)
    # attr=findParent(attributes, rowSet)
    attributes.append('xx')
    root=ID3(attributes, 'xx', rowSet)
    
    validateTree(root, data)


def ID3(attrs, att, rowSet):
    attrs.remove(att)
    cd=checkDecision(rowSet)
    if cd[0]:
        leaf=Node()
        leaf.decision=cd[1]
        return leaf
    elif len(attrs)==1:
        leaf=Node()
        leaf.decision=getOneDecision(rowSet)
        return leaf
    else:
        node=Node()
        attr=findParent(attrs, rowSet)
        if attr=='User':
            return None
        node.name=attr
        column=0
        for i in range(1, len(data[0])):
            if data[0][i]==attr:
                column=i
                break
        childrenSet=[]
        for i in range(len(decision)):
            childrenSet.append([])
        for i in range(len(rowSet)):
            # decision 0, 1, 2...., so childrenSet 0, 1, 2... represent number of decisions.
            d=data[rowSet[i]][column]
            childrenSet[d].append(rowSet[i])
        node.left=ID3(copy.copy(attrs), attr, childrenSet[0])
        node.right=ID3(copy.copy(attrs), attr, childrenSet[1])
        return node
    pass

def findParent(attrs, rowSet):
    informationGains=[]
    distribution=[]
    # attrs includes identity(0) and decision(len(a)), so attrs are from 1 to n - 1. distribution [attribute: [decision p: [decision t: ]]]
    for i in range(1, len(attrs)-1):
        n=0
        distribution.append([])
        for j in range(len(decision)):
            distribution[i-1].append([])
            for k in range(len(decision)):
                distribution[i-1][j].append(0)
    print(distribution)
    ig=[]
    for i in range(1, len(attrs)-1):
        column=0
        # find current attribute from header
        for j in range(1, len(data[0])):
            if attrs[i]==data[0][j]:
                column=j
                break;
        # traverse row set to calculate subset of current attribute
        for j in range(len(rowSet)):
            # find value of attribute
            for k in range(len(decision)):
                # branchs/attribute value of current attribute
                if data[rowSet[j]][column]==decision[k]:
                    # find value of target
                    for d in range(len(decision)):
                        if data[rowSet[j]][len(data[0])-1]==decision[d]:
                            # branches of branches of current attribute
                            distribution[i-1][k][d]=distribution[i-1][k][d]+1
                            break
        print(distribution)
        # calculate information gain
        ig.append(0)
        ss=0
        splitInformation=0.0
        for j in range(len(distribution[i-1])):
            ss=ss+sum(distribution[i-1][j])
            if ss==0:
                continue
        for j in range(len(decision)):
            s=sum(distribution[i-1][j])
            if s==0:
                continue
            splitInformation=splitInformation-s/ss*np.log2(s/ss)
            temp=0
            for d in range(len(decision)):
                if distribution[i-1][j][d]!=0:
                    temp=temp-distribution[i-1][j][d]/s*np.log2(distribution[i-1][j][d]/s)
            ig[i-1]=s/ss*temp+ig[i-1]
        ig[i-1]=(HA-ig[i-1])/splitInformation
    print(ig)
    # find max information gain
    maxIG=0;
    maxIGColumn=-1
    for i in range(len(ig)):
        if ig[i]>maxIG:
            maxIG=ig[i]
            maxIGColumn=i
    if maxIGColumn==-1:
        maxIGColumn=-1
    return attrs[maxIGColumn+1]

# A is array of target
def calculateHA(A):
    ea=0.0
    p=[]
    for i in range(len(decision)):
        p.append(0)
    for i in range(len(A)):
        for j in range(len(decision)):
            if A[i]==decision[j]:
                p[j]=p[j]+1
                break;

    for i in range(len(p)):
        ea=ea-p[i]/total*np.log2(p[i]/total)

    return ea

def checkDecision(rowSet):
    if len(rowSet)==0:
        return [True, None]
    elif len(rowSet)==1:
        return [True, data[rowSet[0]][len(data[0])-1]]
    else:
        for i in range(1, len(rowSet)):
            if data[rowSet[0]][len(data[0])-1]!=data[rowSet[i]][len(data[0])-1]:
                return [False]
    return [True, data[rowSet[0]][len(data[0])-1]]

def getOneDecision(rowSet):
    ds=[]
    for i in range(len(decision)):
        ds.append[0]
    for i in range(len(rowSet)):
        for j in range(len(decision)):
            if data[len(data[0])-1][rowSet[i]]==decision[j]:
                ds[j]=ds[j]+1
                break
    max=ds[0]
    for i in range(1, len(decision)):
        if ds[i]>max:
            max=ds[i]
    return max

def getTreeDepth(tree):
    if tree==None:
        return 0
    cLeft=getTreeDepth(tree.left)+1
    cRight=getTreeDepth(tree.right)+1
    return max(cLeft, cRight)

def printTree(tree, depth, parentp):
    if tree==None:
        return;
    if parentp==0:
        width=0
        for i in range(depth):
            width=width+np.power(2, i)
        width=width/2
        print(' '*width, tree.name, sep='')
    else:
        offset=np.power(2,depth-1)
        print(' '*width, tree.name, sep='')
        printTree(tree.left, depth-1, )

def validateTree(tree, vdata):
    rightSet=[]
    wrongSet=[]
    for i in range(1, len(vdata)):
        row=vdata[i]
        node=tree
        while node.name!='':
            column=0
            for j in range(1, len(vdata[0])-1):
                if node.name==vdata[0][j]:
                    column=j
                    break
            if row[column]==0:
                node=node.left
            else:
                node=node.right
            if node==None:
                break
        if node==None:
            wrongSet.append(row[0])
        elif node.decision==row[len(vdata[0])-1]:
            rightSet.append(row[0])
        else:
            wrongSet.append(row[0])
    print(rightSet)
    print(wrongSet)

def prunningTree(tree):
    if tree==None:
        return;
    if tree.left.decision!=-1 and tree.right.decision!=-1:
        pass
    elif tree.left.decision==-1:
        prunningTree(tree.left)
    elif tree.right.decision==-1:
        prunningTree(tree.right)

class Node:
    name=''
    left=None
    right=None
    decision=-1

