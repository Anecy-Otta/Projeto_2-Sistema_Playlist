from modelos import Musica
from estruturas import Biblioteca

def principal():
    minha_biblioteca = Biblioteca()

    while True:
        print("\n" + "="*30)
        print("MENU DA PLAYLIST")
        print("1. Adicionar música à biblioteca")
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

        elif opcao == "0":
            print("\nEncerrando o sistema... Até logo!")
            break 
            
        else:
            print("\n Opção inválida. Tente novamente.")

if __name__ == "__main__":
    principal()