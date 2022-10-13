import random
ques=['1+1','2+2','3+3','4+4',"5+5","6+6","7+7","8+8","9+9","10+10"]
ans=["2","4","6","8",'10','12','14','16','18','20']
score=0
x1=random.randint(0,9)
q1=ques[x1]
a1=ans[x1]

t1=4
while t1>1:
    ua1=input("enter ans for this "+q1)
    t1-=1
    if ua1==a1 and t1==3:
        score+=25
        break
        
    elif ua1==a1 and t1==2:
        
        score+=10
        break
    elif ua1==a1 and t1==1:
        score+=5
        break
    print("incorrect ans try again")
ques.pop(x1)
ans.pop(x1)
x2=random.randint(0,8)
q2=ques[x2]
a2=ans[x2]
t2=4
while t2>1:
    ua2=input("enter ans for this "+q2)
    t2-=1
    if ua2==a2 and t2==3:
        score+=25
        break
    elif ua2==a2 and t2==2:
        
        
        score+=10
        break
    elif ua2==a1 and t2==1:
        
        score+=5
        break
    print("incorrect ans try again")

ques.pop(x2)
ans.pop(x2)
x3=random.randint(0,7)
q3=ques[x3]
a3=ans[x3]
t3=4
while t3>1:
    ua3=input("enter ans for this "+q3)
    t3-=1
    if ua3==a3 and t3==3:
        score+=25
        break   
    elif ua3==a3 and t3==2:
        score+=10
        break
    elif ua3==a3 and t3==1:
        
        score+=5
        break
    print("incorrect ans try again")

ques.pop(x3)
ans.pop(x3)
x4=random.randint(0,6)
q4=ques[x4]
a4=ans[x4]
t4=4
while t4>1:
    ua4=input("enter ans for this "+q4)
    t4-=1
    if ua4==a4 and t4==3:
        score+=25
        break   
    elif ua4==a4 and t4==2:
        score+=10
        break
    elif ua4==a4 and t4==1:
        
        score+=5
        break
    print("incorrect ans try again")
ques.pop(x4)
ans.pop(x4)
print("your score out of 100 is",score)





