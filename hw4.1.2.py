from z3 import *
a, b, c, e = Consts('a b c e', IntSort())
f = Function('f', IntSort(), IntSort(), IntSort())  
identity = ForAll(a, And(f(a, e) == a, f(e, a) == a))
associativity = ForAll([a, b, c], f(f(a, b), c) == f(a, f(b, c)))
negation = And(
    And(f(a, b) == e, f(b, a) == e),  
    And(f(a, c) == e, f(c, a) == e),  
    b != c                           
)
s = Solver()
s.add(identity, associativity, negation)
if s.check() == sat:
    print("The formula is satisfiable, so an element has more than one inverse.")
else:
    print("The formula is unsatisfiable, so every element has only one inverse.")
