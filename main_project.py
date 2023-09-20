from logical_motor import *
'''
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
'''

def main():
    #Solucionar teorema por refutación, Teorema: Dado que (A -> B and B -> C) -> A -> C , C es falso?
    A = Symbol("A")
    B = Symbol("B")
    C = Symbol("C")
    Knowledge_list = []
    Cond = Condicional(A, B)
    
    Knowledge_list.append(Cond)
    
    Cond = Condicional(B, C)
    
    Knowledge_list.append(Cond)
    
    Cond = Condicional(A, C)
    
    Knowledge_list.append(Cond)
    
    
    Query = No(C).create_symbol()
    
    evaluation_query = Condicional(B, Query)
    
    #Encontrar incongruencia con la base de conocimiento
    for knowledge in Knowledge_list:
        if knowledge.create_symbol() == No(evaluation_query.create_symbol()).create_symbol():
            solution = False
            break
        elif knowledge.create_symbol() == evaluation_query.create_symbol():
            solution = True
        else:
            solution = None
    print(f"Solution: {solution}")
            
            
            
        
    
    
    

if __name__ == "__main__":
    main()