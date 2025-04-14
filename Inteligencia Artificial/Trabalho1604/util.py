import random

class Util:
    @staticmethod
    def gerar_rota(qtd_cidades):
        rota = list(range(1, qtd_cidades + 1))
        random.shuffle(rota)
        return rota