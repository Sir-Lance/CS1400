import random

ary = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 0]
def shuffle(ary):
    a=len(ary)
    b=a-1
    for d in range(b,0,-1):
      e=random.randint(0,d)
      if e == d:
            continue
      ary[d],ary[e]=ary[e],ary[d]
    return ary

result = shuffle(ary)
print(result)
