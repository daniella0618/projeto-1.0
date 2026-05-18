
import os
import sys

# Faz o Python enxergar a pasta src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.core.llm_client import AzureModel

def main():
    llm = AzureModel()

    print("Digite uma recomendação (ou 'sair' para encerrar)\n")

    while True:
        texto = input("Você: ")

        if texto.lower() == "sair":
            print("Encerrando...")
            break

        prompt = f"Analise a recomendação de investimento: {texto}. Diga se é adequada e explique o motivo."

        try:
            response = llm.invoke(prompt)
            resposta = response.choices[0].message.content

            print("\nIA:", resposta)
            print("-" * 50)

        except Exception as e:
            print(f"\nErro: {e}")
            print("-" * 50)


if __name__ == "__main__":
    main()