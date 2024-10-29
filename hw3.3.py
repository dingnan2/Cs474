from z3 import *

l1, u1 = Reals('l1 u1')
l2, u2 = Reals('l2 u2')
l3, u3 = Reals('l3 u3')
l4, u4 = Reals('l4 u4')

solver = Solver()
edges = And(l1 < u2, l2 < u1, l2 < u3, l3 < u2, l3 < u4, l4 < u3,l4 < u1, 
            l1 < u4 )
not_edges = And(Not(And(l1 < u3, l3 < u1)), Not(And(l2 < u4, l4 < u2)))

alpha_G = And(edges, not_edges)
solver.add(Not(Exists([l1, u1, l2, u2, l3, u3, l4, u4], alpha_G)))
if solver.check() == sat:
    print("The formula is satisfiable.")
else:
    print("The formula is unsatisfiable.")
