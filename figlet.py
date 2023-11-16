import sys
from pyfiglet import Figlet


# Valida se os argumentos de linha de comando que o usuario inseriu estão corretos
if len(sys.argv) == 1:
    fonte = Figlet()
elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        try:
            fonte = Figlet(font=sys.argv[2])
        except:
            print("Invalid usage")
            sys.exit(1)
    else:
        print("Invalid usage")
        sys.exit(1)
else:
    print("Invalid usage")
    sys.exit(1)

# Recebe input do usuario e mostra na tela o resultado
texto = input("Input: ")
print("\n", fonte.renderText(texto))