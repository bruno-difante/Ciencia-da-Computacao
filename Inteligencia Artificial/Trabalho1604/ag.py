import random
from cromossomo import Cromossomo
from util import Util

class AG:
    @staticmethod
    def gerar_populacao(populacao, tamanho_populacao, rota_ideal):
        for _ in range(tamanho_populacao):
            populacao.append(Cromossomo(Util.gerar_rota(len(rota_ideal)), rota_ideal))

    @staticmethod
    def exibir(populacao):
        for c in populacao:
            print(c)

    @staticmethod
    def selecionar_por_torneio(populacao, nova_populacao, taxa_selecao):
        qtd = int(taxa_selecao * len(populacao) / 100)
        nova_populacao.append(populacao[0])  # elitismo

        while len(nova_populacao) <= qtd:
            candidatos = random.sample(populacao, 3)
            candidatos.sort()
            vencedor = candidatos[0]
            if vencedor not in nova_populacao:
                nova_populacao.append(vencedor)

    @staticmethod
    def reproduzir(populacao, nova_populacao, taxa_reproducao, rota_ideal):
        qtd = int(taxa_reproducao * len(populacao) / 100)

        while len(nova_populacao) < len(populacao):
            pai = random.choice(populacao)
            mae = random.choice(populacao)
            while mae == pai:
                mae = random.choice(populacao)

            corte = len(pai.valor) // 2
            filho1 = pai.valor[:corte] + mae.valor[corte:]
            filho2 = mae.valor[:corte] + pai.valor[corte:]

            nova_populacao.append(Cromossomo(filho1, rota_ideal))
            if len(nova_populacao) < len(populacao):
                nova_populacao.append(Cromossomo(filho2, rota_ideal))

    @staticmethod
    def mutar(populacao, rota_ideal):
        qtd_mutantes = random.randint(1, max(1, len(populacao) // 5))
        for _ in range(qtd_mutantes):
            index = random.randint(0, len(populacao) - 1)
            mutante = populacao[index].valor[:]
            i, j = random.sample(range(len(mutante)), 2)
            mutante[i], mutante[j] = mutante[j], mutante[i]
            populacao[index] = Cromossomo(mutante, rota_ideal)
