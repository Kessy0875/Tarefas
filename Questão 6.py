# faça um programa que receba o salário de um funcionário
# calcule e mostre o novo salário sabendo-se que este sofreu aumento de 25%.

sal = float(input(' digite seu salario: '))
Aumento = 0.25

novoSal = sal*Aumento+sal

print(f" Seu novo salario e: {novoSal}")