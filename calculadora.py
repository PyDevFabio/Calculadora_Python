# Importa todos os Widgtes
from tkinter import *


class Calculadora:

    def __init__(self):

        # Importando Janela no atributo.
        self.window = Tk()
        self.window.title('Calculadora')
        # A aplicação não é escalável, não pode ser redimensionada.
        self.window.resizable(0, 0)
        # Cor da Janela com Pick Color
        """self.window.config(bg='#070221')"""

        # Criando visor que permite digitar números na calc.
        # fg = cor da fonte digitada.
        # bg = cor da tela que digita números.
        self.screen_numbers = Entry(
            self.window, font='arial 20 bold', bg='#070221', fg='white', width=20)
        #ipady = altura, ipadx = altura
        self.screen_numbers.pack(ipady=15, ipadx=200)

        self.frame = Frame(self.window)
        self.frame.pack()

        # bd = define a borda do widget
        # fg = muda a cor do texto do botão.
        # widht = largura do botão
        # heigth = altura do botão
        # Cria uma grade para dimensionar os objetos.
        #row = linha
        #column = coluna
        self.button_1 = Button(self.frame, text='1', bg='orange', bd=0,
                               font='arial 20 bold', width=10, fg='white', height=4, command=lambda: self.touch('1'))

        self.button_2 = Button(self.frame, text='2', bg='orange', bd=0,
                               font='arial 20 bold', width=10, fg='white', height=4, command=lambda: self.touch('2'))

        self.button_3 = Button(self.frame, text='3', bg='orange', bd=0,
                               font='arial 20 bold', width=10, fg='white', height=4, command=lambda: self.touch('3'))

        self.button_4 = Button(self.frame, text='4', bg='orange', bd=0,
                               font='arial 20 bold', width=10, fg='white', height=4, command=lambda: self.touch('4'))

        self.button_5 = Button(self.frame, text='5', bg='orange', bd=0,
                               font='arial 20 bold', width=10, fg='white', height=4, command=lambda: self.touch('5'))

        self.button_6 = Button(self.frame, text='6', bg='orange', bd=0,
                               font='arial 20 bold', width=10, fg='white', height=4, command=lambda: self.touch('6'))

        self.button_7 = Button(self.frame, text='7', bg='orange', bd=0,
                               font='arial 20 bold', width=10, fg='white', height=4, command=lambda: self.touch('7'))

        self.button_8 = Button(self.frame, text='8', bg='orange', bd=0,
                               font='arial 20 bold', width=10, fg='white', height=4, command=lambda: self.touch('8'))

        self.button_9 = Button(self.frame, text='9', bg='orange', bd=0,
                               font='arial 20 bold', width=10, fg='white', height=4, command=lambda: self.touch('9'))

        self.button_adição = Button(self.frame, text='+', bg='#070221', bd=0,
                                    font='arial 20 bold', width=10, fg='white', height=4, command=lambda: self.touch('+'))

        self.button_subtrai = Button(self.frame, text='-', bg='#070221', bd=0,
                                     font='arial 20 bold', width=10, fg='white', height=4, command=lambda: self.touch('-'))

        self.button_divisão = Button(self.frame, text='/', bg='#070221', bd=0,
                                     font='arial 20 bold', width=10, fg='white', height=4, command=lambda: self.touch('/'))

        self.button_multiplica = Button(self.frame, text='*', bg='#070221', bd=0,
                                        font='arial 20 bold', width=10, fg='white', height=4, command=lambda: self.touch('*'))

        self.button_igual = Button(self.frame, text='=', bg='#070221', bd=0, font='arial 20 bold',
                                   width=20, fg='white', height=4, command=self.total)

        self.button_limpar = Button(self.frame, text='clear', bg='#070221', bd=0,
                                    font='arial 20 bold', width=10, fg='white', height=4, command=lambda: self.clean)

        self.button_potência = Button(self.frame, text='**', bg='#070221', bd=0,
                                      font='arial 20 bold', width=10, fg='white', height=4, command=None)

        self.button_1.grid(row=0, column=0)
        self.button_2.grid(row=0, column=1)
        self.button_3.grid(row=0, column=2)
        self.button_divisão.grid(row=0, column=3)
        self.button_4.grid(row=1, column=0)
        self.button_5.grid(row=1, column=1)
        self.button_6.grid(row=1, column=2)
        self.button_multiplica.grid(row=1, column=3)
        self.button_7.grid(row=2, column=0)
        self.button_8.grid(row=2, column=1)
        self.button_9.grid(row=2, column=2)
        self.button_adição.grid(row=2, column=3)
        self.button_subtrai.grid(row=3, column=3)
        self.button_limpar.grid(row=3, column=2)
        # columnspan = quantas colunas o botão irá ocupar no grid.
        self.button_igual.grid(row=3, column=0, columnspan=2)

        self.window.mainloop()

    def touch(self, num):
        self.screen_numbers.insert(END, num)

    @property
    def clean(self):
        self.screen_numbers.delete(0, END)
        # Método delete, limpa a tela do 0 = Inicio, até END que significa até o fim do que foi digitado.

    def total(self):
        # Eval retorna resultado de operações matemáticas.
        t = eval(self.screen_numbers.get())
        # Deleta o contéudo da tela digitado.
        self.screen_numbers.delete(0, END)
        # Insere o resultado na tela da operação matemática.
        self.screen_numbers.insert(0, str(t))

        # Métodos da Classe Calculadora


calc = Calculadora()
