from nltk.chat.util import Chat, reflections
pairs = (

    (
        r"Por que eu não consigo acessar (.*) ?",
        (
            "Já tentou acessar o site da universidade?",
            "Você realmente tentou?"
        ),
    ),
    (
        r"Onde posso achar a planilha de (.*)?",
        (
            "Entrando no site da faculdade e indo na parte de arquivos",
            "No telegram da nossa faculdade.",

        ),
    ),
    (
        r"Olá (.*)",
        (
            "Olá, estou feliz que você veio aqui hoje",
            "Olá, como você está hoje?",
            "Olá, como você está se sentido hoje?",
        ),
    ),
    (
        r"Sair",
        (
            "Obrigado por falar comigo.",
            "tchau.",
            "Muito obrigado. Tenha um ótimo dia!",
        ),
    ),
    (
        r"(.*)",
        (
            "Por favor, me conte mais.",
            "Você pode falar mais sobre?",
            "Por que você disse isso %1?",
            "Tirou 0 em circuitoskkkkkkk.",
            "Testinho acabou com o ome",
            "%1.",
            "Justo. O que é o J?",
        ),
    ),
)

baldr_chatbot = Chat(pairs, reflections)


def baldr_chat():
    print("=" * 72)
    print("Olá, como posso te ajudar?")

    baldr_chatbot.converse()


def demo():
    baldr_chat()


if __name__ == "__main__":
    demo()
