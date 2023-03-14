
from nltk.chat.util import Chat, reflections

# Perguntas e respostas
pairs = [
    [
        r"Por que não consigo acessar o site da (.*)?",
        ["O site pode estar em manutenção", "Talvez o site esteja fora do ar"]
    ],
    [
        r"Onde posso encontrar as notas de (.*)?",
        ["No site do Sigaa, na aba de ensino", "No site do Siga"]
    ],
    [
        r"Onde encontro o MC geral do curso de (.*)?",
        ["Na aba de ensino do SIGAA",  "No site da UFRPE"]
    ],
    [
        r"adeus",
        ["Até logo! Espero ter sido útil para você.",
            "Obrigado por falar comigo.", "Muito obrigado. Tenha um ótimo dia!"]
    ],
    [
        r"(.*)",
        ["Por favor, me conte mais.", "Você pode falar mais sobre?", "Tirou 0 em circuitoskkkkkkk.",
            "Tô em Serra", "Testinho acabou com o ome", " O que é o J?"]

    ],

]

# entrada de dados do usuario
def process_input(user_input):
    return user_input.lower()

# Gerar Respostas
def generate_response(user_input):
    for pattern, responses in pairs:
        match = nltk.matching.regexp.match(pattern, user_input)
        if match is not None:
            response = nltk.chat.util.reflections.random_response(responses)
            return response


baldr_chatbot = Chat(pairs, reflections)


def baldr_chat():
    print("Olá, como posso te ajudar?")
    baldr_chatbot.converse()


def demo():
    baldr_chat()


if __name__ == "__main__":
    demo()
