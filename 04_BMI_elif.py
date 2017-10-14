height = float(input('please input height(m):'))
weight = float(input('please input weight(kg):'))

bmi = float(weight/(height**2))
if 18.5>bmi:
    print('你bmi指数为:%.2f\n过轻'%bmi)
elif 18.5<=bmi<25:
    print('你bmi指数为:%.2f\n正常'%bmi)
elif 25<=bmi<28:
    print('你bmi指数为:%.2f\n过重'%bmi)
elif 28<=bmi<32:
    print('你bmi指数为:%.2f\n肥胖'%bmi)
elif 32<= bmi:
    print('你bmi指数为:%.2f\n严重肥胖'%bmi)