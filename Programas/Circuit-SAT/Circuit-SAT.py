import random
from collections import defaultdict

AND = 'AND'
OR = 'OR'
NOT = 'NOT'
BOOLEAN_LIST = [False, True]

class Node(object):
    def __init__(self, name, neighbours, val=None, function=None) -> None:
        self.name =  name
        self.function = function
        self.neighbours = neighbours
        self.val = val
        
    def compute_val(self): 
        val = None
        if self.function == NOT:
            val = not self.neighbours[0].val
        elif self.function == AND:
            val =self.neighbours[0].val & self.neighbours[1].val
        else:
            val = self.neighbours[0].val | self.neighbours[1].val
            
        self.val = val
        
    def __str__(self) -> str:
        if self.function:
            if self.function == NOT:
                return f"{self.name} = NOT {self.neighbours[0].name} = {self.val}"
            
            return f"{self.name} = {self.neighbours[0].name} {self.function} {self.neighbours[1].name} = {self.val}"
        
        return f"{self.name} = {self.val}"
        

class Graph(object):
    def __init__(self, node_list) -> None:
        self.level_map = defaultdict(list)
        
        for node, level in node_list:
            self.level_map[level].append(node)
                        
    def __str__(self) -> str:
        str_builder = []
        
        for i in range(len(self.level_map)):
            for node in self.level_map[i]:
                str_builder.append(('\t'*i) + str(node))
            
        return '\n'.join(str_builder)
    
    def compute_output(self): # O(n) dónde n es el número de nodos función
        for i in range(1, len(self.level_map)):
            for node in self.level_map[i]:
                node.compute_val()
                
        return self.level_map[len(self.level_map)-1][0].val
    


if __name__ == "__main__":
    node_list = []
    
    # Primero creamos los nodos de entrada
    
    for i in range(5):
        node_lvl = (Node("x"+str(i), [], random.choice(BOOLEAN_LIST)), 0)
        node_list.append(node_lvl)
        
    # Creamos los nodos correspondientes a las puertas 
    
    g1 = Node("g1", [node_list[0][0], node_list[1][0]], function=AND)
    g2 = Node("g2", [node_list[1][0], node_list[2][0]], function=OR)
    g3 = Node("g3", [node_list[3][0], node_list[4][0]], function=OR)
    g4 = Node("g4", [g1], function=NOT)
    g5 = Node("g1", [g2, g3], function=AND)
    output_node = Node("output node", [g4, g5], function=AND) # Nodo salida
    
    node_list.append((g1, 1))
    node_list.append((g2, 1))
    node_list.append((g3, 1))
    node_list.append((g4, 2))
    node_list.append((g5, 2))
    node_list.append((output_node, 3))
    
    circuit = Graph(node_list)
    
    print("El circuito que se tiene es el siguiente, donde los xi son los nodos de entrada\n\n")
    print(circuit)
    print('\n\n')
    
    output = circuit.compute_output()

    print(f"La salida que se obtiene con esta configuración es la siguiente: {output}\n\n")
    print("Ahora el circuito se ve de la siguiente manera, con todos los valores de las puertas computados:\n\n")
    print(circuit)
    
    
    #  También podriamos tratarlo como un árbol binario y realizar un recorrido post-order
