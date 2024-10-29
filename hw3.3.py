from z3 import *

x = Real('x')
y = Real('y')
left = 2*y > 3*x 
right = 4*y < (8*x+10)
phi = ForAll(x, Exists(y, And(left, right)))
solver = Solver()
solver.add(Not(phi))
if solver.check() == sat:
    print("The formula is valid.")
else:
    print("The formula is not valid.")