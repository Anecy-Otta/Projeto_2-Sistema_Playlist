from modelos import NodoLista, NodoFila

class Biblioteca:
    def __init__(self):
        self.inicio = None 

    def inserir(self, musica):
        """Adiciona uma música sempre no final da lista."""
        novo_nodo = NodoLista(musica)
        
        if self.inicio is None:
            self.inicio = novo_nodo
        else:
            atual = self.inicio
            while atual.proximo is not None:
                atual = atual.proximo
            
            atual.proximo = novo_nodo

    def buscar(self, id_musica):
        """Percorre a lista procurando uma música pelo ID."""
        atual = self.inicio
        while atual is not None:
            if atual.musica.id == id_musica:
                return atual.musica 
            atual = atual.proximo
        return None 

    def remover(self, id_musica):
        """Remove uma música da lista baseada no ID."""
        atual = self.inicio
        anterior = None
        
        while atual is not None:
            if atual.musica.id == id_musica:
                if anterior is None:
                    self.inicio = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                return True 
            
            anterior = atual
            atual = atual.proximo
            
        return False 
    
class Fila:
    def __init__(self):
        self.frente = None
        self.fim = None
        self._tamanho = 0 

    def esta_vazia(self):
        return self.frente is None

    def enfileirar(self, musica):
        """Adiciona uma música ao fim da fila (enqueue)."""
        novo_nodo = NodoFila(musica)
        if self.esta_vazia():
            self.frente = novo_nodo
            self.fim = novo_nodo
        else:
            self.fim.proximo = novo_nodo
            self.fim = novo_nodo
        self._tamanho += 1

    def desenfileirar(self):
        """Remove e retorna a música da frente da fila (dequeue)."""
        if self.esta_vazia():
            return None
        
        musica = self.frente.musica
        self.frente = self.frente.proximo
        
        if self.frente is None:
            self.fim = None
            
        self._tamanho -= 1
        return musica