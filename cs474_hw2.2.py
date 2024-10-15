from z3 import *

p = Bool('p')
q = Bool('q')
r = Bool('r')

#original formula
phi1 = And(Or(q, Not(r)), Or(Not(p), r), Or(Not(q), r, p))
phi = And(phi1, Or(p, q, Not(q)), Or(Not(r), q))

solver_phi = Solver()
solver_phi.add(phi)

if solver_phi.check() == sat:
    print("The formula φ is satisfiable.")
else:
    print("The formula φ is not satisfiable.")


psi1 = And(Or(q, Not(r)), Or(Not(p), r), Or(Not(q), r, p))
psi = And(psi1, Or(p, q, Not(q)), Or(Not(r), q), q, r, Or(p,r))
solver_psi  = Solver()
solver_psi.add(psi)
if solver_psi.check() == sat:
    print("The final set of clauses ψ is satisfiable.")
else:
    print("The final set of clauses ψ is not satisfiable.")

print("Check if φ and ψ are equivalent: ")
if solver_phi.check() == solver_psi.check():
    print("     φ and ψ are equivalent.")
else:
    print("     φ and ψ are not equivalent")