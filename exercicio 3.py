import os

def contpasta(a = '.'):
    arq = os.listdir(a)
    txts = []
    for txt in arq:
        if txt[-4:]=='.txt':
            txts.append(txt)
        else:                   
            pass

    pal = [] 
    fq = []
    pf = []
    print(txt)

    for i in txts:
        arq = open(i,'r')
        q = arq.read() 
        z = q.split(" ")
        for p in z:
            p.replace(',','')            
            p.replace('.','')
            p.replace(':','')
        pal += z 
    for i in pal:
        z = i.split('\n')
        pal.remove(i)
        pal += z
    
    paluni = list(dict.fromkeys(palavras))   
    for x in paluni:
        y=str(pal.count(x))
        pf.append(x+' - '+y)
    pf.sort(key= lambda a: int(a.split(' - ')[1]) ,reverse=True) 
    return pf
