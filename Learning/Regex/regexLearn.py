import re
# print("\tnidhish")
# #using raw string
# print(r"\tnidhish")

pattern=re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
pattern=re.compile(r'[25]22[*.-]\d\d\d[*.-]\d\d\d\d')   #[25]  means either of 2 or 5  [*.-] same goess for these sign
pattern=re.compile(r'[2-5]')  #matching all those containing letters
pattern=re.compile(r'[a-zA-Z]')  # matches those containing a-z or A-Z
pattern=re.compile(r'[^a-zA-Z]')  # not including a-z and A-Z
pattern=re.compile(r'[^b]at')   # all three letter word ending with at not beginning with b

#Quantifiers
pattern=re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
#or
pattern=re.compile(r'\d{3}.\d{3}.\d{4}')   # same as above
pattern=re.compile(r'Mr\.?\s[A-Z]\w*')
pattern=re.compile(r'M(r|s|rs)(.|\s|.\s)[A-Z]\w*')# including all names
pattern=re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')  # including all characters
pattern=re.compile(r'[C][A-Za-z]\w*\@[a-zA-Z]+\.com')#including first email
pattern=re.compile(r'[a-zA-Z]+@[a-zA-Z]+\.com')  #getting 1st email
pattern=re.compile(r'[a-zA-Z.]+@[a-zA-Z]+\.(com|edu)')#getting 1st and 2nd email
pattern=re.compile(r'[a-zA-Z.0-9-]+@[a-zA-Z-]+\.(com|edu|net)')#getting all the 3 emails together
pattern=re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+') #same as above ,learn to read as well


urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''
#Capture information from group (from url)
#pattern=re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
#sub_urls = pattern.sub(r'\2\3',urls)
#print(sub_urls)

#sentence='Give me time'
#pattern=re.compile(r'^G[A-Za-z]*\s[a-z]*\s[a-z]*')
#pattern=re.compile(r'\d{3}-\d{3}-\d{4}')
#match=pattern.finditer(sentence)
#for m in match:
#    print(m.group(0))
#pattern=re.compile(r'M(rs|s|.|s.|r|r).?(\s)[a-zA-Z]*')
#pattern=re.compile(r'M(r|s|rs)(.|\s|.\s)[A-Z]\w*')
with open('data.txt') as f :
    content=f.read()
    #match=pattern.finditer(content)
    match=pattern.finditer(content) #using findall functinality
    for m in match:
        print(m.group(0))
        break
        #print(m.group(2))
