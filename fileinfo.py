a=input()
b=input()
list1=[]
list2=[]
mark=0
for i in range(len(a)//2):                #切片
    list1.append(a[2*i:2*i + 2])
for i in range(len(b)//2):
    list2.append(b[2*i:2*i + 2])
for j in range(len(list2)):
    list1.append(list2[j])
    if list1.count('1p') >= 3 and list1.count('2p') >= 1 and list1.count('3p') >= 1 and list1.count('4p') >= 1 and list1.count('5p') >= 1 and list1.count('6p') >= 1 and list1.count('7p') >= 1 and list1.count('8p') >= 1 and list1.count('9p') >= 3 and not (list1.count('1p') == 3 and list1.count('2p') == 1 and list1.count('3p') == 1 and list1.count('4p') == 1 and list1.count('5p') == 1 and list1.count('6p') == 1 and list1.count('7p') == 1 and list1.count('8p') == 1 and list1.count('9p') == 3):
        print(j+1)
        mark+=1
        break
    elif list1.count('1s') >= 3 and list1.count('2s') >= 1 and list1.count('3s') >= 1 and list1.count('4s') >= 1 and list1.count('5s') >= 1 and list1.count('6s') >= 1 and list1.count('7s') >= 1 and list1.count('8s') >= 1 and list1.count('9s') >= 3 and not (list1.count('1s') == 3 and list1.count('2s') == 1 and list1.count('3s') == 1 and list1.count('4s') == 1 and list1.count('5s') == 1 and list1.count('6s') == 1 and list1.count('7s') == 1 and list1.count('8s') == 1 and list1.count('9s') == 3):
        print(j+1)
        mark+=1
        break
    elif list1.count('1m') >= 3 and list1.count('2m') >= 1 and list1.count('3m') >= 1 and list1.count('4m') >= 1 and list1.count('5m') >= 1 and list1.count('6m') >= 1 and list1.count('7m') >= 1 and list1.count('8m') >= 1 and list1.count('9m') >= 3 and not (list1.count('1m') == 3 and list1.count('2m') == 1 and list1.count('3m') == 1 and list1.count('4m') == 1 and list1.count('5m') == 1 and list1.count('6m') == 1 and list1.count('7m') == 1 and list1.count('8m') == 1 and list1.count('9m') == 3):
        print(j+1)
        mark+=1
        break
if mark==0:
    print('Stop Your Daydream!')
import turtle
turtle.setup(650,350,200,200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("purple")
turtle.seth(-40)
for i in range (4):
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
