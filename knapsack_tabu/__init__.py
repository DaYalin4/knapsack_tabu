""" Clase principal para el problema de la mochila """

class ProblemaMochila:
    def __init__(self, ítems, utilidades, pesos, límite):
        self.ítems = ítems
        self.utilidades = np.array([list(utilidades.values())[i] for i in range(len(utilidades))])
        self.pesos = np.array([list(pesos.values())[i] for i in range(len(pesos))])
        self.límite = límite
        self.num_items = len(self.ítems)

    def vector_ítems(self, vector):
        return [self.ítems[i] for i in range(len(vector)) if vector[i] == 1]

    def vector_utilidades(self):
        return np.array([list(self.utilidades.values())[i] for i in range(len(self.utilidades))])

    def vector_pesos(self):
        return np.array([list(self.pesos.values())[i] for i in range(len(self.pesos))])

    def generar_solucion_aleatoria(num_items):
        return np.array([random.randint(0, 1) for _ in range(self.num_items)])

    def mejor_cambio(self, indices, v_actual):
        i_best = indices[0]
        u_best = (self.utilidades[0]/self.pesos[0])**(v_actual[0])
        for i in indices:
            u_i = (self.utilidades[i]/self.pesos)**(v_actual[i])
            if u_i > u_best:
                i_best = i
        return i_best
    
    def utilidad(self, vector):
        return self.utilidades.dot(vector)
    
    def tabu_search(self, capacidad_mochila, max_iter=20, L=8):
        tabu_list = []
        c = 1
        X = generar_solucion_aleatoria(self.num_items)
        Curl_W = X_best.dot(self.pesos)
        X_best = X
        while c<=max_iter:
            N = [i for i in range(num_items)]
            start = max([0, c-L])
            for i in range(start, c)
                N = N.remove(tabu_list[i])
            for i in N:
                if (X[i] == 0) and (Cur_W + self.pesos[i] > capacidad_mochila):
                    N = N.remove(i)
            if len(N) != 0:
                i_posible = mejor_cambio(N, X)
                tabu_list.append(i_posible)
                X[i_posible] = 1-X[i_posible]
                if X[i_posible] == 1:
                    Curl_W = Curl_W + self.pesos[i_posible]
                else:
                    Curl_W = Curl_W - self.pesos[i_posible]
            if utilidad(X) > utilidad(X_best):
                X_best = X
            c += 1
        return X_best
                
                

    
