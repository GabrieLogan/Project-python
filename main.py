import tkinter
from  tkinter import messagebox

root = tkinter.Tk()
root.withdraw()

count = 0

msg_box = messagebox.showwarning("NOME DA PESSOA", "VOCÊ FOI HACKEADO!")

if msg_box == 'ok':
    msg_box = messagebox.showwarning("HAHA!", "PRA SOLUCIONAR ISSO PRECISO QUE VOCÊ RESPONDA UMA PERGUNTA")
    
if msg_box == 'ok':
    msg_box = messagebox.askquestion("RESPONDA", "ESCREVA A PERGUNTA")

while msg_box == 'no':
    count += 1
    msg_box = msg_box = messagebox.askquestion("RESPONDA", "ESCREVA A PERGUNTA")
    if (count == 100):
        msg_box = messagebox.showerror("DIGA A VERDADE", "ABRA DE NOVO E DIGA A VERDADE")
        break

if msg_box == 'yes':
    msg_box = messagebox.showinfo("BOA!", "SUA MENSAGEM")    
