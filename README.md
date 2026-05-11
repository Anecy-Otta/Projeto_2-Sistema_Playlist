# Projeto_2-Sistema_Playlist

Este projeto é um sistema de gerenciamento de playlist de músicas desenvolvido como requisito para a disciplina de Estrutura de Dados. O objetivo principal é aplicar conceitos de estruturas de dados lineares (Listas Encadeadas e Filas) sem o uso de estruturas prontas da linguagem.

## Funcionalidades

Atualmente, o sistema conta com as seguintes operações:
1.  **Adicionar música à biblioteca**: Cadastro de faixas com Título, Artista, Gênero e BPM.
    * Geração de ID automático e sequencial.
    * Validação rigorosa de BPM (deve ser numérico e > 0).
    * Inserção no final da lista encadeada.

## Requisitos Técnicos Implementados

-   **Classes de Dados**: `Musica`, `NodoLista` e `NodoFila`.
-   **Biblioteca**: Implementação de uma **Lista Encadeada Simples** manual.
-   **Fila de Reprodução/Histórico**: Implementação de **Fila FIFO** (First-In, First-Out) com ponteiros para início e fim.
-   **Não utilização de estruturas prontas**: Todo o gerenciamento de memória e encadeamento é feito via nós.
-   **Tratamento de Erros**: Validação de entradas para garantir a integridade dos dados.

## Estrutura do Projeto

-   `modelos.py`: Contém as definições dos objetos de dados e nós.
-   `estruturas.py`: Contém a lógica das estruturas de dados (Lista e Fila).
-   `main.py`: Interface de linha de comando para interação com o usuário.

## Como executar

Para rodar o projeto, certifique-se de ter o Python instalado e execute:

```bash
python main.py