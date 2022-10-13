def read_data(filename):
    l=open(filename,'r')
    list0=[]
    for i in l:
        list0.append(i)
    return list0
print(read_data(Lab9_data1.txt))
