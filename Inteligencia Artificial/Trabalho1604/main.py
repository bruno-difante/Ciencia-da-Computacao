import copy
from ag import AG

tamanho_populacao = int(input("Tamanho da população: "))
taxa_selecao = int(input("Taxa de seleção (20–40%): "))
taxa_reproducao = 100 - taxa_selecao
taxa_mutacao = int(input("Taxa de mutação (5–10%): "))
qtd_geracoes = int(input("Quantidade de gerações: "))

rota_ideal = list(range(1, 10))
populacao = []
nova_populacao = []

AG.gerar_populacao(populacao, tamanho_populacao, rota_ideal)
populacao.sort()
print("\nGeração 1:")
AG.exibir(populacao)

for geracao in range(2, qtd_geracoes + 1):
    AG.selecionar_por_torneio(populacao, nova_populacao, taxa_selecao)
    AG.reproduzir(populacao, nova_populacao, taxa_reproducao, rota_ideal)

    if geracao % max(1, (len(populacao) // taxa_mutacao)) == 0:
        AG.mutar(nova_populacao, rota_ideal)

    populacao = copy.deepcopy(nova_populacao)
    nova_populacao.clear()
    populacao.sort()

    print(f"\nGeração {geracao}:")
    AG.exibir(populacao)