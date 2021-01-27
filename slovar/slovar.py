def loe_failist(f):
    fail=open(f,'r',encoding="utf-8-sig")
    mas=[]
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas

def salvesta_failisse(f,text):
    fail=open(f,"a",encoding="utf-8-sig")
    fail.write+(text+"\n")
    fail.close()
    mas=[]
    mas=loe_failist(f)
    return mas
def tolkimine(rus,eng):
    slovo=input("Введи слово->")
    if slovo in rus:
        ind=rus.index(slovo)
        print(f"{slovo}-{eng[ind]}")
    elif slovo in eng:
            ind2=eng.index(slovo)
            print(f"{slovo}-{eng[ind]}")

def parandus():
    viga=input("Какое слово хотите исправить?")
    if viga in rus:
        ind=rus.index(viga)
        print(f"Будет исправлена пара слов{viga}-{en_list[ind]}")
        rust.pop(ind)
        eng.pop(ind)
        new_words()
    elif viga in eng:
        ind=eng
        print(f"Будет исправлена пара слов{viga}-{rus_list[ind]}")
        rus.pop(ind)
        eng.pop(ind)
        new_words()
    else:
        print(f"{viga.upper()} отсутствует в словаре")
        return rus,eng
        

rus=loe_failist("rus.txt")
eng=loe_failist("eng.txt")
print(rus)
print(eng)

while True:
    g=input("1->перевод,2->Новое слово,3->испровление ошибок,4->Проверка знаний->")
    if g=="1":
        tolkimine(rus,eng)
    elif g=="2":
        rus,eng = new_sen8()
    elif v=="3":
        print(ru_list,en_list)
        ru_list,en_list=parandus
        (ru_list,en_list)
        print(ru_list,en_list)

    





