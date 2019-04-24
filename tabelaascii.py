###################################################################################
#Impressora de Tabela ASCII
#Vinícius Rabello Rodrigues
#DRE:119056899
#Curso: Matemática Aplicada
###################################################################################

print('Use a função "ImprimirTabela(ini,fim,tam)", para imprimir a tabela ASCII')

def ImprimirTabela(ini = 32, fim = 127, tam = 25):
    i = ini
    c = 0

    if ini < 32: ini = 32
    if fim > 127: fim = 127

    for i in range (ini, fim + 1):

        if c % (tam + 1) == 0:
            print('+','-' * 17,'+','-' * 7,'+','-' * 6,'+','-' * 7,'+','-' * 3,'+')
            print('|','     Binario     ','|','  Oct  ','|','  Hex ','|','  Dec  ','|','Chr','|')
            print('+','-' * 17,'+','-' * 7,'+','-' * 6,'+','-' * 7,'+','-' * 3,'+')
            c += 1

        if 64 > i:
            print('|     {} {}     |   {}   |   {}   |   {}   |  {}  |'.format(bin(i)[2:].zfill(8)[:4],bin(i)[-4:],oct(i)[2:].zfill(3),hex(i)[2:],str(i).zfill(3),chr(range(32,128)[i%95])))
            c += 1
        if i >= 64 and 100 > i:
            print('|     {} {}     |   {}   |   {}   |   {}   |  {}  |'.format(bin(i)[2:].zfill(8)[:4],bin(i)[-4:],oct(i)[2:].zfill(3),hex(i)[2:],str(i).zfill(3),chr(range(32,128)[i%95])))
            c += 1
        if i >= 100 and 127 > i:
            print('|     {} {}     |   {}   |   {}   |   {}   |  {}  |'.format(bin(i)[2:].zfill(8)[:4],bin(i)[-4:],oct(i)[2:].zfill(3),hex(i)[2:],str(i).zfill(3),chr(range(32,128)[i%95])))
            c += 1
        if i == 127:
            print('|     {} {}     |   {}   |   {}   |   {}   |  {}  |'.format(bin(i)[2:].zfill(8)[:4],bin(i)[-4:],oct(i)[2:].zfill(3),hex(i)[2:],str(i).zfill(3),chr(range(32,128)[i%95])))
            c += 1
    
    print('+','-' * 17,'+','-' * 7,'+','-' * 6,'+','-' * 7,'+','-' * 3,'+')
