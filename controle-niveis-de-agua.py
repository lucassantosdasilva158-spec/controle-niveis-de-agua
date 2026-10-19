# Extensão utilizada para atribuir cores ao terminal, tornando a visualização mais intuitiva e agradável

from colorama import Fore, Style, init

init(autoreset=True)

# Cores usadas para representar os níveis de água do reservatório

print("Operador, estas são as cores das bandeiras que representam os níveis de água do reservatório:")

print(Fore.RED + "Bandeira Vermelha: estado crítico!")
print(Fore.YELLOW + "Bandeira Amarela: nível baixo!")
print(Fore.GREEN + "Bandeira Verde: níveis aceitáveis!")
print(Fore.CYAN + "Bandeira Ciano: nível alto!")
print(Fore.BLUE + "Bandeira Azul: alerta de transbordamento!")

# Lista de níveis de água do reservatório, representando diferentes estados de alerta

niveis = [
    "bandeira Vermelha, estado crítico",                             # Índice 0 (Nível 1)
    "bandeira Amarela, abaixo do esperado",                          # Índice 1 (Nível 2)
    "bandeira Verde, níveis aceitáveis",                             # Índice 2 (Nível 3)
    "bandeira Ciano, reservatório cheio",                            # Índice 3 (Nível 4)
    "bandeira Azul, estado de alerta para risco de transbordamento"  # Índice 4 (Nível 5)
]

# Essa função será responsável por atribuir a cor da bandeira com base nos níveis de água do reservatório

def bandeira(nivel):
    """
    Essa função irá receber os níveis da água e atribuir a bandeira correta com base em seu nível
    """
    # Verifica se o nível digitado é válido (entre 1 e 5)

    if 1 <= nivel <= 5:

        # Define a cor de acordo com o nível

        if nivel == 1:
            cor = Fore.RED
        elif nivel == 2:
            cor = Fore.YELLOW
        elif nivel == 3:
            cor = Fore.GREEN
        elif nivel == 4:
            cor = Fore.CYAN
        elif nivel == 5:
            cor = Fore.BLUE

        # Puxa a situação direto da lista (subtrai 1 porque as listas começam no índice 0)

        situacao = niveis[nivel - 1]
        return f"{cor}O reservatório está na {situacao}{Style.RESET_ALL}"
    
# Uso da função para estabelecer o nível do reservatório e encontrar sua bandeira

print("Bem-vindo, operador! Vamos verificar o nível do reservatório e a bandeira correspondente.")

operador = input("Primeiramente, digite o seu nome: ")

nivel_da_agua = int(input(f"Operador {operador}, digite o nível do reservatório (1 a 5): "))

# Caso o valor digitado seja invalido, o programa solicitará que o operador digite novamente até que seja fornecido um valor valido

while nivel_da_agua < 1 or nivel_da_agua > 5:
    print(Fore.WHITE + "Nível inválido! Digite um valor entre 1 e 5." + Style.RESET_ALL)
    nivel_da_agua = int(input("Digite novamente o nível do reservatório (1 a 5): "))

# Resultado da nossa função será exibido no terminal

resultado_final = bandeira(nivel_da_agua)

print(resultado_final)