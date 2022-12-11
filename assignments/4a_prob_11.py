import random

random1 = random.randint(0, 500)
random2 = random.randint(0, 500)
random3 = random.randoint(0,500)


print(random1, random2)
print(random1, random2)
print(random1, random2)

user_answer = int(input('Type your answer: '))

def check(random1, random2):
    if ((random1 + random2) == user_answer):
        print('Congrast you are right!')
    else: print('Wrongg!!')

answer = check(random1,random2)

print(answer)
