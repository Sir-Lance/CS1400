#35.74 + 0.6215 * T - (35.75 * (V ** 0.16)) + 0.4275 * T * (V ** 0.16)
t = -30
v = 0
print(end = '\t\t')
for z in range(1, 11):
    v = v + 5
    print(v, end = '\t\t')

v = -5
print()
for i in range(1, 10):
    t = t + 10
    print(t, end = '\t\t')
    for j in range(10):
        v = v + 5
        wc = 35.74 + 0.6215 * t - (35.75 * (v ** 0.16)) + 0.4275 * t * (v ** 0.16)
        print(wc // 1, end = '\t\t')
    print()
    #print('\t', t)
    #print(v, '\n')
