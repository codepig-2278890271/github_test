# 超级简单的 Python 小程序：猜数字游戏
# 直接复制到只读编译器里运行就行！

import random
number = random.randint(1, 10)
print("我想了一个 1 到 10 之间的数字，来猜猜看！")

while True:
    guess = int(input("请输入你的猜测："))
    if guess < number:
        print("太小啦！再试试～")
    elif guess > number:
        print("太大啦！再试试～")
    else:
        print("恭喜你，猜对了！🎉")
        break