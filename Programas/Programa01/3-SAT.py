import random
from collections import defaultdict
import string
from xmlrpc.client import Boolean

BOOLEAN_LIST = [True, False]
NUM_VAR = 10
NUM_CLAUSULAS = 5



class Variable(object):
    def __init__(self, id, valor, neg) -> None:
        self.id = id
        self.valor = valor if not neg else not valor
        self.neg = neg
        
    def __str__(self) -> str:
        s = "~" if self.neg else ""
        val = 'T' if self.valor else "F"
        
        return s + self.id + "(" + val + ")"
    
class Clause(object):
    def __init__(self, variables, neg) -> None:
        self.variables = variables
        self.neg = neg
        
    def add_variable(self, var) -> None:
        self.variables.append(var)
        
    def __str__(self) -> str:
        str_builder = ' V '.join([str(v) for v in self.variables])
        str_builder.rstrip(' V ')
        
        if self.neg:
            return "~(" + str_builder + ")"
        
        return "(" + str_builder + ")"
    
    def get_valor(self) -> Boolean:
        evaluation = self.variables[0].valor
        
        for var in self.variables[1:]:
            evaluation |= var.valor
            
        return evaluation if not self.neg else not evaluation
    

def create_random_clauses(list_chars, num_clauses):
    aux_dict = {c : set() for c in list_chars}
    clauses = []
    
    val_variables = {}
    
    for _ in range(num_clauses):
        neg = random.choice(BOOLEAN_LIST)
        clauses.append(Clause([], neg))
        
    for i in range(len(clauses)):
        for _ in range(3):
            c = random.choice(list_chars)
            
            while i in aux_dict[c]:
                c = random.choice(list_chars)
                
            aux_dict[c].add(i)
            
            val = random.choice(BOOLEAN_LIST)
            neg = random.choice(BOOLEAN_LIST)
            
            if c in val_variables:
                clauses[i].add_variable(Variable(c, val_variables[c], neg))
            else:
                clauses[i].add_variable(Variable(c, val, neg))
                val_variables[c] = val
                
    return clauses

def evaluate_3sat(clauses):
    evaluation = clauses[0].get_valor()
    
    for clause in clauses[1:]:
        evaluation &= clause.get_valor()
        
    return evaluation


if __name__ == "__main__":
    chars = random.choices([c for c in "abcdefghijklmnñopqrstuvwxyz"], k=NUM_VAR)
    
    clauses = create_random_clauses(chars, NUM_CLAUSULAS)
    print("-"*40)
    print("3-SAT\n\n")
    print("Candidato propuesto:")
    
    for clause in clauses:
        print(clause)
        
    output = evaluate_3sat(clauses)
    
    if output:
        print("\nEl candidato propuesto sí es solución")
    else:
        print("\nEl candidato propuesto no es solución")

            
            

    
    
    
    
    
        