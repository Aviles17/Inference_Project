from logical_motor import *

A = Symbol("Mañana hara sol")
B = Symbol("Mañana llovera", False)
NO_A = No(A).create_symbol()
C = No(No(A).create_symbol()).create_symbol()
A_CONDITION_B = Condicional(A, No(B).create_symbol())
or_state = Or(A, B, NO_A, C)

print(f"{A_CONDITION_B.create_symbol().sentence}, {A_CONDITION_B.create_symbol().value}")
print(f"{A} OR {B}")
print(f"{A.value} OR {NO_A.value}")
print(f"{or_state} | {or_state.evaluar()}")
print(f"{A.value} | {C.value}")
print(A == B)
print(A == No(NO_A).create_symbol())
print(A.value == NO_A.value)