import random

name = input("Qual seu nome? ")

class Inicio:
    def __init__(self):
        decid = input("Vamos comecar o jogo? ").lower()

        if decid in ["sim", "claro", "ok", "s", "sure", "bora"]:
            print("Entao vamos la\n")

        else:
            print("ok, entao bye")
            exit()

print("""
==========================================================================

Seja Bem Vindo %s

--------------------------------------------------------------------------

Regras: A cada questao respondida corretamente voce acumula +100 pontos
por outro lado a cada questao errada sera descontado -50 pontos

Boa sorte !

==========================================================================\n""" % (name))

class Jogo:
    pontuacao = 0

    acerto = 100
    erro = -50

    ganhar = 400
    perder = -300

    perguntas = [
        {
            'pergunta': 'Qual a cor do cavalo branco de Napoleao?\n',
            'respostas': {
                'a': 'Branco',
                'b': 'Preto',
                'c': 'Vermelho',
                'd': 'Azul\n'
            },
            'certa': 'b'
        },
        {
            'pergunta': 'O UFC foi criado por quem?\n',
            'respostas': {
                'a': 'Helio Gracie',
                'b': 'Vitor Belfort',
                'c': 'Carlinhos Gracie\n'
            },
            'certa': 'c'
        },
        {
            'pergunta': 'Aonde foi a famosa Baguncinha?\n',
            'respostas': {
                'a': 'Los Anges, California',
                'b': 'New York, Albany',
                'c': 'Brasil, Berlandia\n'
            },
            'certa': 'a'
        },
    ]

    def __init__(self):
        self.perguntar()

    def perguntar(self):
        pergunta = random.choice(self.perguntas)

        texto_da_pergunta = pergunta['pergunta']
        alternativas = pergunta['respostas'].keys()

        while True:
            print(texto_da_pergunta)
            for alternativa in alternativas:
                print("%s) %s" % (alternativa, pergunta['respostas'][alternativa]))

            resposta = input()
            if (resposta in alternativas):
                print("\nVoce escolheu a resposta %s\n" % resposta.upper())
                if (resposta == pergunta['certa']):
                    self.acertou()
                else:
                    self.errou()

                self.pontuacaoAtual()
                break
            else:
                print("\nResposta invalida.\n")

        if (self.pontuacao >= self.ganhar):
            self.ganhou()
        elif (self.pontuacao <= self.perder):
            self.perdeu()
        else:
            self.perguntar()

    def acertou(self):
        print('Acertou Miresavi !!!')
        self.pontuacao = self.pontuacao + self.acerto

    def errou(self):
        print('\nresposta errada!!')
        self.pontuacao = self.pontuacao + self.erro

    def pontuacaoAtual(self):
        print('Voce acumulou %s pontos\n' % self.pontuacao)

    def ganhou(self):
        print('\nGANHOU !!!\n')
        exit()

    def perdeu(self):
        print('\nPERDEU PREYBOI !!!\n')
        exit()

Inicio()
jogo = Jogo()
