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
