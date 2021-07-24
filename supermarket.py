import sys
import datetime
items='''

rice:30/1kg
sugar-20/1kg
oil-150/1liter
salt-5/1kg
wheat-20/1kg
'''
print(5 * ' =>', "welcome to satyasupermarket","",datetime.datetime.now().strftime("%H:%M:%S"), 5 * ' =>')
il=[]
ql=[]
tl=[]
list=[]
finalprice=0
final=0
total1=0
itemslist = {"rice": 30, "sugar": 20, "oil": 150, "salt": 5, "wheat": 20}
name=input("enter your name")
a=input("enter 1 to see list of itmes")
if a=='1':
    print(items)
    for i in range(len(itemslist)):
        a=input("enter 1 to buy 2 to exit")
        if a=='1':
            pass
            option=input("enter the item u want to buy")
            if option in itemslist.keys():
                quant=int(input("enter the quantity"))
                price= quant*itemslist[option]
                list.append((option,quant,price))
                total1=price+total1
                il.append(option)
                ql.append(quant)
                tl.append(price)
                gst=(total1*0.5)/100
                finalprice=gst+total1
            else:
                 print("you entered wrong number")

        elif a=='2':
            break
        else:
            print("invalid option")
    q=input("do u want bill forthe items type yes or no")
    if q == "yes" or"yes":
        if finalprice!=0:
            print(25*"=","satya supermarket",25*"=")
            print("slno",5*' ',"name",4*' ',"quantity","total",5*' ')
            for i in range(len(list)):
                print(i,8*' ',il[i],6*' ',ql[i],6*' ',5*'',tl[i])
            print(5 * ' -', "total price", 5 * ' -', total1)
            print(50 * '-')
            print(5 * ' -', "gst price", 5 * ' -', gst)
            print(50 * '-')
            print(5*' -',"final price",5*'-',finalprice)
            print(50 * '-')
            print(5 * ' -', "thanks for visiting satyasupermarket","",name, 5 * ' -')
        else:
            print("you didnt buy anything",finalprice)
    elif q =="no"or"NO":
        print(50 * '-')
        print(5 * ' -', "final price",10 * ' -', finalprice)
        print(50 * '-')
        print(5 * ' -', "thanks for visiting satyasupermarket ",name,5 * ' -')
else:
    print(" invalid option")
