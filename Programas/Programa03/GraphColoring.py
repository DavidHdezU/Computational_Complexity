import random

BOOLEAN_LIST = [True, False]
MIN_NUM_VERTICES = 10
MAX_NUM_VERTICES = 20

class Vertex(object):
    def __init__(self, id, color=None) -> None:
        self.id = id
        self.neighbours = []
        self.color = color
    
    def __str__(self) -> str:
        neighbours_ids = [v.id for v in self.neighbours]
        
        if not self.color:            
            return f"{self.id} : {neighbours_ids}"
        
        return f"{self.id} : {neighbours_ids}, color: {self.color}" 
        
    
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
        """
        Método que añade una arista entre 2 vértices a la gráfica

        Args:
            v (int): indice de la lista de vértices correspondiente al vértice v
            u (int): indice de la lista de vértices correspondiente al vértice u
        """
        self.vertices[v].neighbours.append(self.vertices[u])
        self.vertices[u].neighbours.append(self.vertices[v])
        
    def __str__(self) -> str:
        str_builder = []
        
        for v in self.vertices:
            str_builder.append(str(v))
            
        return '\n'.join(str_builder)
    
    @staticmethod
    def create_random_graph(n):
        """
        Constructor que crea una gráfica aleatoria con un número n de vértices

        Args:
            n (int): Número de vértices que tendrá la gráfica

        Returns:
            Graph: Una gráfica aleatoria con un número n de vértices
        """
        graph = Graph(n)
        
        for v in range(n):
            for u in range(v+1, n):
                if random.choice(BOOLEAN_LIST):
                    graph.add_edge(v, u)
                    
        return graph
    
    
def colore_graph(graph, k): # Fase adivinadora
    """
    Método que dado una gráfica y un entero k,
    colorea los vértices de la gráfica aleatoriamente con k colores

    Args:
        graph (Graph): Gráfica a colorear
        k (int): Número de colores a usar
    """
    colors = [i for i in range(k)]
    
    for i in range(len(graph.vertices)):
        color = random.choice(colors)
        graph.vertices[i].color = color
        
def validate_coloring(graph): # Fase verificador
    """
    Método que verifica si una gráfica ha sido coloreada de manera correcta

    Args:
        graph (Graph): Gráfica a verificar

    Returns:
        Boolean: True si la gráfica ha sido coloreada de manera correcta, False en otro caso
    """
    for v in graph.vertices:
        for u in v.neighbours:
            if v.color == u.color:
                print(f"Los vértices {v.id} y {u.id} que son vecinos tienen el mismo color asignado: {v.color}")
                return False
    
    return True
        
      
if __name__ == "__main__":
    number_vertices = random.randrange(MIN_NUM_VERTICES, MAX_NUM_VERTICES+1)   
    graph = Graph.create_random_graph(number_vertices)
    print(f"Gráfica generada con {number_vertices} vértices generada: aleatoriamente: \n\n{graph}\n")
    
    k = random.randrange(2, MAX_NUM_VERTICES+1)   # El número de colores se elige aleatoriamente el rango [2, MAX_NUM_VERTICES]
    
    colore_graph(graph, k) # Coloreamos la gráfica
    print(f"Gráfica generada coloreada con {k} colores: \n\n{graph}\n")
    
    res = validate_coloring(graph) # Validamos la gráfica
    
    if res:
        print(f"La gráfica tiene una {k}-coloración valida")
    else:
        print(f"Por lo tanto la gráfica no tiene una {k}-coloración valida")