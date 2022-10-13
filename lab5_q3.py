import random
x=['text','lol','hi','new','why','how','where','there','then','thus']
y=['kuputuhi','paka','kia ora','Hōu','he aha','me pēhea','Kei hea','reira','taua wā','na reira']
a=random.randint(0,9)
b=random.randint(0,9)
c=random.randint(0,9)
d=random.randint(0,9)
mouri=[y[a],y[b],y[c],y[d]]
lmao=[x[a],x[b],x[c],x[d]]
a1=random.randint(0,3)
b1=random.randint(0,3)
c1=random.randint(0,3)
d1=random.randint(0,3)
a2=lmao[a1]
b2=lmao[b1]
c2=lmao[c1]
d2=lmao[d1]

o=mouri[a1]
r=lmao[a1]
print(r)
print('tell english of %s'%(o))
print('your options are:\n 1 %s\n 2 %s\n 3 %s\n 4 %s\n'%(a2,b2,c2,d2))
p=int(input('pls enter your choice among us'))


print(r)

if r==lmao[a1]:
    print("congrats you are right")
else:
    print('sry u r wrng')


