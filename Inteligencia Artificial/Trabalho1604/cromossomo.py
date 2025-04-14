class Cromossomo:
    def __init__(self, rota, rota_ideal):
        self.valor = rota
        self.aptidao = self.calcular_aptidao(rota_ideal)

    def calcular_aptidao(self, rota_ideal):
        nota = 0

        for i in range(len(self.valor)):
            for j in range(i + 1, len(self.valor)):
                if self.valor[i] > self.valor[j]:
                    nota += 10

        vistos = {}
        for cidade in self.valor:
            vistos[cidade] = vistos.get(cidade, 0) + 1

        for count in vistos.values():
            if count > 1:
                pares_repetidos = count * (count - 1) // 2
                nota += 20 * pares_repetidos

        return nota

    def __eq__(self, other):
        return isinstance(other, Cromossomo) and self.valor == other.valor

    def __gt__(self, other):
        return self.aptidao >= other.aptidao  # menor = melhor

    def __str__(self):
        return f"rota = {self.valor}, aptidão = {self.aptidao}"