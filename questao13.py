alt = float(input("Qual é sua altura? "))
sexo = input("Você é homem ou mulher? ")
pesoIdealH = (72.7*alt)-58
pesoIdealM = (62.1*alt)-44.7

if (sexo == "homem"):
    print(f"O peso ideal para homem é: {pesoIdealH}kg")
else :
    print(f"O peso ideal para mulher é: {pesoIdealM}kg")
