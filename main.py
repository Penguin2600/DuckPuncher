from DuckPuncher import someclass

#Singleton A object
A = someclass.A()

#Run some of A's normal functions
print "==Unpatched=="
print A.print_val()
print someclass.a_func("test", 0).print_val()

#Import PatchedA and rerun to compare
print "==Patched=="
from DuckPuncher import duckpunch
print A.print_val()
print someclass.a_func("test", 6).print_val()
