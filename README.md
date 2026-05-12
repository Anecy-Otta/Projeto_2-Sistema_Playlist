# Projeto_2-Sistema_Playlist

Este projeto é um sistema de gerenciamento de playlist de músicas desenvolvido como requisito para a disciplina de Estrutura de Dados. O objetivo principal é aplicar conceitos de estruturas de dados lineares (Listas Encadeadas e Filas) sem o uso de estruturas prontas da linguagem.

## Funcionalidades

O sistema interativo de linha de comando conta com 10 operações principais:

1.  **Adicionar música à biblioteca**: 
    * Cadastro de faixas com Título, Artista, Gênero e BPM.
    * Geração de ID automático, sequencial e não reutilizável.
    * Validação rigorosa de BPM (deve ser numérico e > 0).
    * Inserção no final da lista encadeada.

2. **Remover música da biblioteca**: 
   * Busca por ID e remoção lógica do nó, reorganizando os ponteiros da lista e ativando o Garbage Collector do Python.

3. **Buscar música**: 
   * Busca Linear pelo ID ou pelo Título.

4. **Listar biblioteca completa**: 
   * Percorre a lista encadeada do `inicio` ao fim.

5. **Montar fila de reprodução por humor**: 
   * Monta uma nova estrutura baseada em Fila (Queue FIFO) através da filtragem de BPM da Biblioteca.
   * A cada execução, limpa referências da fila anterior e remonta a estrutura do zero para os humores: Relaxar (≤80), Focar (81-120), Animar (121-160) e Treinar (>160).

6. **Reproduzir próxima música**: 
   * Retira a música do topo da fila atual (`dequeue`) e a insere imediatamente em uma fila independente de histórico (`enqueue`), com tratamento para evitar erros de "fila vazia".

7. **Exibir fila de humor**: 
   * Travessia *read-only* (apenas leitura) dos nós da fila atual, exibindo a ordem sem alterar os ponteiros de frente e fim.

8. **Exibir histórico de reproduções**: 
   * Reutiliza a lógica de travessia para listar as músicas já tocadas em ordem cronológica a partir da fila FIFO de histórico.

9. **Estatísticas do sistema**: 
   * Painel de controle que exibe o total de músicas na biblioteca (via travessia) e a volumetria dinâmica das filas.

10. **Sair**: 
   * Encerra o laço do sistema de forma segura.

## Requisitos Técnicos Implementados

-   **Classes de Dados**: `Musica`, `NodoLista` e `NodoFila`.
-   **Biblioteca**: Implementação de uma **Lista Encadeada Simples** manual.
-   **Fila de Reprodução/Histórico**: Implementação de **Fila FIFO** (First-In, First-Out).
-   **Não utilização de estruturas prontas**: Todo o gerenciamento de memória e encadeamento é feito via nós.
-   **Tratamento de Erros**: Validação de entradas para evitar quebra do sistema.

## Estrutura do Projeto

-   `modelos.py`: Contém as definições dos objetos de dados e nós.
-   `estruturas.py`: Contém a lógica das estruturas de dados
-   `main.py`: Interface de linha de comando.

## Como executar

Para rodar o projeto, certifique-se de ter o Python instalado e execute:

```bash
python main.py