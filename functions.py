import random
import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def generate_encryption_key():
    # Gera uma chave de criptografia aleatória de 16 bytes (128 bits)
    key = bytearray(random.getrandbits(8) for _ in range(16))
    return key

def encrypt_data(data, encryption_key):
    # Criptografa os dados fornecidos usando o algoritmo AES em modo CBC (Cipher Block Chaining) com a chave de criptografia fornecida
    cipher = Cipher(algorithms.AES(encryption_key), modes.CBC(), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(data) + encryptor.finalize()
    return encrypted_data

def decrypt_data(encrypted_data, encryption_key):
    # Descriptografa os dados criptografados fornecidos usando o algoritmo AES em modo CBC (Cipher Block Chaining) com a chave de criptografia fornecida
    cipher = Cipher(algorithms.AES(encryption_key), modes.CBC(), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
    return decrypted_data

def listPets():
    # Lista os animais registrados, exibindo seus IDs e nomes no console
    animals = {
        1: "Diná",
        2: "Zé Lelé",
        3: "Bagueera",
        4: "Balu",
        5: "Pretinha",
        6: "Quevedo",
        7: "Armandinho",
        8: "Nina",
        9: "Jupí",
        10: "Muleke"
    }
    print("Animais registrados:")
    for id, name in animals.items():
        print(f"{id} - {name}")

def generateData():
    # Gera dados aleatórios de alimentação para cada animal registrado
    animals = {
        1: "Diná",
        2: "Zé Lelé",
        3: "Bagueera",
        4: "Balu",
        5: "Pretinha",
        6: "Quevedo",
        7: "Armandinho",
        8: "Nina",
        9: "Jupí",
        10: "Muleke"
    }
    data = {}
    for id, name in animals.items():
        vezes = random.randint(1, 5)
        data[f"({id}) {name}"] = f"se alimentou {vezes} vezes"
    for animal, vezes in data.items():
        print(f"{animal} - {vezes}")
    return data

def listAscendingOrder():
    # Gera dados de alimentação e ordena os animais com base no número de vezes que foram alimentados em ordem crescente
    data = generateData()
    sorted_data = sorted(data.items(), key=lambda x: int(x[1].split()[2]))
    print("Animais ordenados pelo número de vezes que foram alimentados:")
    for animal, vezes in sorted_data:
        print(f"{animal} - {vezes}")

def listUnhealthyAnimals():
    # Gera dados de alimentação e verifica quais animais se alimentaram de maneira não recomendada (mais de 2 vezes)
    data = generateData()
    print("Animais que se alimentaram de maneira não recomendada (Animais adultos devem comer em média 2 vezes ao dia):")
    for animal, vezes in data.items():
        if int(vezes.split()[2]) >= 3:
            print(animal)

# Chamadas de função

listPets()

print("\n--- Dados Gerados ---")
generateData()

print("\n--- Animais em Ordem Crescente de Alimentação ---")
listAscendingOrder()

print("\n--- Animais que se Alimentaram de Maneira Não Recomendada ---")
listUnhealthyAnimals()
