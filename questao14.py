kg = float(input("Quantos quilos de peixe está levando? "))
kge = kg - 50 
rkg = kge * 4

if kg <=50:
    print("Esta adequado, sem quilos excedentes")
else:
    print(f"Não está adequado, possui {kge}kg excedente e cobrara o valor de R$ {rkg}")