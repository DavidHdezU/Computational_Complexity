class SubSetSumAprox():
    def __init__(self, S, t, epsilon) -> None:
        self.S = S
        self.t = t
        self.epsilon = epsilon
        self.curr_solution = [0]
    
    def __createLplusS(self, x):
        """
        Crea la lista L_(i-1) + xi

        Args:
            x (int): El elemento xi de el conjunto de entrada S

        Returns:
            List: La lista L_(i-1) + xi
        """
        return [i + x for i in self.curr_solution]
    
    def __removeElementesGreaterThanT(self):
        """
        Quita de la lista Li los elementos que son mayores a t  
        """
        self.curr_solution = [x for x in self.curr_solution if x <= self.t]
        
    def __merge(self, new_L):
        """
        Merge usado en MergeSort para hacer el merge de 2 listas,
        en este caso el de L_(i-1) y L_(i-1) + xi

        Args:
            new_L (List): Lista con la cual se hará el merge

        Returns:
            List: La nueva lista después de haber hecho el merge de ambas listas
        """
        res = []
        
        i, j = 0, 0
        
        while i < len(self.curr_solution) and j < len(new_L):
            if self.curr_solution[i] < new_L[j]:
                res.append(self.curr_solution[i])
                i += 1
            else:
                res.append(new_L[j])
                j += 1
                
        while i < len(self.curr_solution):
            res.append(self.curr_solution[i])
            i += 1
            
        while j < len(new_L):
            res.append(new_L[j])
            j += 1
            
        return res
    
    def __trim(self, Li):
        """
        Función que aplica la función Trim descrita en el libro

        Args:
            Li (List): Lista a la cual se le aplicará el Trim

        Returns:
            List: Lista después de habersele aplicado el Trim
        """
        delta = self.epsilon / (2*len(self.S))
        
        L = [Li[0]]
        last = L[0]
        
        for i in range(1, len(Li)):
            if Li[i] > last * (1 + delta):
                L.append(Li[i])
                last = Li[i]
                
        return L
    
    
    def sub_set_sum_Aprox(self):
        """
        Función que aplica el algoritmo de aproximación de Sub Set Sum

        Returns:
            int: El resultado aproximado que regresa el algoritmo
        """
        for i in range(len(self.S)):
            LiPlusXi = self.__createLplusS(self.S[i])
            
            Li = self.__merge(LiPlusXi)
            Lj = self.__trim(Li)
            
            self.curr_solution = Lj
            self.__removeElementesGreaterThanT()
            
        return self.curr_solution[-1]
    
    
if __name__ == "__main__":
    subSetSumAprox = SubSetSumAprox(S = [104, 102, 201, 101], t = 308, epsilon = 0.40)
    print(f"Para el ejemplar\n S = {subSetSumAprox.S}\t t = {subSetSumAprox.t}\t epsilon = {subSetSumAprox.epsilon}")
    res = subSetSumAprox.sub_set_sum_Aprox()
    print(f"El resultado aproximado obtenido es: {res}")