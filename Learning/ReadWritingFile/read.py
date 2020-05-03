import re
pattern=re.compile(r'abc')

def writingfunction(n):
    with open("readFile", 'r') as ra:
        with open("writefile", 'w')as wf:
            for line in ra:
                if "simnow" in line:
                    line=line.rstrip('\n')+' '+n

                    wf.write(line)
                    wf.write('\n')
                else:
                    wf.write(line)
print("Enter stirng to enter")
n=input()
writingfunction(n)
