
"""
MEMBROS DO GRUPO 17

Camilo Augusto Borges Caballero
Cesar Cunha Ziobro
Enzo Bloss Stival
Lucas Philippe Nunes de Lima
Rafael Schmitz Herdt                                        
                                                  
                              /                   
                             @@%.                 
                       ,@@@@@@@@@@@@@@            
                 @@@@@@@@@@@@@@@@@                
                    ,&&. *..*@&@@                 
                   @@@  /@@@  @@@                 
                  .@@@  *@@&  @@@,                
                    @@@@@@@@@@@@/                 
                     @@@@@@@@@@*                  
                      @@@@@@@@@                   
                      @@@@@@@@@,                  
                     %@@@@@@@@@(                  
                   #@@@@@@@@@@@@@@                
                 &@@@@@#     &@@@@@@              
               ,@@@@@           ,@@@@/            
               @@@@.               @@@            
              (@@@                   @@           
            .@@                                   
                                        

"""

from menus_calculadora import menu_inicial, menu_bases1, menu_bases2, menu_soma, menu_subtracao



while True:
    menu_inicial()
    escolha = int(input("Escolha um opção: "))

    if escolha == 1:

        menu_bases1()
        base = int(input("insira a base do valor inicial: "))

        menu_bases2()
        base_converter = int(input("insira a base para a qual quer converter: "))

        if base == base_converter:
            print("Você quer converter para a mesma base? Sinto muito mas não fazemos isso aqui nao amigão")

        elif base == 1: # Conversão de base decimal

            valor = int(input("Qual o valor que você quer converter? "), 10)

            if base_converter == 2: # Conversão de base decimal para binaria

                resultado = bin(valor)
                print(f"O numero {valor} em binário é {resultado}...\n")
                break

            elif base_converter == 3: # Conversão de base decimal para octal

                resultado = oct(valor)
                print(f"O numero {valor} em octal é {resultado}... \n")
                break

            elif base_converter == 4: # Conversão de base decimal para hexadecimal

                resultado = hex(valor)
                print(f"O numero {valor} em hexadecimal é {resultado}... \n")
                break

            elif base_converter == 9:   # fechar o programa
                break

            else: 
                print("opção invalida")
                break

        elif base == 2: # Conversão de binario

            valor = int(input("Qual o valor que você quer converter? "), 2) # ja pegando o valor na base binaria (2)

            if base_converter == 1: # Conversão de binario para decimal

                resultado = float(valor)
                print(f"A conversão para decimal é {resultado}...\n")
                break

            elif base_converter == 3:   # Conversão de binario para octal

                resultado = oct(valor)
                print(f"A conversão para octal é {resultado}... \n")
                break

            elif base_converter == 4:   # Conversão de binario para hexadecimal

                resultado = hex(valor)
                print(f"A conversão para Hexadecimal é {resultado}... \n")
                break

            elif base_converter == 9:   # fechar o programa
                break

            else: 
                print("Opção invalida")
                break
        
        elif base == 3: # Conversão de Octal

            valor = int(input("Qual o valor que você quer converter? "), 8) # ja pegando o valor na base octal (8)

            if base_converter == 1: # Conversão de Octal para decimal

                resultado = float(valor)
                print(f"A conversão para decimal é {resultado}...\n")
                break

            elif base_converter == 2: # Conversão de Octal para binario

                resultado = bin(valor)
                print(f"A conversão para binário é {resultado}... \n")
                break

            elif base_converter == 4: # Conversão de Octal para hexadecimal

                resultado = hex(valor)
                print(f"A conversão para Hexadecimal é {resultado}... \n")
                break

            elif base_converter == 9:   # fechar o programa
                break

            else: 
                print("opção invalida")
                break

        elif base == 4: # Conversão de Hexadecimal

            valor = int(input("Qual o valor que você quer converter? "), 16) # Já pegando o valor na base Hexadecimal (16)

            if base_converter == 1: # Conversão de Hexadecimal para decimal

                resultado = float(valor)
                print(f"A conversão para decimal é {resultado}...\n")
                break

            elif base_converter == 2: # Conversão de Hexadecimal para binario

                resultado = bin(valor)
                print(f"A conversão para binário é {resultado}... \n")
                break

            elif base_converter == 3: # Conversão de Hexadecimal para octal

                resultado = oct(valor)
                print(f"A conversão para octal é {resultado}... \n")
                break

            elif base_converter == 9: # fechar o programa
                break

            else: 
                print("opção invalida")
                break


    elif escolha == 2:  # Soma

        menu_soma()
        escolha = int(input("Escolha a base para a soma: "))

        if escolha == 1:    # Soma de decimais

            valor1 = int(input("Insira um valor: "))
            valor2 = int(input("Insira um valor: "))

            total = valor1 + valor2

            print(f"A soma de {valor1} e {valor2} é igual a {total}")
            break
    
        elif escolha == 2:  # Soma de binarios

            valor1 = int(input("Insira um valor: "), 2)
            valor2 = int(input("Insira um valor: "), 2)

            total = valor1 + valor2

            print(f"A soma de {bin(valor1)} e {bin(valor2)} é igual a {bin(total)}")
            break

    
        elif escolha == 3:  # Soma de octal

            valor1 = int(input("Insira um valor: "), 8)
            valor2 = int(input("Insira um valor: "), 8)

            total = valor1 + valor2

            print(f"A soma de {oct(valor1)} e {oct(valor2)} é igual a {oct(total)}")
            break

    
        elif escolha == 4:  # Soma de hexadecimal

            valor1 = int(input("Insira um valor: "), 16)
            valor2 = int(input("Insira um valor: "), 16)

            total = valor1 + valor2

            print(f"A soma de {hex(valor1)} e {hex(valor2)} é igual a {hex(total)}")
            break

        elif escolha == 9:
            break
        else:
            print("Opção inválida")


    elif escolha == 3:  # Subtração

        menu_subtracao()
        escolha = int(input("Escolha a base para a subtração: "))

        if escolha == 1:    # Subtração de decimais

            valor1 = int(input("Insira um valor: "))
            valor2 = int(input("Insira um valor: "))

            total = valor1 - valor2

            print(f"A subtração de {valor1} por {valor2} é igual a {total}")
            break
    
        elif escolha == 2:  # Subtração de binarios

            valor1 = int(input("Insira um valor: "), 2)
            valor2 = int(input("Insira um valor: "), 2)

            total = valor1 - valor2

            print(f"A subtração de {bin(valor1)} por {bin(valor2)} é igual a {bin(total)}")
            break

    
        elif escolha == 3:  # Subtração de octais

            valor1 = int(input("Insira um valor: "), 8)
            valor2 = int(input("Insira um valor: "), 8)

            total = valor1 - valor2

            print(f"A subtração de {oct(valor1)} por {oct(valor2)} é igual a {oct(total)}")
            break

    
        elif escolha == 4: # Subtração de hexadecimais

            valor1 = int(input("Insira um valor: "), 16)
            valor2 = int(input("Insira um valor: "), 16)

            total = valor1 - valor2

            print(f"A subtração de {hex(valor1)} por {hex(valor2)} é igual a {hex(total)}")
            break

        elif escolha == 9:
            break
        else:
            print("opção inválida")

    elif escolha == 9:
        break
    else:
        print("opção inválida")