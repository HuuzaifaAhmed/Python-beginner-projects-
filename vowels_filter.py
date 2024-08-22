#vowel=["a","e","i","o","u"]

#taking input 
#b=str(input("enter alphabets by space"))#
#b=[str(x) for x in b.split()]

#filtering through loop
#for el in b:
 #   if el in vowel:
  #      print(el,"is vowel")
   # else:
    #    print(el,"is not vowel")

vowel=["a","e","i","o","u"]

a=str(input("enter alphabets : "))
a=[str(x) for x in a.split()]

for el in a:
    if el in vowel:
        print(el,"is vowel")
    else:
        print(el,"not vowel")
          
