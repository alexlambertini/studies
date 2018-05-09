name = input("Qual seu nome? ")
decid = input("Vamos comecar o jogo? ").lower()

if decid == ("sim"):
    print("Entao vamos la \n")
elif decid == ("claro"):
    print("Entao vamos la \n")
elif decid == ("ok"):
    print("Entao vamos la \n")
elif decid == ("s"):
    print("Entao vamos la \n")
else:
    print("ok, entao bye")
    exit()

print("\n===================================================\n Seja Bem Vindo %s \n===================================================\n" % (name))

print("Qual a cor do cavalo branco de Napoleao? \n\n a) Branco \n b) Preto \n c) Vermelho \n")
resp = input().lower()
score = str("100")
if resp == ("b"):
    print("\nVoce escolheu a resposta %s \nAcertou Miresavi !!! \nVoce acumulou %s pontos" % (resp.upper(), score))
else:
    print("\nVoce escolheu a resposta %s, resposta errada!!" % (resp.upper()))
