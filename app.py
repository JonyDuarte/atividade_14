# Importar módulo
from equacoes import *
import time
import os
# programa principal
if __name__ =='__main__':
    while True:
        print('''
              [0] - Sair do programa.
              [1] - Calcular equação do primeiro grau.
              [2] - Calcular equação do segundo grau.
              ''')
        
        opcao = input("Opção desejada: ")
        os.system("cls")

        match opcao:
            case "0":
                print("Saindo do programa...")
                time.sleep(1.5)
                break
            case "1":
                try:
                    a = float(input("Informe o valor de 'a': ").replace(",","."))
                    b = float(input("Informe o valor de 'b': ").replace(",","."))
                    print(f"Valor de x: {primeiro_grau(a, b)}.")
                except Exception as e:
                    print(f"Não foi possível calcular a equação do primeiro grau. {e}")
                finally:
                    continue
            
            case "2":
                try:
                    a = float(input("Informe o valor de 'a': ").replace(",","."))
                    b = float(input("Informe o valor de 'b': ").replace(",","."))
                    c = float(input("Informe o valor de 'c': ").replace(",","."))

                    # armazena os valores da função  em uma lista
                    resultados = segundo_grau(a, b, c)

                    # Imprime os resultados na tela
                    for resultado in resultados:
                        print(resultado)
                except Exception as e:
                    print(f"Não foi possível calcular a equação do segundi grau. {e}")
                finally:
                    continue
            case _:
                print("Opção inválida.")
                continue

                  

