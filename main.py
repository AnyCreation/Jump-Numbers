import Find as FJ

NumJump = input(":").split()
print(NumJump)
list_num = [float(i) for i in NumJump]

NUMs = FJ.Jump(list_num)
print(N)

if NUMs[0] == True and NUMs[1] == True:
    print("The list must contain 3 elements")
else:
    if NUMs[1] == True:

        if NUMs[0][0] == True:
            print(f'Jump == X + {list_num[1] - list_num[0]}')

        elif NUMs[0][1] == True:
            print(f'Jump == X * {list_num[1] / list_num[0]}')

        elif NUMs[0][2] == True:
            print(f'Jump == X ** 2')

    elif NUMs[0] == True and NUMs[1] == False:
            print('All elements in list are the same')
            

    elif NUMs[1] == False:
        
        if NUMs[0][0] == True:
            print(f'Jump == X - {list_num[0] - list_num[1]}')

        elif NUMs[0][1] == True:
            print(f'Jump == X / {list_num[0] / list_num[1]}')

        elif NUMs[0][2] == True:
            print(f'Jump == X ** 0.5')
 
