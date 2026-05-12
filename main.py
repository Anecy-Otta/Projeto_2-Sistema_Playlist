from modelos import Musica
from estruturas import Biblioteca, Fila

def principal():
    minha_biblioteca = Biblioteca()
    fila_reproducao = Fila()
    historico = Fila() 

    while True:
        print("\n" + "="*30)
        print("MENU DA PLAYLIST")
        print("1. Adicionar música à biblioteca")
        print("2. Remover música da biblioteca")
        print("3. Buscar música na biblioteca")
        print("4. Listar todas as músicas da biblioteca")
        print("5. Montar fila de reprodução por humor (BPM)")
        print("6. Reproduzir próxima música da fila")
        print("7. Exibir fila de reprodução atual")
        print("0. Sair do programa")
        print("="*30)
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n--- Adicionar Nova Música ---")
            titulo = input("Digite o título da música: ")
            artista = input("Digite o nome do artista: ")
            genero = input("Digite o gênero musical: ")
            
            while True:
                bpm_entrada = input("Digite o BPM (maior que zero): ")
                
                if bpm_entrada.isdigit():
                    bpm = int(bpm_entrada)
                    if bpm > 0:
                        break 
                    else:
                        print("Erro: O BPM deve ser maior que zero!")
                else:
                    print("Erro: O BPM deve ser um número inteiro válido!")
            
            nova_musica = Musica(titulo, artista, genero, bpm)
            minha_biblioteca.inserir(nova_musica)
            
            print(f"\n Sucesso! A música '{nova_musica.titulo}' foi adicionada com o ID: {nova_musica.id}")

        elif opcao == "2":
            print("\n--- Remover Música ---")
            
            id_input = input("Digite o ID da música que deseja remover: ")
            
            if id_input.isdigit():
                id_para_remover = int(id_input)
                
                sucesso = minha_biblioteca.remover(id_para_remover)
                
                if sucesso:
                    print(f" Música com ID {id_para_remover} removida com sucesso!")
                else:
                    print(f" Erro: Não foi encontrada nenhuma música com o ID {id_para_remover}.")
            else:
                print(" Erro: Por favor, digite um ID numérico válido.")

        elif opcao == "3":
            print("\n--- Buscar Música ---")
            print("1. Buscar por ID")
            print("2. Buscar por Título")
            tipo_busca = input("Escolha a forma de busca (1 ou 2): ")

            if tipo_busca == "1":
                id_input = input("Digite o ID da música: ")
                if id_input.isdigit():
                    musica_encontrada = minha_biblioteca.buscar(int(id_input)) 
                    if musica_encontrada:
                        print(f"\n Encontrada: {musica_encontrada}")
                    else:
                        print("\n Nenhuma música encontrada com este ID.")
                else:
                    print(" Erro: O ID deve ser um número válido.")

            elif tipo_busca == "2":
                titulo_input = input("Digite o título da música: ")
                musica_encontrada = minha_biblioteca.buscar_por_titulo(titulo_input)
                if musica_encontrada:
                    print(f"\n Encontrada: {musica_encontrada}")
                else:
                    print("\n Nenhuma música encontrada com este título.")
            else:
                print(" Opção inválida.")

        elif opcao == "4":
            print("\n--- Biblioteca Completa ---")
            
            tem_musicas = minha_biblioteca.listar_todas()
            
            if not tem_musicas:
                print("A biblioteca está vazia no momento. Adicione algumas músicas primeiro!")

        elif opcao == "5":
            print("\n--- Montar Fila de Reprodução por Humor ---")
            print("1. Relaxar (até 80 BPM)")
            print("2. Focar (81 a 120 BPM)")
            print("3. Animar (121 a 160 BPM)")
            print("4. Treinar (acima de 160 BPM)")
            
            escolha_humor = input("Escolha o humor desejado (1 a 4): ")
            
            if escolha_humor == "1":
                bpm_min, bpm_max = 0, 80
                nome_fila = "Relaxar"
            elif escolha_humor == "2":
                bpm_min, bpm_max = 81, 120
                nome_fila = "Focar"
            elif escolha_humor == "3":
                bpm_min, bpm_max = 121, 160
                nome_fila = "Animar"
            elif escolha_humor == "4":
                bpm_min, bpm_max = 161, 9999 
                nome_fila = "Treinar"
            else:
                print("Opção inválida. Operação cancelada.")
                continue 
            
            fila_reproducao = minha_biblioteca.filtrar_por_bpm(bpm_min, bpm_max)
            
            if fila_reproducao.esta_vazia():
                print(f"\nNenhuma música na biblioteca se encaixa no humor '{nome_fila}' ({bpm_min}-{bpm_max} BPM).")
            else:
                print(f"\nFila '{nome_fila}' montada do zero com {fila_reproducao._tamanho} música(s)!")

        elif opcao == "6":
            print("\n--- Reproduzir Próxima Música ---")
            
            if fila_reproducao.esta_vazia():
                print("Erro: A fila de reprodução está vazia! Vá na Opção 5 e monte uma fila primeiro.")
            else:
                musica_atual = fila_reproducao.desenfileirar()
                
                print(f"Tocando agora: {musica_atual}")
                
                historico.enfileirar(musica_atual)

        elif opcao == "7":
            print("\n--- Fila de Reprodução Atual ---")
            
            tem_musicas = fila_reproducao.exibir_fila()
            
            if not tem_musicas:
                print("A fila de reprodução está vazia. Vá na Opção 5 para montar uma nova fila.")

        elif opcao == "0":
            print("\nEncerrando o sistema... Até logo!")
            break 
            
        else:
            print("\n Opção inválida. Tente novamente.")

if __name__ == "__main__":
    principal()