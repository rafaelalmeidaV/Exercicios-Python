HorasTrabalhadas = int(input("Digite a quantidade de horas trabalhadas: ")) 
ValorSalarioMinimo = float(input("Digite o valor do salário mínimo: "))
PorcentagemDeImposto = 0.03

ValorHora = ValorSalarioMinimo / 2

SalarioBruto = HorasTrabalhadas * ValorHora

TotalImposto = SalarioBruto * PorcentagemDeImposto

SalarioLiquido = SalarioBruto - TotalImposto

print("O salario liquido do funcionário é:", SalarioLiquido)	