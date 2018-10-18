'''
题目：企业发放的奖金根据利润提成。
利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%，
高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
程序分析：请利用数轴来分界，定位。注意定义时需把奖金定义成长整型。
'''
Money = 0
Total = int(input("请输入奖金值,单位万元"))
'''
if (Total <= 10):
    Money = Total * 0.1
elif (Total > 10 <= 20):
    Money = 10 * 0.1 + (Total - 10) * 0.075
elif (20 < Total <= 40):
    Money = 10 * 0.1 + 10*0.075 + (Total - 20) * 0.05
elif (40 < Total <= 60):
    Money = 10 * (0.1 + 0.075 + 2*0.05) + (Total - 40) * 0.03
elif (60< Total <= 100):
    Money = 10 * (0.1 + 0.075 + 2*0.05 + 2*0.03) + (Total - 60) * 0.015
elif (Total > 100):
    Money = 10 * (0.1 + 0.075 + 2*0.05 + 2*0.03 + 4*0.015) + (Total - 100) * 0.01
print(Money)

version 2
arr = [0, 10, 20, 40, 60, 100]
rate = [0.1, 0.075, 0.05, 0.03, 0.015, 0.01]

for idx in range(1,6):
    if (Total >= arr[idx]):
        Money += (arr[idx]-arr[idx-1]) * rate[idx-1]
        print(Money)
    else:
        Money += (Total - arr[idx-1]) * rate[idx -1]
        print(Money)

'''

arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0
for idx in range(0,6):
    if Total>arr[idx]:
        r+=(Total-arr[idx])*rat[idx]
        print((Total-arr[idx])*rat[idx])
        Total=arr[idx]
print(r)