ganho = float(input("Quanto você ganha por hora? "))
hora = float(input("Quantas horas por semana você trabalha? "))
semana = int(input("Foram quantas semanas no mês? "))

salario = (hora*semana)*ganho

print(f"Seu salário mensal foi de R$ {salario}")
