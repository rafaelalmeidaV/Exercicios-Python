nota1 = float(input("Digite a primeira nota: "))
peso1 = int(input("Digite o peso da primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
peso2 = int(input("Digite o peso da segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
peso3 = int(input("Digite o peso da terceira nota: "))

media_ponderada = ((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)) / (peso1 + peso2 + peso3)

print("A média ponderada das notas é:", media_ponderada)