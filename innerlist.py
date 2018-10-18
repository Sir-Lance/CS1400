X = [1, 2, 3, 4]
Y = [5, 6, 7, 8]

def innerProd(X, Y):
   if len(X) != len(Y):
      return X * Y

   return sum(i[0] * i[1] for i in zip(X, Y))

result = innerProd(X, Y)
print(result)
