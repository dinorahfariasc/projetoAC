from itertools import *
# 2.1
# # 21 codigo morse OK
# print("\n================ 2.1 Questao 21 ===================")
# palavras = []
# for i in product(["ponto", "traço"], repeat=4):
#     print(list(i))
#     palavras.append(i)
# print(f"Total de palavras {len(palavras)}")
#
# # 22 fichas OK usando nested loops
# print("\n================ 2.1 Questao 22 ===================")
# total = []
# for x in ["amarelo","vermelho", "azul"]:
#     for y in ["circular", "retangular","triangulares"]:
#         for z in ["finas","grossas"]:
#             total.append([x, y, z])
#
# for x in total:
#     print(x,end="\n")
# print(f"Total de fichas: {len(total)}")


# 2.3
# 29 times OK
# print("\n================ 2.3 Questao 29 ===================")
# times = ["time" + str(x) for x in range(1, 21)]
# jogos = list(combinations(times, 2))
# for y in combinations(times, 2):
#     print(list(y))
#
# print(f"o total do jogos sera: {len(jogos)}")

# ======================================================================

# print("\n================ 2.3 Questao 27 ===================")
# from itertools import combinations
# # Jogadores disponíveis
# jogadores = ["Jogador1", "Jogador2", "Jogador3", "Jogador4", "Jogador5",
#              "Jogador6", "Jogador7", "Jogador8", "Jogador9", "Jogador10",
#              "Jogador11", "Jogador12", "Jogador13", "Jogador14", "Jogador15"]

# # Chama a função para dividir os jogadores em 3 times
# print("\nopcoes equipe esperança\n")
# esperança = combinations(jogadores, 5)
# count = 0
# for x in esperança:
#   print(list(x))
#   count += 1
# print(count)

# # como 5 jogadores ja foram selecionados, para o proximo grupo sobraram 10
# opcoesConfianca = [1,2,3,4,5,6,7,8,9,10]

# confianca = combinations(opcoesConfianca,5)
# count2 = 0
# for x in confianca:
#   print(list(x))
#   count2 += 1
# print(count2)

# print("\nopcoes equipe vitoria")
# opcoesVitoria = [1,2,3,4,5]

# vitoria = combinations(opcoesVitoria,5)
# count3 = 0
# for x in vitoria:
#   print(list(x))
#   count3 += 1
# print(count3)

# print(f"\no total de times possiveis será de: {count * count2 * count3}")

#=====================================================================================================
# print("\n================ 2.2 Questao 13 ===================")
#
# # calculamos a quantidades de jogos possiveis, de 12 combinados 2 a 2 em 6 vezes, e dividimos pela permuatacao dos jogos de uma unica rodada 6!
# from math import factorial
# from itertools import combinations
#
# def combinacoes_jogos(times,partida = 2):
#     times += 1
#     quantidade_times = [x for x in range(1, times)]
#     jogos = combinations(quantidade_times, partida)
#     count = 0
#     for x in jogos:
#         print(list(x))
#         count += 1
#     print(f"possibilidades de jogos para C({times-1},{partida}): {count}")
#     return count
#
# # a cada partida diminui 2 times, os quais foram selecionados na anterior
#
# partida1 = combinacoes_jogos(12)
# partida2 = combinacoes_jogos(10)
# partida3 = combinacoes_jogos(8)
# partida4 = combinacoes_jogos(6)
# partida5 = combinacoes_jogos(4)
# partida6 = combinacoes_jogos(2)
#
# # todas combinacoes possiveis
#
# todas = partida1 * partida2 * partida3 * partida4 * partida5 * partida6
# # dividindo pelas permutacoes dentro de cada partida
#
# total = int(todas/factorial(6))
# print(f"Assim o total de jogos possiveis na primeira rodada, entre 12 times será de: {total}")
#


