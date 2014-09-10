import pickle
from classes import *

print C.__mro__
print D.__mro__

c=C()
d=D()

pickle.dump(c,open( "c.p", "wb" ))
pickle.dump(d,open( "d.p", "wb" ))
