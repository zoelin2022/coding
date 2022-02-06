import random

# 讓使用者決定隨機數字的範圍
min = input('請輸入範圍最小的數字：')
min = int(min)
max = input('請輸入範圍最大的數字：')
max = int(max)

r = random.randint(min, max)
print(r)
count = 0
while True:
    num = input('請猜數字：')
    num = int(num)
    count += 1
    if num == r:
        print('終於猜對了')
        print(f"總共猜了{count}次")
        break
    elif num > r:
            print('比答案大')
    elif num < r:
            print('比答案小')
    print(f"這是你猜的第{count}次")