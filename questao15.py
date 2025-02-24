horas = float(input("Quanto você ganha por hora? "))
horario = float(input("Quantas horas você trabalhou no mês? "))
salario = horas*horario
ir = salario*0.11
inss = salario*0.08
Sindicato = salario*0.05
salarioLiquido = salario-ir-inss-Sindicato

print(f"Você ganhou o total de R$ {salario}\nPagou R$ {ir} de Imposto de Renda\nPagou R$ {inss} de INSS\nPagou R$ {Sindicato} ao Sindicato\ne Seu salário liquido foi de R$ {salarioLiquido}")
