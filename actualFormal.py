#default 
def add(a, *b):

      c=a
  
      for i in b:
            c=c+i
      print(c)


add(1,2,3,4,5)


#keyword variable
def person(name,**data):
   print(name)

   for i,j in data.items():
        print(i,j)


person('rima',age=90,city='mumbai',mob=908)








