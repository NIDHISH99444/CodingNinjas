def runLengthEncoding(string):
    rptr,wptr=0,0
    char,f="",0
    while rptr<len(string):
        char=string[rptr]
        f=0
        while rptr<len(string) and char==string[rptr]:
            rptr+=1
            f+=1
        string[wptr]=char
        wptr+=1
        if f>1:
            for ch  in  str(f):
                string[wptr]=ch
                wptr+=1
    return string[:wptr]

print(runLengthEncoding(["a","a","b","b","c","c","c","c","c","c","c","c","c","c","c","c","c","c","c"]))