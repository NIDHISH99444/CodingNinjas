def multiple( A):
    flag = False
    i = 1

    # for char in str(A):
    #     print(char)

    while (flag != True):


        result = A * i


        allowed_chars = set('01')
        validationString = str(result)
        # if set(validationString).issubset(allowed_chars):
        #     flag = True;
        #     break;
        # else:
        #     i = i + 1
        for char in validationString:
            if char  in ['0','1']:
                continue
            else:
                flag=True
                break
        if flag==False:
            return result
        else:
            i+=1
            flag=False




print(multiple(55))