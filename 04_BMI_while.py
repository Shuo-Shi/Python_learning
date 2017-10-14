h = float(input('please input height(m):'))
w = float(input('please input weight(kg):'))
bmi = w/(h*h)
falg = ('过轻','正常','过重','肥胖','严重肥胖')
thre = (18.5,25,28,32)
dex = 0;
while bmi>thre[dex]:
    dex = dex +1
    if dex==len(thre):break
print(falg[dex],'\t',bmi)
