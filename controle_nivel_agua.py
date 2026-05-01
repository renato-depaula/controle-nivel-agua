from colorama import Fore, Style, init

init(autoreset=True)

niveis = [
    "Nível 1 - Muito baixo (Crítico)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (Alerta)"
]

def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE

for i in range(1, 6):
    cor = definir_cor(i)
    print(cor + niveis[i - 1])

print(Style.RESET_ALL)