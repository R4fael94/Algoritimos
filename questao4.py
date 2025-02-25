not1 = float(input("Informe a 1º Nota: "))
not2 = float(input("Informe a 2º Nota: "))
not3 = float(input("Informe a 3º Nota: "))
not4 = float(input("Informe a 4º Nota: "))
media = (not1+not2+not3+not4)/4

print(f"Sua média é: {media}")
if media >=7:
	print("Você foi aprovado!")