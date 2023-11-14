from tkinter import *
from functions import *



def tela_1(tela,titulo,geometria):
  tela = Tk(tela)
  titulo = tela.title(titulo)
  geometria = tela.geometry(geometria)
  loop = tela.mainloop()


# def tela():


# def tela_2(toplevel):
#   toplevel = Toplevel(toplevel)
#   tela_1(tela='teste 2',titulo='teste',geometria='300x300')
from tkinter import Tk, Button

def create_tela(titulo, geometria):
    tela = Tk()
    tela.title(titulo)
    tela.geometry(geometria)
    return tela

class Functions():
    def buttons(self, master,text, width, height, x, y, command=None):
        button = Button(master=master,text=text, width=width, height=height, command=command)
        button.place_configure(x=x, y=y)
        return button
    def entrys(self,master,width,x,y,**kargs):
        entrys = Entry(master=master,width=width)
        entrys.place_configure(x=x,y=y)
        return entrys
    
    def labels(self,master,text,x,y,**kargs):
        label = Label(master=master,text=text)
        label.place_configure(x=x,y=y)
        return label

class App(Functions):
    def __init__(self):
        self.root = create_tela(titulo='Janela Principal', geometria='800x400')
        self.widgets(self.root)
        self.run()
        
    def widgets(self,tela):
        wgt = Widgets()
        


    def criar_nova_tela(self):
        nova_tela = create_tela(titulo='Nova Janela', geometria='400x400')
        self.label2 = self.labels(master=nova_tela,text="Digite aqui:",x=150,y=75)
        nova_tela.mainloop()

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    App()
