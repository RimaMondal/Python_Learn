def greet():
    print('hello')
    print('good night')


greet()

def add(x,y):
  c=x+y
  print(c)

add(2,3)



def add2(x,y):
    c=x+y
    return c
result= add2(4,5)
print(result)

#one functions multiple value
def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d

result,result2=add_sub(5,4)
print(result,result2)




