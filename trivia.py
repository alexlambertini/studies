name = input("Qual seu nome? ")
decid = input("Vamos comecar o jogo? ").lower()
if decid == ("sim"):
    print("Entao vamos la \n")
else:
    print("ok, entao bye")

print("\n===================================================\n Seja Bem Vindo %s \n===================================================\n" % (name))

print("Qual a cor do cavalo branco de Napoleao? \n\n a) Branco \n b) Preto \n c) Vermelho \n")
resp = input()
if resp == ("a"):
    print("\n Acertou Miresavi !! Voce acumulou " + str(100) + " pontos")
else:
    print("\n Resposta errada")
