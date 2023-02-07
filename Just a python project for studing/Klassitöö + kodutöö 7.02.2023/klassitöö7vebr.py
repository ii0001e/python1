#B-1 Kool
#
#Напишите функцию kool(), при запуске которой происходит заполнение двух списков: ученики[], прогулы[].
#После заполнения списков появляется меню с выбором действий:
#• Узнать n лучших учеников;
#• Упорядочить список в порядке возрастания прогулов. отобразить прогулы вместе с фамилиями учеников;
#• Вывести список учеников отправленных на комиссию ( >50 прогулов);
#• Отчислить(удалить из списка)  учеников, у которых прогулов больше чем 100;
#• Изменение прогулов.
#Для решения задачи используйте функции.

from klassitoo7vebr_mod import *
opilased=[]
puudumised=[]
opilased=loe_failist("opilased.txt")
puudumised=loe_failist("puudumised.txt")
try:
    while True:
        print("_"*30)
        print("0 - Loe failist\n1 - Opilaste lisamine\n2 - Salvestame failisse\n3 - Kustuta\n4 - Parimad opilased\n5 - Sorteerimine\n6 - Opilased komissioonile\n7 - Eksmatrikuleerimine\n8 - Esita puudumistõend\n9 - Exit") 
        v=int(input())
        if v == 0:
            print(puudumised)
            print(opilased)
        elif v == 1:
            puudumised, opilased = element_listisse(puudumised,opilased)
            print(puudumised)
            print(opilased)
        elif v == 2:
            lisamine(puudumised,"puudumised.txt")
            lisamine(opilased,"inimesed.txt")
        elif v == 3:
            print(opilased)
            puudumised,opilased = kustuta(input("Keda kustutada? "),puudumised,opilased)
        elif v == 4:
            best_student(puudumised,opilased)
        elif v == 5:
            sorteerimine(puudumised,opilased)
            for i in range(len(puudumised)):
                print(f"{opilased[i]} - {puudumised[i]}")
        elif v == 6:
            commision(puudumised,opilased)
        elif v == 7:
            exmat(puudumised,opilased)
        elif v == 8:
            print(opilased)
            puudumistoend(input("opilasee nimi --> "),input("Sisesta puudumise arv --> "),puudumised,opilased)
        else:
            exit()
except:
    print("Vale endmetüüp!")

