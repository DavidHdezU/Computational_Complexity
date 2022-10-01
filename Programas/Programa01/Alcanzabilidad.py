import random

BOOLEAN_LIST = [True, False]
MIN_NUM_VERTICES = 10
MAX_NUM_VERTICES = 20

class Vertex(object):
    def __init__(self, id) -> None:
        self.id = id
        self.neighbours = []
    
    def __str__(self) -> str:
        neighbours_ids = [v.id for v in self.neighbours]
        
        return f"{self.id} : {neighbours_ids}"
    
    def __eq__(self, u)  -> None:
        if isinstance(u, Vertex):
            return self.id == u.id
        
        return False
    
    
class Graph(object):
    def __init__(self, n) -> None:
        self.vertices = []
        
        for i in range(n):
            self.vertices.append(Vertex(i))
            
    def add_edge(self, v, u) -> None:
        self.vertices[v].neighbours.append(self.vertices[u])
        self.vertices[u].neighbours.append(self.vertices[v])
        
    def __str__(self) -> str:
        str_builder = []
        
        for v in self.vertices:
            str_builder.append(str(v))
            
        return '\n'.join(str_builder)
    
    @staticmethod
    def create_random_graph(n):
        graph = Graph(n)
        
        for v in range(n):
            for u in range(v+1, n):
                if random.choice(BOOLEAN_LIST):
                    graph.add_edge(v, u)
                    
        return graph
    
    

def reachability(s, t, graph):   
    current_node = graph.vertices[s.id]
     
    path = [current_node]
    seen = set([current_node.id])
    
    while graph.vertices[current_node.id].neighbours and current_node != t:
        while current_node in path:
            seen.add(current_node.id)
            current_node = random.choice(graph.vertices[current_node.id].neighbours)
            
            if len(seen) >= len(graph.vertices[current_node.id].neighbours):  # Usamos esto como primitva nd
                break
        
        if current_node not in path:
            path.append(current_node)
            seen.clear()
        
        if len(seen) >= len(graph.vertices[current_node.id].neighbours): # Usamos esto como primitva nd
            break
            
    return t == path[-1], [v.id for v in path]

if __name__ == "__main__":
    number_vertices = random.randrange(MIN_NUM_VERTICES, MAX_NUM_VERTICES+1)    
    graph = Graph.create_random_graph(number_vertices)
    print(f"Gráfica generada con {number_vertices} vértices generada: aleatoriamente: \n\n{graph}")
    
    s = random.choice(graph.vertices)
    t = random.choice(graph.vertices)
    
    while s == t: # Evitamos que sean el mismo
        t = random.choice(graph.vertices)
        
    print("-"*40)
    print("ALCANZABILIDAD")
        
    print(f"Nodo s = {s.id}")
    print(f"Nodo t = {t.id}")
    
        
    output, path = reachability(s, t, graph)
    
    print(f"\nEl candidato propuesto es: \n{path}")
    print("\n")
    
    if output:
        print("El candidato propuesto sí es solución")
    else:
        print("El candidato propuesto no es solución")
