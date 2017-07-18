# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from core.models import Jogador, Jogo


class TenisTest(TestCase):

    def test_jogo(self):
        jogador1 = Jogador()
        jogador2 = Jogador()
        jogo = Jogo(jogador1, jogador2)
        jogo.pontua(jogador1)
        self.assertEqual(jogo.get_placar(), ['15', '0'])
        jogo.pontua(jogador1)
        self.assertEqual(jogo.get_placar(), ['30', '0'])
        jogo.pontua(jogador2)
        self.assertEqual(jogo.get_placar(), ['30', '15'])
        jogo.pontua(jogador2)
        self.assertEqual(jogo.get_placar(), ['30', '30'])
        jogo.pontua(jogador1)
        self.assertEqual(jogo.get_placar(), ['40', '30'])
        jogo.pontua(jogador2)
        self.assertEqual(jogo.get_placar(), ['40', '40'])
        jogo.pontua(jogador1)
        self.assertEqual(jogo.get_placar(), ['A', '40'])
        jogo.pontua(jogador2)
        self.assertEqual(jogo.get_placar(), ['40', '40'])
        jogo.pontua(jogador1)
        self.assertEqual(jogo.get_placar(), ['A', '40'])
        jogo.pontua(jogador1)
        self.assertEqual(jogo.get_placar(), ['W', '40'])

    def test_jogador_1_15_pontos(self):
        jogador1 = Jogador()
        jogador2 = Jogador()
        jogo = Jogo(jogador1, jogador2)
        jogo.pontua(jogador1)
        self.assertEqual(jogo.get_pontuacao_1(), '15', "deveria retornar 15")

    def test_jogador_1_30_pontos(self):
        jogador1 = Jogador()
        jogador2 = Jogador()
        jogo = Jogo(jogador1, jogador2)
        jogo.pontua(jogador1)
        jogo.pontua(jogador1)
        self.assertEqual(jogo.get_pontuacao_1(), '30', "deveria retornar 30")

    def test_jogador_1_40_pontos(self):
        jogador1 = Jogador()
        jogador2 = Jogador()
        jogo = Jogo(jogador1, jogador2)
        jogo.pontua(jogador1)
        jogo.pontua(jogador1)
        jogo.pontua(jogador1)
        self.assertEqual(jogo.get_pontuacao_1(), '40', "deveria retornar 40")

    def test_jogador_1_vitoria(self):
        jogador1 = Jogador()
        jogador2 = Jogador()
        jogo = Jogo(jogador1, jogador2)
        jogo.pontua(jogador1)
        jogo.pontua(jogador1)
        jogo.pontua(jogador1)
        jogo.pontua(jogador1)
        self.assertEqual(jogo.get_pontuacao_1(), 'W', "deveria retornar W")

    def test_jogador_2_15_pontos(self):
        jogador1 = Jogador()
        jogador2 = Jogador()
        jogo = Jogo(jogador1, jogador2)
        jogo.pontua(jogador2)
        self.assertEqual(jogo.get_pontuacao_2(), '15', "deveria retornar 15")

    def test_jogador_2_30_pontos(self):
        jogador1 = Jogador()
        jogador2 = Jogador()
        jogo = Jogo(jogador1, jogador2)
        jogo.pontua(jogador2)
        jogo.pontua(jogador2)
        self.assertEqual(jogo.get_pontuacao_2(), '30', "deveria retornar 30")

    def test_jogador_2_40_pontos(self):
        jogador1 = Jogador()
        jogador2 = Jogador()
        jogo = Jogo(jogador1, jogador2)
        jogo.pontua(jogador2)
        jogo.pontua(jogador2)
        jogo.pontua(jogador2)
        self.assertEqual(jogo.get_pontuacao_2(), '40', "deveria retornar 40")

    def test_jogador_2_vitoria(self):
        jogador1 = Jogador()
        jogador2 = Jogador()
        jogo = Jogo(jogador1, jogador2)
        jogo.pontua(jogador2)
        jogo.pontua(jogador2)
        jogo.pontua(jogador2)
        jogo.pontua(jogador2)
        self.assertEqual(jogo.get_pontuacao_2(), 'W', "deveria retornar 60")

    def test_jogador_deuce_1(self):
        jogador1 = Jogador()
        jogador2 = Jogador()
        jogo = Jogo(jogador1, jogador2)
        jogo.pontua(jogador1)
        jogo.pontua(jogador1)
        jogo.pontua(jogador1)
        jogo.pontua(jogador2)
        jogo.pontua(jogador2)
        jogo.pontua(jogador2)
        jogo.pontua(jogador1)
        self.assertEqual(jogo.get_pontuacao_1(), 'A', "deveria retornar 'A'")

    def test_jogador_deuce_2(self):
        jogador1 = Jogador()
        jogador2 = Jogador()
        jogo = Jogo(jogador1, jogador2)
        jogo.pontua(jogador1)
        jogo.pontua(jogador1)
        jogo.pontua(jogador1)
        jogo.pontua(jogador2)
        jogo.pontua(jogador2)
        jogo.pontua(jogador2)
        jogo.pontua(jogador2)
        self.assertEqual(jogo.get_pontuacao_2(), 'A', "deveria retornar 'A'")

    # def test_jogador_vitoria(self):
    #     jogador1 = Jogador()
    #     jogador2 = Jogador()
    #     jogo = Jogo(jogador1, jogador2)
    #     jogo.pontua(jogador1)
    #     jogo.pontua(jogador1)
    #     jogo.pontua(jogador1)
    #     jogo.pontua(jogador1)
    #     jogo.pontua(jogador2)
    #     jogo.pontua(jogador2)
    #     self.assertEqual(jogo.get_placar(), 'jogador1', "deveria retornar empate")