from z3 import *

l1, u1, l2, u2= Reals('l1 u1 l2 u2')
z, w = Reals('z w')

inequality = Or(z < w, w < z)
right_inner = And(l1 < w, w < u1, l2 < w, w < u2, inequality)
left = And(l1 < z, z < u1, l2 < z, z < u2)
phi = ForAll(z, Implies(left, Exists(w, right_inner)))

qf = Tactic('qe')(phi).as_expr()
print("Quantifier-free formula is:", qf)
