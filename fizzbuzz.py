def fizz_buzz(i : int):
    if i%3==0 and i%5==0:
        return "fizz buzz"
    elif i%3==0:
        return "fizz"
    elif i%5==0:
        return "buzz"
    else :
        return i

n=0
while (n<100):
    n+=1
    print(fizz_buzz(n))
    n+=1
    cor_ans=fizz_buzz(n)
  #  urans=input("your turn\n")
    urans=str(cor_ans)
    if (urans)!=str(cor_ans):
        print("oops wrong ans")
        break
    