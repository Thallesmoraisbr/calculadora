while True:

    print("Escolha uma operação:") 

    print("1 - Soma")

    print("2 - Subtração")

    print("3 - Multiplicação")

    print("4 - Divisão")

    print("5 - Divisão Inteira")

    print("6 - Módulo")

    print("7 - Potenciação")
    
    print("0 - Sair")

    opcao = int(input("Informe o número da operação:"))

    while opcao > 7 or opcao < 0:

        opcao = int(input("Não existe essa operação, indique uma operação entre 0 e 7:"))
        
    if opcao == 0:

        print("encerrando")

        break

    primiero = float(input("Informe o primeiro número:"))

    segundo = float(input("Informe o segundo número:"))
    
    if opcao == 1:

        resultado = primiero + segundo

        print("O resultado é:" + str(resultado))

    elif opcao == 2:

        resultado = primiero - segundo

        print("O resultado é:" + str(resultado))

    elif opcao == 3:

        resultado = primiero * segundo

        print("O resultado é:" + str(resultado))

    elif opcao == 4:

        while segundo == 0:

            print("Não existe divisão por zero")

            segundo = float(input("Informe o segundo número novamente:"))

        resultado = primiero / segundo

        print("O resultado é:" + str(resultado))

    elif opcao == 5:

        resultado = primiero // segundo

        print("O resultado é:" + str(resultado))

    elif opcao == 6:

        resultado = primiero % segundo

        print("O resultado é:" + str(resultado))

    elif opcao == 7:

        resultado = primiero ** segundo

        print("O resultado é:" + str(resultado))
