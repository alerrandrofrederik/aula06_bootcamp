nome = input("digite seu nome: ")
salario = float(input("digite seu salario: "))
bonus_percentual = float(input("digite o percentual de bonus: "))
kpi = 1000 + salario * bonus_percentual

print(f"Olá {nome}, seu bônus foi de {kpi}")
