# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Jogador(object):
    pontos_dict = ['0', '15', '30', '40', 'A', 'W']
    vitoria = False
    pontos = 0

    def get_pontuacao(self):
        return self.pontos_dict[self.pontos]


class Jogo(object):

    pontos = ['0', '15', '30', '40', 'A', 'W']
    jogador1 = None
    jogador2 = None
    ultimo = None

    def __init__(self, jogador1, jogador2):
        self.jogador1 = jogador1
        self.jogador2 = jogador2
        self.ultimo = jogador1

    def pontua(self, jogador):
        if self.jogador1.get_pontuacao() == '40' and self.jogador2.get_pontuacao() == '40':
            jogador.pontos += 1
        elif self.ultimo.get_pontuacao() == 'A' and self.ultimo != jogador:
            self.ultimo.pontos -= 1
        elif jogador.get_pontuacao() == '40':
            jogador.pontos += 2
        else:
            jogador.pontos += 1
        self.ultimo = jogador

    def get_pontuacao_1(self):
        print self.jogador1.pontos
        return self.pontos[self.jogador1.pontos]

    def get_pontuacao_2(self):
        return self.pontos[self.jogador2.pontos]

    def get_placar(self):
        pontuacao_jogador1 = self.get_pontuacao_1()
        pontuacao_jogador2 = self.get_pontuacao_2()

        return [pontuacao_jogador1, pontuacao_jogador2]