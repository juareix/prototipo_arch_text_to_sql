import sys
import os
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "src")))
from pipelines.router.router_chain import RouterChain


def main():
    router = RouterChain()
    while True:
        user_message = input("Digite sua pergunta (ou 'sair' para encerrar): ")
        if user_message.lower() == "sair":
            print("Encerrando o sistema. Até mais!")
            break

        start_time = time.time()
        decision = router.run(user_message)
        end_time = time.time()
        print(f"Tempo de processamento da decisão: {end_time - start_time:.2f} segundos")

        if decision.route == "sql":
            print("Rota SQL selecionada. Processando pergunta com pipeline SQL...")
            # Aqui você chamaria a função do pipeline SQL
        elif decision.route == "policy":
            print("Rota Policy selecionada. Processando pergunta com pipeline de documentos...")
            # Aqui você chamaria a função do pipeline de documentos
        else:
            print("Rota Smalltalk selecionada. Processando pergunta com pipeline de conversas casuais...")
            # Aqui você chamaria a função do pipeline de smalltalk
main()