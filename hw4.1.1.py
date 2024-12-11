from z3 import *
e,e_prime,x = Consts('e e_prime x', IntSort())
f = Function('f', IntSort(), IntSort(), IntSort())
identity_e = ForAll(x, And(f(x, e) == x, f(e, x) == x))
identity_e_prime = ForAll(x, And(f(x, e_prime) == x, f(e_prime, x) == x))
not_equal = e != e_prime
negation = And(identity_e, identity_e_prime, not_equal)
solver = Solver()
solver.add(negation)
result = solver.check()
if result == z3.sat:
    print("The formula is satisfiable, so the identity element is not unique.")
else:
    print("The formula is unsatisfiable, so the identity element is unique under group axioms.")
