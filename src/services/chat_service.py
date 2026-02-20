import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "src")))
from pipelines.router.router_chain import RouterChain

if __name__ == "__main__":
    user_message = "Qual é a receita média mensal da empresa no último trimestre?"  # Exemplo de mensagem do usuário
    router = RouterChain()
    decision = router.run(user_message)

    if decision.route == "sql":
        print("Rota SQL selecionada. Processando pergunta com pipeline SQL...")
    elif decision.route == "policy":
        print("Rota Policy selecionada. Processando pergunta com pipeline de documentos...")
    elif decision.route == "analytics":
        print("Rota Analytics selecionada. Processando pergunta com pipeline analítico...")
    else:
        print("Rota Smalltalk selecionada. Processando pergunta com pipeline de conversas casuais...")