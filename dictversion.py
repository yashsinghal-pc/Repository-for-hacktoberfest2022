import random

filename='Maori2Eng.txt'
maori2eng=[]
with open(filename,'r') as docs:
    for i in range(50):
        get=docs.readline().strip('\n').split(',')
        print(get)
        maori2eng.append(get)

print("WELCOME TO GAME")
ch1={'1','2',''}
choice=''
points=0
score=0
print("CHOOSE BETWEEN 2 MODES \n 1. QNA\n 2. MCQ\npress anything to exit".upper())
choice=input("ENTER mode number : ".upper())


if choice in ch1:
    if choice=='1':
        print("\n\nLET'S PLAY QNA MODE")
        
        for i in range(10):
            co_qno=random.randint(0,len(maori2eng)-1)
            print(co_qno)
            correct_pair=maori2eng[co_qno]
            ans=input(f"{i+1}. TRANSLATE '{correct_pair[1]} ' TO MAORI :")
            del maori2eng[co_qno]
            if ans.casefold()==correct_pair[0]:
                print("your answer is correct \n +1points".upper())
                points+=1
            else:
                print("your answer is incorrect\n +0 points".upper())
    elif choice=='2':
        print("\n\nlet's play mcq mode".upper())
        
        for i in range(10):
            correctQ=random.randint(0,len(maori2eng)-1)
            a=random.randint(0,len(maori2eng)-1)
            b=random.randint(0,len(maori2eng)-1)
            c=random.randint(0,len(maori2eng)-1)
            mcq=[maori2eng[correctQ],maori2eng[a],maori2eng[b],maori2eng[c]]
        
            print("\nwhat is the translation of '{}'?".format(maori2eng[correctQ][1]).upper())
            
            fmcq=random.sample(mcq,4)
            for index, value in enumerate(fmcq):
                print(f"\t{index+1} : {value[0]}")
            
            your_answer=input("enter following number  : ".upper())
            correct_answer=maori2eng[correctQ]
            valid_ans_options={'1','2','3','4'}
            
            if your_answer not in valid_ans_options:
                print("enter valid choice\n no marks given".upper())
                continue
            
            if fmcq[int(your_answer)-1] == correct_answer:
                print("your answer is correct \n +1points".upper())
                points+=1
            else:
                print("your answer is incorrect\n +0 points".upper())
            del correct_answer
    score=points
        # score2
else:
    print("enter valid choice\n".upper())
print("\nyou have exited the game".upper())
print(f"your score for mode is '{score}'".upper())
