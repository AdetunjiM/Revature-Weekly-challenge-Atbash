

alpha= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

alphacaps=[]

for x in alpha:
      new=x.upper()
      alphacaps.append(new)


def atbash(word):
      result=""
      for x in range(len(word)):
            if word[x].isupper():
                  for y in range(25):
                        new=""
                        if word[x] == alphacaps[y]:
                              new= alphacaps[25-y]
                              result= result+new
            elif word[x].islower():
                  for z in range(25):
                        if word[x]== alpha[z]:
                              new = alpha[25-z]
                              result = result + new
            else :
                  new = word[x]
                  result = result +new
      return result

test0="apple"
test1 =  "Hello world!"
test2 = "Christmas is the 25th of December"


print(atbash(test0))
print(atbash(test1))
print(atbash(test2))

