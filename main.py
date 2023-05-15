import tkinter
from  tkinter import messagebox

root = tkinter.Tk()
root.withdraw()

count = 0

msg_box = messagebox.showwarning("NOME DA PESSOA", "VOCÊ FOI HACKEADO!")
#Quando selecionado 'Ok' exibirá a mensagem que você desejar.
if msg_box == 'ok':
    msg_box = messagebox.showwarning("TÍTULO", "PRA SOLUCIONAR ISSO PRECISO QUE VOCÊ RESPONDA MINHA PERGUNTA")
    
if msg_box == 'ok':
    msg_box = messagebox.askquestion("TÍTULO DA PERGUNTA", "FAÇA UMA PERGUNTA AQUI")
#Caso seja selecionado o 'não' ele conta +1.
while msg_box == 'no':
    count += 1
    msg_box = messagebox.askquestion("TÍTULO DA PERGUNTA", "PERGUNTA NOVAMENTE")
    if (count == 5):
        #Caso seja selecionado 5 vezes o 'não' ele exibe a mensagem de erro.
        msg_box = messagebox.showerror("TITULO DO ERROR", "ESCREVA AQUI UMA MENSAGEM DE ERROR")
        break
#Caso seja selecionado yes será exibido essa mensagem.
if msg_box == 'yes':
    msg_box = messagebox.showinfo("TITULO DA INFO", "ESCREVA AQUI ALGUMA INFO")    
