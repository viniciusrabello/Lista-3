import os

def ecsv(x = '.'):
    arq = os.listdir(x)
    lcsv=[]
    for csv in arq:
        if csv[-4:] == '.csv':
            lcsv.append(csv)
        else:
            pass

    lincsv = 0
    a = 0

    for i in lcsv:        
        arq = open(i,'r')
        q = arq.read()        
        b = q.count('\n')        
        lincsv += b
        w = q.split('\n')[4]
        e = w.split(';')
        a += len(e)

    r = 'os arq possuem: ' +str(b)+ ' linhas, e ' +str(a)+ ' colunas.'   

    return r
