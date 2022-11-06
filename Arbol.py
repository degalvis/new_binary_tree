from Nodo import Nodo


class Arbol:
    def __init__(self, data):
        self.raiz = Nodo(data)
        
    def insertarRecursivo(self, nodo, data):
        if self.raiz == None:
            self.raiz = Nodo(data)
        else:
            if data > nodo.data:
                if nodo.der == None:
                    nodo.der = Nodo(data)
                else:
                    self.insertarRecursivo(nodo.der, data)
            elif data < nodo.data:
                if nodo.izq == None:
                    nodo.izq = Nodo(data)
                else:
                    self.insertarRecursivo(nodo.izq, data)
            else:
                return
    
    def insertar(self, data):
        self.insertarRecursivo(self.raiz, data)
      
    def insertarSubT(self, arbol):
        self.insertarSubTRecursivo(self.raiz, arbol)
            
    def insertarSubTRecursivo(self, nodo, arbol):
        if nodo == None:
            return
        else:
            if nodo.subT == None:
                nodo.subT = arbol
            else:
                self.insertarSubTRecursivo(nodo.izq, arbol)
                self.insertarSubTRecursivo(nodo.der, arbol)
        
    def insertarPagesRecursivo(self, nodo, arbol):
        if nodo == None:
            return
        else:
            if nodo.pages == None:
                nodo.pages = arbol
            else:
                self.insertarSubTRecursivo(nodo.izq, arbol)
                self.insertarSubTRecursivo(nodo.der, arbol)
    
    def insertarPages(self, arbol):
        self.insertarPagesRecursivo(self.raiz, arbol)
    
    def imprimir(self):
        self.imprimirRecursivo(self.raiz)
        
    def imprimirRecursivo(self, nodo):
        if nodo != None:
            self.imprimirRecursivo(nodo.izq)
            print("")
            print(nodo.data)
            self.imprimirSubTRecursivo(nodo.subT)
            self.imprimirRecursivo(nodo.der)
        else:
            return
        
    def imprimirSubTRecursivo(self, arbol):
        if arbol != None:
            self.imprimirSubTotalRecursivo(arbol.raiz.izq)
            print(arbol.raiz.data)
            self.imprimirSubTotalRecursivo(arbol.raiz.der)
        else:
            return
            
    def imprimirSubTotalRecursivo(self, nodo):
        if nodo != None:
            self.imprimirSubTotalRecursivo(nodo.izq)
            print(nodo.data)
            self.imprimirSubTotalRecursivo(nodo.der)   
        else:
            return    
