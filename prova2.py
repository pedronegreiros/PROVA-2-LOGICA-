#PROVA 2 DE  LOGICA DE PROGRAMAÇÃO ALUNO: PEDRO NEGREIROS 

# Verifica se a velocidade ultrapassa 80 km/h

limite_velocidade = 80
velocidade= input(int("Qual a velocidade? "))



if velocidade > limite_velocidade:

    # Calcula o valor da multa

    valor_multa = (velocidade - limite_velocidade) * 20.0



    # Exibe a mensagem de multa e o valor

    print(f"Você foi multado! A velocidade excedeu {limite_velocidade} km/h.")

    print(f"Valor da multa: R${valor_multa:.2f}")

else:

    print("Velocidade dentro do limite permitido.")
