from collections import Counter
import heapq

texto = "otorrinolaringologia"

frequencia = Counter(texto)

monte = [[peso, [simbolo, ""]] for simbolo, peso in frequencia.items()]
heapq.heapify(monte)
while len(monte) > 1:
    menor = heapq.heappop(monte)
    maior = heapq.heappop(monte)
    for par in menor[1:]:
        par[1] = '0' + par[1]
    for par in maior[1:]:
        par[1] = '1' + par[1]
    heapq.heappush(monte, [menor[0] + maior[0]] + menor[1:] + maior[1:])

codigos_huffman = sorted(heapq.heappop(monte)[1:], key=lambda p: (len(p[-1]), p))

dicionario_codigos_huffman = {simbolo: codigo for simbolo, codigo in codigos_huffman}
print(dicionario_codigos_huffman)
