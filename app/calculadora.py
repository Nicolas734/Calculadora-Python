from tkinter import *


calculadora = Tk()
calculadora.title("Calculadora Python")
calculadora.geometry("390x450")
calculadora.config(bg='gray')
calculadora.resizable(width=False, height=False)

conta = ""


def calcular():
    global conta
    conta = eval(conta)
    conta = str(conta)
    
    text_box['text'] = conta    


def soma():
    global conta
    adicao = '+'
    if conta[-1] == '0' or conta[-1] == '1'or conta[-1] == '2'or conta[-1] == '3'or conta[-1] == '4'or conta[-1] == '5'or conta[-1] == '6'or conta[-1] == '7'or conta[-1] == '8'or conta[-1] == '9':
        conta =  conta + str(adicao)
        text_box['text'] = conta
                     
    else:
        print("false")


def subtracao():
    global conta
    subtracao = "-"
    if conta[-1] == '0' or conta[-1] == '1'or conta[-1] == '2'or conta[-1] == '3'or conta[-1] == '4'or conta[-1] == '5'or conta[-1] == '6'or conta[-1] == '7'or conta[-1] == '8'or conta[-1] == '9':
        conta =  conta + str(subtracao)
        text_box['text'] = conta
                
    else:
        print("false")
    
        
def multiplicacao():
    global conta
    multiplicacao = "*"
    if conta[-1] == '0' or conta[-1] == '1'or conta[-1] == '2'or conta[-1] == '3'or conta[-1] == '4'or conta[-1] == '5'or conta[-1] == '6'or conta[-1] == '7'or conta[-1] == '8'or conta[-1] == '9':
        conta =  conta + str(multiplicacao)
        text_box['text'] = conta
                
    else:
        print("false")
 
        
def divisao():
    global conta
    divisao = "/"
    if conta[-1] == '0' or conta[-1] == '1'or conta[-1] == '2'or conta[-1] == '3'or conta[-1] == '4'or conta[-1] == '5'or conta[-1] == '6'or conta[-1] == '7'or conta[-1] == '8'or conta[-1] == '9':
        conta =  conta + str(divisao)
        text_box['text'] = conta
                
    else:
        print("false")
     
        
def nove():
    global conta
    nove9 = 9
    conta =  conta + str(nove9)
    text_box['text'] = conta


def oito():
    global conta
    oito8 = 8
    conta =  conta + str(oito8)
    text_box['text'] = conta


def sete():
    global conta
    sete7 = 7
    conta =  conta + str(sete7)
    text_box['text'] = conta


def seis():
    global conta
    seis6 = 6
    conta =  conta + str(seis6)
    text_box['text'] = conta


def cinco():
    global conta
    cinco5 = 5
    conta =  conta + str(cinco5)
    text_box['text'] = conta


def quatro():
    global conta
    quatro4 = 4
    conta =  conta + str(quatro4)
    text_box['text'] = conta


def tres():
    global conta
    tres3 = 3
    conta =  conta + str(tres3)
    text_box['text'] = conta


def dois():
    global conta
    dois2 = 2
    conta =  conta + str(dois2)
    text_box['text'] = conta


def um():
    global conta
    um1 = 1
    conta =  conta + str(um1)
    text_box['text'] = conta


def zero():
    global conta
    zero0 = 0
    conta =  conta + str(zero0)
    text_box['text'] = conta


def limpar():
    global conta
    conta = ""
    text_box['text'] = conta


text_box = Label(bg='white', text='', fg='black', font=('Arial 30 bold'))
text_box.place(x=15,y=20)

limpar = Button(bg='white', command=limpar, text='<', fg='black', width=3, height=1, font=('Arial 30 bold'))
limpar.place(x=288,y=5)

numero9 = Button(bg='white', command=nove, text='9', fg='black', width=3, height=1, font=('Arial 30 bold'))
numero9.place(x=18, y=90)

numero8 = Button(bg='white', command=oito, text='8', fg='black', width=3, height=1, font=('Arial 30 bold'))
numero8.place(x=108, y=90)

numero7 = Button(bg='white', command=sete, text='7', fg='black', width=3, height=1, font=('Arial 30 bold'))
numero7.place(x=198, y=90)

opercao_soma = Button(bg='white', command=soma,  text='+', fg='black', width=3, height=1, font=('Arial 30 bold'))
opercao_soma.place(x=288, y=90)

numero6 = Button(bg='white', command=seis, text='6', fg='black', width=3, height=1, font=('Arial 30 bold'))
numero6.place(x=18, y=180)

numero5 = Button(bg='white', command=cinco, text='5', fg='black', width=3, height=1, font=('Arial 30 bold'))
numero5.place(x=108, y=180)

numero4 = Button(bg='white', command=quatro, text='4', fg='black', width=3, height=1, font=('Arial 30 bold'))
numero4.place(x=198, y=180)

opercao_subtrair = Button(bg='white', command=subtracao,  text='-', fg='black', width=3, height=1, font=('Arial 30 bold'))
opercao_subtrair.place(x=288, y=180)

numero3 = Button(bg='white', command=tres, text='3', fg='black', width=3, height=1, font=('Arial 30 bold'))
numero3.place(x=18, y=270)

numero2 = Button(bg='white', command=dois, text='2', fg='black', width=3, height=1, font=('Arial 30 bold'))
numero2.place(x=108, y=270)

numero1 = Button(bg='white', command=um, text='1', fg='black', width=3, height=1, font=('Arial 30 bold'))
numero1.place(x=198, y=270)

opercao_multiplicacao = Button(bg='white', command=multiplicacao,  text='*', fg='black', width=3, height=1, font=('Arial 30 bold'))
opercao_multiplicacao.place(x=288, y=270)

numero0 = Button(bg='white', command=zero, text='0', fg='black', width=6, height=1, font=('Arial 30 bold'))
numero0.place(x=18, y=360)

resultado = Button(bg='white', command=calcular, text='=', fg='black', width=4, height=1, font=('Arial 30 bold'))
resultado.place(x=175, y=360)

opercao_divisao = Button(bg='white', command=divisao, text='/', fg='black', width=3, height=1, font=('Arial 30 bold'))
opercao_divisao.place(x=288, y=360)

calculadora.mainloop()