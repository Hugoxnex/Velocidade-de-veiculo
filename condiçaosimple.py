print(" Condiçao SIMPLES")
velocidade = float(input(" Qual e sua velocidade real: ? "))
if velocidade > 80:
    print("Multado ! Voce exedeu o limite permitido de 80km/h ")
    Multa = (velocidade-80) * 7
    print(" Voce deve pagar Uma Multa de R$ {:.2f}!".format(Multa))
print(" Tenha um bom dia ! Dirija com Segurança!")