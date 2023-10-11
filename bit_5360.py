### funções a serem utilizadas

def invertev(v): #inverte vetores
    for i in range(len(v)//2):
        c = v[i]
        v[i] = v[len(v)-1-i]
        v[len(v)-1-i] = c
    return v

def binario(a): #esta função transforma um decimal em binário e os deixa com 10 casas
    q = a
    v = []
    if q != 0:
        while q != 0:
            b = q % 2
            q = q // 2
            v.append(b)

        while len(v) < 11:
            v.append(0)

        v = invertev(v)
    else:
        for i in range(11):
            v.append(0)

    return v


def sbin(a, b): #esta função soma dois binarios
    v = []
    c = 0
    for i in range(len(a)):
        if a[(len(a)-1-i)] + b[(len(b)-1-i)] + c == 0:
            v.append(0)
        elif a[(len(a)-1-i)] + b[(len(b)-1-i)] + c == 1:
            c = 0
            v.append(1)
        elif a[(len(a)-1-i)] + b[(len(b)-1-i)] + c == 2:
            c = 1
            v.append(0)
        elif a[(len(a)-1-i)] + b[(len(b)-1-i)] + c == 3:
            c = 1
            v.append(1)
    v = invertev(v)
    return v

def bindec(a): #transforma binario em decimal
    count = 0
    invertev(a)
    for i in range(len(s)):
        count += s[i] * (2**i)
    return(count)

### Inicio do código

n1 = int(input())
n2 = int(input())
tipo = int(input())

if (n1 >= 0 and n2 >= 0 and n1 <= 512 and n2 <= 512) and (tipo == 2 or tipo == 8 or tipo == 10 or tipo == 16):
    b1 = binario(n1)
    b2 = binario(n2)

    s = sbin(b1, b2)
    count = 0

    if tipo == 2:
        for i in range(len(s)):
            print(s[i], end='')

    elif tipo == 10:
        print(bindec(s))

    elif tipo == 8: # converte decimal para octal
        s = bindec(s)
        v = []
        r = 0
        if s != 0:
            while s >= 8 :
                    r = s % 8
                    s = s // 8
                    v.append(r)
            if s != 0:
                v.append(s)
            while len(v) < 4:
                v.append(0)
            for i in range(len(v)):
                print(v[len(v)-1-i], end="")
        else:
            print(0000)

    elif tipo == 16:
        dh = "0123456789ABCDEF"#dicionário de hexadecimal
        s = bindec(s)
        r = ""
        q = 0
        if s == 0:
            print(000)
        else:
            while s > 0:
                q = s%16
                r = dh[q] + r
                s = s // 16
                
            r = r.zfill(3)
            
            print(r)
else:
    print("ERRO")