#import array as arr

print("Hello world")
#import array as arr
from array import *
vals= array('i',[1,2,3])
#vals.reverse()
print(vals)
print(vals.buffer_info())
newarr =array(vals.typecode,  (a*a for a in vals))
for e in newarr:
  print(e)
