# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for x in [0, 1]:
    for y in range (2):
        for z in [0, 1]:
            print(f'x = {x}, y = {y}, z = {z}')
            rezult = not(x or y or z)
           # print(result)
            res = not x and not y and not z
            #print(res)
            print(rezult == res)
