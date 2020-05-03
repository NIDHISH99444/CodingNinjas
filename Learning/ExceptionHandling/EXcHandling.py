#Exception Handling

# try:
#     pass
# except Exception:
#     pass
# else:
#     pass
# finally:
#     pass
try:
    f=open("abc",'r')   # if some exception is thrown ,may be file is not present
    #var=bad_var
    if f.name=='abc':
            raise Exception    # if you want to raise the exception

except FileNotFoundError  as e :  # put specific exception
    print(e)
except Exception as e :
    print("Inside general Exception ")
    print(e)
else:                       # this block comes when we doesnt throw any exception
    print(f.read())
    f.close()
finally:
    print("This block will be executed every time ")   #this will execute in case of  exeption or not an exception





