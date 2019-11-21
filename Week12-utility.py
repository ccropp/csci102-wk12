# https://github.com/ccropp/csci102-wk12
# Cason Cropp
# CSCI102-B
# Week12 A


def PrintOutput(x):
    x = str(x)
    print('OUTPUT {}'.format(x))

#PrintOutput('hello')

def LoadFile(x):
    f = open(x,'r')
    s = str(f.read())
    return s

def UpdateString(x,y,n):
    x[n] = y
    return x

def FindWordCount(x,y):
    lx = len(x)
    ly = len(y)
    s = 0
    for i in range(lx-ly):
        if x[i:i+ly] == y:
            s += 1
    return s
        
def ScoreFinder(x,y,z):
    s = 0
    for i in range(len(x)):
        if x[i] == z:
            print('OUTPUT {} got a score of {}'.format(z,y[i]))
            s += 1
    if s == 0:
        print('OUTPUT player not found')
            
def Union(x,y):
    w = x + y
    return w

def Intersection(x,y):
    w = []
    for i in range(len(x)):
        for j in range(len(y)):
            if x[i] == y[j]:
                w.append(x[i])
    return w

def NotIn(x,y):
    w = []
    for i in range(len(x)):
        for j in range(len(y)):
            if x[i] != y[j]:
                w.append(x[i])
    return w

