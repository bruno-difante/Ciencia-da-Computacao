import xmlrpc.client

class Jogada:
    def __init__(self, nome_fundamento, zona, resultado):
        self.nome_fundamento = nome_fundamento
        self.zona = zona
        self.resultado = resultado

    def __repr__(self):
        return f'Objeto Jogada -> Tipo: {self.nome_fundamento} | Local: {self.zona} | Status: {self.resultado}'

def main():
    print("Conectando ao servidor RPC...")
    try:
        proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
    except Exception as e:
        print("Erro ao conectar. O servidor.py está rodando?")
        return

    print("\n=== SISTEMA DE ANÁLISE DE PADEL ===")
    print("Formatos aceitos: voleio(vo), smash(sm), bandeja(ba)")
    print("Zonas: z1, z2, z3 | Resultado: p (ponto), e (erro)")
    print("Exemplo de uso: vo;z1;p")
    print("Digite 'sair' para encerrar.\n")

    while True:
        entrada = input(">> Digite a jogada (fund;zona;res): ").strip().lower()

        if entrada in ["sair", "exit", "q"]:
            print("Encerrando cliente.")
            break

        if ";" not in entrada or entrada.count(";") != 2:
            print("Erro: Formato incorreto. Use: sm;z1;p")
            continue

        try:
            dados_retorno = proxy.analisar_padel(entrada)
            
            if dados_retorno.get("sucesso"):
                objeto_jogada = Jogada(
                    dados_retorno["nome_fundamento"],
                    dados_retorno["zona"],
                    dados_retorno["resultado"]
                )
                
                print(f"✅ Sucesso! {objeto_jogada}")
            else:
                print(f"❌ Erro do Servidor: {dados_retorno.get('erro')}")

        except ConnectionRefusedError:
            print("❌ Erro: Sem conexão ao servidor.")
            break
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")

if __name__ == "__main__":
    main()
