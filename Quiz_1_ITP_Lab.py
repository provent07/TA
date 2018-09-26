dicttop={}
dictmid={}
dictbot={}

def TOP():
    decide= input("put or take: ")
    if decide=="put":
        food= input("the food name")
        weight= int(input("The weight:"))
        if food in dicttop:
            dicttop[food]=dicttop.get(food) +weight
        else:
            dicttop[food]=weight
        sum(dicttop.values())
        if (sum(dicttop.values()))>15:
            dicttop[food] = dicttop.get(food) -weight
            print("Too heavy")
        else:
            print("Still can store",(15-sum(dicttop.values())))
    else:
        food=input("What do you want to take:")
        if food in dicttop:
            items=list(dicttop.items())
            print(items)
            weight= int(input("How much do you want to take:"))
            dicttop[food] = dicttop.get(food) - weight
            if dicttop.values()== [0]:
                del dicttop[food]
            if dicttop[food]<0:
                dicttop[food] = dicttop.get(food) + weight
                print ("You are broke")
            print ("Still can store",(15-sum(dicttop.values())))
        else:
            print("Nothing There")

def MID():
    decide= input("put or take: ")
    if decide=="put":
        food= input("the food name")
        weight= int(input("The weight:"))
        if food in dictmid:
            dictmid[food]=dictmid.get(food) +weight
        else:
            dictmid[food]=weight
        sum(dictmid.values())
        if (sum(dictmid.values()))>15:
            dictmid[food] = dictmid.get(food) -weight
            print("Too heavy")
        else:
            print("Still can store",(15-sum(dictmid.values())))
    else:
        food=input("What do you want to take:")
        if food in dictmid:
            items=list(dictmid.items())
            print(items)
            weight= int(input("How much do you want to take:"))
            dictmid[food] = dictmid.get(food) - weight
            if dictmid.values()== [0]:
                del dictmid[food]
            if dictmid[food]<0:
                dictmid[food] = dictmid.get(food) + weight
                print ("You are broke")
            print ("Still can store",(15-sum(dictmid.values())))
        else:
            print("Nothing There")

def BOT():
    decide= input("put or take: ")
    if decide=="put":
        food= input("the food name")
        weight= int(input("The weight:"))
        if food in dictbot:
            dictbot[food]=dictbot.get(food) +weight
        else:
            dictbot[food]=weight
        sum(dictbot.values())
        if (sum(dictbot.values()))>15:
            dictbot[food] = dictbot.get(food) -weight
            print("Too heavy")
        else:
            print("Still can store",(15-sum(dictbot.values())))
    else:
        food=input("What do you want to take:")
        if food in dictbot:
            items=list(dictbot.items())
            print(items)
            weight= int(input("How much do you want to take:"))
            dictbot[food] = dictbot.get(food) - weight
            if dictbot.values()== [0]:
                del dictbot[food]
            if dictbot[food]<0:
                dictbot[food] = dictbot.get(food) + weight
                print ("You are broke")
            print ("Still can store",(15-sum(dictbot.values())))
        else:
            print("Nothing There")

fridge=input("Do you want to open the refrigerator:(yes/no)")
if fridge == "yes":
    select = input("top, mid, bot, or exit")
    while select == 'top':
        TOP()
        select = input("top, mid, bottom, or exit")
    while select == 'mid':
        MID()
        select = input("top, mid, bottom, or exit")
    while select == 'bot':
        BOT()
        select = input("top, mid, bottom, or exit")
    while select == 'exit':
        print ("Go away")

else:
    print("Go away")
