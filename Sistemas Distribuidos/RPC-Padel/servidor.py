from xmlrpc.server import SimpleXMLRPCServer
import sys

MAP_FUNDAMENTOS = {
    "vo": "Voleio",
    "sm": "Smash",
    "ba": "Bandeja"
}

MAP_ZONAS = {
    "z1": "Zona 1",
    "z2": "Zona 2",
    "z3": "Zona 3"
}

MAP_RESULTADOS = {
    "p": "Ponto",
    "e": "Erro"
}

def processar_jogada(dados_string):
    try:
        partes = dados_string.split(';')
        
        if len(partes) != 3:
            return {"erro": "Formato inválido. Use: fundamento;zona;resultado"}

        cod_fund, cod_zona, cod_res = partes

        resposta = {
            "nome_fundamento": MAP_FUNDAMENTOS.get(cod_fund, "Desconhecido"),
            "zona": MAP_ZONAS.get(cod_zona, "Desconhecida"),
            "resultado": MAP_RESULTADOS.get(cod_res, "Desconhecido"),
            "sucesso": True
        }
        
        print(f"Processado: {dados_string} -> {resposta}")
        return resposta

    except Exception as e:
        return {"sucesso": False, "erro": str(e)}

port = 8000
server = SimpleXMLRPCServer(("localhost", port), allow_none=True)
print(f"Servidor de Padel rodando na porta {port}!")
print("Aguardando requisições...")

server.register_function(processar_jogada, "analisar_padel")

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nServidor parando...")
    sys.exit(0)
