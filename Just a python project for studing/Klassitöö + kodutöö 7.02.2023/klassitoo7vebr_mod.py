#B-1 Kool
#
#Напишите функцию kool(), при запуске которой происходит заполнение двух списков: ученики[], прогулы[].
#После заполнения списков появляется меню с выбором действий:
#• Узнать n лучших учеников; если количество прогулов меньше 20
#• Упорядочить список в порядке возрастания прогулов. отобразить прогулы вместе с фамилиями учеников;
#• Вывести список учеников отправленных на комиссию ( критерий придумать самостоятельно);
#• Отчислить(удалить из списка)  учеников, у которых прогулов больше чем 100;
#• Свой вариант.
#Для решения задачи используйте функции.
from pickle import TRUE
from struct import pack


def loe_failist(file:str)->list:
    fail=open(file,'r',encoding="utf-8-sig")
    mas=[]
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas


def lisamine(mas:list,file:str):
    f=open(file,'w',encoding="utf-8-sig")
    for item in mas:
        f.write(item+"\n")
    f.close()

def element_listisse(p:list,i:list):
    n=int(input("Mitu opilasi lisame?\n"))
    for j in range (n):
        nimi=input("Nimi: ").lower()   
        i.append(nimi)
        palk=input("Puudumised: ")
        p.append(palk)
    return p,i

def best_student(p:list, o:list):
    N = len(p)
    best = []
    smallest = []
    for i in range(N):
        if int(p[i])<20:
            best.append(p[i])
            smallest.append(o[i])
    for i in range(len(best)):
        print(f"{best[i]} - {smallest[i]}" )

def sorteerimine(p:list, o:list): 
    N = len(p)
    for i in range(N):
        for j in range(i+1,N):
            if int(p[i])>int(p[j]):
                abi = p[i]
                p[i] = p[j]
                p[j] = abi
                abi = o[i]
                o[i] = o[j]
                o[j] = abi
    return p, o

def commision(p:list, o:list):
    N = len(p)
    for i in range(N):
        if int(p[i])>50:
            print(f"Opilane {o[i]} toodud komissioonile puudumise arvuga - {p[i]}\n")

def exmat(p:list,o:list):
    p=list(map(int,p))
    for i in range(len(p)):    
        for j in p:
                if j >= 100:
                    ind = p.index(j)
                    print(f"Opilane {o[ind]} - eksmatrikuleeritud!\n")
                    p.remove(j)
                    o.pop(ind)

def puudumistoend(name:str,paev:int,p:list, o:list):
    p=list(map(int,p))
    name = name.lower()
    try:
        ind = o.index(name)
        print(f"Teie lapsel on kokku {p[ind]} puudumist. \nTeil on võmalik kustutuda ainult {p[ind]} päeva.")
        while True:    
            if int(paev) <= p[ind]:
                if name in o:
                    p[ind] = p[ind] - int(paev)
                    if int(p[ind]) >= 0:
                        print(f"Opilasel - {name} on muutunud puudumise arvu {p[ind]}-ks!")
                        break
            else:
                print("Te sisestasite palju rohkem kui on see võimalik!")
                break
    except:
       print("See opilane puudub meie koolis või te sisestasite vale andmetüüp!")


def kustuta(nimi:str,p:list,i:list):
    n=i.count(nimi)
    pos=0
    for j in range(n):
        ind=i.index(nimi,pos)
        pos=ind
        i.remove(nimi)
        p.pop(ind)
    return p,i    