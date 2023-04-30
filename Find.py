
"""

1 < 2 < 4 < 8 < 16 || X * 2
16 > 8 > 4 > 2 > 1 || X / 2

1 < 3 < 5 < 7 < 9 || X + 2
10 < 7 < 4 < 1 || X - 3

2 < 4 < 16 < 256 < 65536 || X^2
65536 < 256 < 16 < 4 < 2 || X^0.5

2 < 4 < 256 || X^X


"""

def SomeJump(list_X):
    pass

def Jump(list_X):
    
    UpDown, Equals = False, False
    PMSp = [False, False, False]
    MDSr = [False, False, False]
    Break = False
    ThreeEle = False

    if len(list_X) < 3:
        ThreeEle = True
        return ThreeEle, ThreeEle
    else:
        #Up Jump
        if list_X[0] < list_X[1]:
            UpDown = True
            if list_X[1] + (list_X[1] - list_X[0]) == list_X[2]:
                for i in range(2, len(list_X)):
                    if list_X[i-1] + (list_X[1] - list_X[0]) == list_X[i]:
                        PMSp[0] = True
                        return PMSp, UpDown
                    else:
                        Break = True
                        return Break
                        
            elif list_X[1] * (list_X[1] / list_X[0]) == list_X[2]:
                for i in range(3, len(list_X)):
                    if list_X[i-1] * (list_X[1] / list_X[0]) == list_X[i]:
                        PMSp[1] = True
                        return PMSp, UpDown
                    else:
                        Break = True
                        return Break
                        
            elif list_X[0] ** 2 == list_X[1]:
                for i in range(3, len(list_X)):
                    if list_X[i-1] ** 2 == list_X[i]:
                        PMSp[2] = True
                        return PMSp, UpDown
                    else:
                        Break = True
                        return Break

        #All elements in the list are the same//breaking
        elif list_X[0] == list_X[1]:
            Equals = True
            for i in range(2, len(list_X)):
                if list_X[i-1] == list_X[i]:
                    return Equals
                else:
                    Break = True
                    return Break
        #Down Jump
        else:
            UpDown = False
            if list_X[1] - (list_X[0] - list_X[1]) == list_X[2]:
                for i in range(3, len(list_X)):
                    if list_X[i-1] - (list_X[0] - list_X[1]) == list_X[i]:
                        MDSr[0] = True
                        print(3)
                        return MDSr, UpDown
                    else:
                        Break = True
                        return Break
                        
            elif list_X[1] / (list_X[0] / list_X[1]) == list_X[2]:
                for i in range(3, len(list_X)):
                    if list_X[i-1] / (list_X[0] / list_X[1]) == list_X[i]:
                        MDSr[1] = True
                        return MDSr, UpDown
                    else:
                        Break = True
                        return Break
            
            elif list_X[0] ** 0.5 == list_X[1]:
                for i in range(2, len(list_X)):
                    if list_X[i-1] ** 0.5 == list_X[i]:
                        MDSr[2] = True
                        return MDSr, UpDown 
                    else:
                        Break = True
                        return Break
