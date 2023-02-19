"""summary_
    """

import tkinter


def __abrir_janela__():
    janela2 = tkinter.Toplevel()
    janela2.title("Janela 2")
    label_nome = tkinter.Label(janela2, text="Nome")
    label_nome.grid(row=0, column=0)
    botao_voltar = tkinter.Button(
        janela2, text="Fechar a Janela2", command=janela2.destroy)
    botao_voltar.grid(row=1, column=1)
    janela2.geometry("500x400+200+100")


janela = tkinter.Tk()
janela.title("Teste de janela")
janela.geometry("500x400+500+250")

myBut = tkinter.Button(janela, text="Clique aqui!", command=__abrir_janela__)
myBut.grid(row=0, column=0,)

janela.mainloop()
