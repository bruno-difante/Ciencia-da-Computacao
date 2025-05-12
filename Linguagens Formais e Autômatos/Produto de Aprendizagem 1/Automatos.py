#Funcao para verificar o automato
def afd_termina_em_101(palavra):
    estado = 'q0'

    for simbolo in palavra:
        if simbolo not in ['0', '1']:
            return False

        if estado == 'q0':
            if simbolo == '1':
                estado = 'q1'
            else:
                estado = 'q0'

        elif estado == 'q1':
            if simbolo == '0':
                estado = 'q2'
            else:
                estado = 'q1'

        elif estado == 'q2':
            if simbolo == '1':
                estado = 'q3'
            else:
                estado = 'q0'

        elif estado == 'q3':
            if simbolo == '0':
                estado = 'q2'
            else:
                estado = 'q1'

    return estado == 'q3'


# Parte do usuario
print("🔁 Verificador de palavras que terminam em '101'")
print("Digite palavras com 0s e 1s. Digite 'sair' para encerrar.\n")

while True:
    entrada = input("Digite uma palavra: ").strip()
    if entrada.lower() == 'sair':
        print("Encerrando o verificador. Até logo!")
        break

    resultado = afd_termina_em_101(entrada)
    print(f"Resultado: {'✅ Aceita' if resultado else '❌ Rejeita'}\n")
