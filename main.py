import tkinter
from  tkinter import messagebox

root = tkinter.Tk()
root.withdraw()

count = 0

msg_box = messagebox.showwarning("MOMO", "VOCÊ FOI HACKEADA!")

if msg_box == 'ok':
    msg_box = messagebox.showwarning("HAHA!", "PRA SOLUCIONAR ISSO PRECISO QUE VOCÊ RESPONDA ALGUMAS PERGUNTAS")
    
if msg_box == 'ok':
    msg_box = messagebox.askquestion("RESPONDA", "VOCÊ AMA SEU NAMORADO PARA SEMPRE?")

while msg_box == 'no':
    count += 1
    msg_box = msg_box = messagebox.askquestion("RESPONDA", "VOCÊ AMA SEU NAMORADO PARA SEMPRE?")
    if (count == 5):
        msg_box = messagebox.showerror("VOU TE PEGAR", "VAI TER QUE DIZER SIM HAHAHA")
        break

if msg_box == 'yes':
    msg_box = messagebox.showinfo("BOA!", "ÓTIMA ESCOLHA")    
