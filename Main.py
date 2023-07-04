import functions

def menu():
    print("Menu:")
    print("1 - Listar animais registrados.")
    print("2 - Gerar quantidade de vezes em que cada animal se alimentou.")
    print("3 - Organizar de maneira crescente de acordo com a alimentação de cada animal.")
    print("4 - Listar as vezes em que os animais se alimentaram e sinalizar os animais que estão com a alimentação não-saudável.")
    print("5 - Sair")
    return input("Escolha uma opção: ")

while True:
    option = menu()
    if option == "1":
        functions.listPets()
    elif option == "2":
        functions.generateData()
    elif option == "3":
        functions.listAscendingOrder()
    elif option == "4":
        functions.listUnhealthyAnimals()
    elif option == "5":
        break
    else: 
        print("Opção inválida. Tente novamente.")
