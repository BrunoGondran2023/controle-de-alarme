# Definindo constantes para os estados possíveis.

aberta = "a"
fechada = "f"


def verificar_estado(componente, estado, nome_componente):
    """
    Função para verificar o estado de um componente (porta ou janela)
    e imprimir uma mensagem apropriada.
    """
    if componente == estado:
        print(f"{nome_componente} aberta, alarme disparado!")
    else:
        print(f"{nome_componente} fechada.")


def verificar_controle(porta, janela, estado):
    """
    Função para verificar se tudo está sob controle.
    """
    if porta != estado and janela != estado:
        print("Tudo sob controle!")


def main():
    """
    Função principal do programa.
    """
    # Definindo o estado da porta e da janela.
    porta = fechada
    janela = aberta

    # Definindo o estado que dispara o alarme.
    disparar_alarme = aberta

    # Verificando o estado da porta e da janela.
    verificar_estado(porta, disparar_alarme, "Porta")
    verificar_estado(janela, disparar_alarme, "Janela")

    # Verificando se tudo está sob controle.
    verificar_controle(porta, janela, disparar_alarme)


if __name__ == "__main__":
    main()
