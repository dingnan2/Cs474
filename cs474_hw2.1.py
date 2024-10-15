from z3 import *

p = Bool('p')
q = Bool('q')

formula = And(p, Or(Not(p), q), Not(q))

solver = Solver()
solver.add(formula)
result = solver.check()

if result == unsat:
    print("The formula is valid.")
    print("Negation is unsatisfiable, hence the original formula is valid.")
else:
    print("The formula is not valid.")
    print("The negation is satisfiable, so the original formula is not valid.")


