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
