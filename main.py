import Find
NumJump = input(":").split()
print(NumJump)
list_num = [float(i) for i in NumJump]

NUMs = Find.Jump(list_num)


if len(NUMs) == 1:
    if NUMs:
        print('Jump is break')
else:
    if NUMs[0] == True and NUMs[1] == True:
        print("The list must contain 3 elements")
    else:
        if NUMs[1]:

            if NUMs[0][0]:
                print(f'Jump == X + {list_num[1] - list_num[0]}')

            elif NUMs[0][1]:
                print(f'Jump == X * {list_num[1] / list_num[0]}')

            elif NUMs[0][2]:
                print(f'Jump == X ** 2')

        elif NUMs[0] and NUMs[1]:
                print('All elements in list are the same')


        elif NUMs[1]:

            if NUMs[0][0]:
                print(f'Jump == X - {list_num[0] - list_num[1]}')

            elif NUMs[0][1]:
                print(f'Jump == X / {list_num[0] / list_num[1]}')

            elif NUMs[0][2]:
                print(f'Jump == X ** 0.5')

