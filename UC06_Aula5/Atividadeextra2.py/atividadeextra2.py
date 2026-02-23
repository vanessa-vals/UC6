while True:
    print("\n--- MENU ---")
    print("1- Par ou Ímpar (1 a 99999)")
    print("2- Tabuada")
    print("3- Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        print("\nContando de 1 a 10:")
        for i in range(1, 11):
            if i % 2 == 0:
                print(f"{i} é par")
            else:
                print(f"{i} é ímpar")

    elif opcao == '2':
        num = int(input("Digite um número para ver a tabuada: "))
        print(f"\nTabuada do {num}:")
        for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")

    elif opcao == '3':
        print("Saindo do programa... Até logo!")
        break  # Interrompe o while e encerra o programa

    else:
        print("Opção inválida! Tente novamente.")