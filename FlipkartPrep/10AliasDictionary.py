def isAlienSorted( words, order):
  dict={}
  for i,v in enumerate(order):
      dict[v]=i
  res=[]
  for word in words:
      new=[]
      for letter in word:
          new.append(dict[letter])
      res.append(new)
  print(res)
  for i in range(len(res)-1):
      if res[i]>res[i+1]:
          return False
  return True

print(isAlienSorted(["word","world","row"],  "worldabcefghijkmnpqstuvxyz"))