letters = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
import random
lr1 = random.choice(letters)
lr2 = random.choice(letters) 
lr3 = random.choice(letters) 
lr4 = random.choice(letters) 
num = ("1234567890")
numr1 = random.choice(num)
numr2 = random.choice(num)
numr3 = random.choice(num) 
print(lr1 + lr2 + "-" + numr1 + numr2 + numr3 + "-" + lr3 + lr4)