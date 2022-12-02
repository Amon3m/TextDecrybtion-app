import re
import string
from tkinter import messagebox

from tkinter import*
gui_dec =  Tk()
gui_dec.title("Decryption Tool")
gui_dec.geometry('630x390')
gui_dec.resizable(False, False)
gui_dec.configure(background="#23ada6")

##decryption--------------

ciphertext_widget = Label(gui_dec,text="Enter cipher text",height=2,bg ="#080707", fg = "white", font =("Arial", 20 ), bd=2)
ciphertext_widget.place(x=7, y=80, height=38)


ciphertext= StringVar()
ciphertext_input= Entry(gui_dec, width =30 ,bd=5,  textvariable =ciphertext)
ciphertext_input.place(x=35, y=122)


ciphertext_widget = Label(gui_dec,text="Enter the key (a)",height=2,bg ="#080707", fg = "white", font =("Arial", 20 ), bd=2)
ciphertext_widget.place(x=7, y=160, height=38)

key= StringVar()
key_input= Entry(gui_dec, width =30 ,bd=5, textvariable =key)
key_input.place(x=35, y=210)

ciphertext_widget = Label(gui_dec,text="Enter the key (b)",height=2,bg ="#080707", fg = "white", font =("Arial", 20 ), bd=2)
ciphertext_widget.place(x=7, y=250, height=38)

key2= StringVar()
key_input2= Entry(gui_dec, width =30 ,bd=5, textvariable =key2)
key_input2.place(x=35, y=300)
##ceaser----------
def ceaser():
    Alphabet = string.ascii_uppercase
    ciphertext_value = ciphertext.get().upper()
    key_1 = int(key.get())
    Decryption_ceaser = ""
    if key_1>26:
        key_1 %= 26
    for i in range(len(ciphertext_value)):
        n=ciphertext_value[i]
        index=Alphabet.find(n)
        c = (index-key_1)%26
        Decryption_ceaser += Alphabet[c]
    print( " Decryption ", Decryption_ceaser )
    messagebox.showinfo("Decryption : ", "Decryption : " + Decryption_ceaser)
##affine----------
def affine():
        import string
        Alphabet = string.ascii_uppercase
        plaintext_value = ciphertext.get().upper()
        key_1 = int(key.get())
        key_2 = int(key2.get())
        if key_2 > 26:
            key_2 % 26

        Decryption_Affine = ""

        for i in range(len(plaintext_value)):
            n = plaintext_value[i]

            index = Alphabet.find(n)
            c = (key_1 * index + key_2) % 26
            c = pow(int(key_1), -1, 26) * (Alphabet.index(plaintext_value[i].upper()) - int( key_2)) % 26
            Decryption_Affine += Alphabet[c]

        for i in range(key_1):
            if key_1 == [2, 4, 6, 8, 10, 12, 13, 14, 16, 18, 20, 22, 24]:
                key1 = int(key.get())
        print(" Decryption ", Decryption_Affine)
        messagebox.showinfo(" Decryption : ", " Decryption : " + Decryption_Affine)
#---------------------------------
ceaserdec_ptn =Button (gui_dec,text="ceaser decryption ",height=2, font =("Arial", 20 ),bg ="#e91e63", fg = "white" ,borderwidth=5,command=ceaser)
ceaserdec_ptn.place(x=320,y=110)


affinedec_ptn =Button (gui_dec,text="affine decryption ",height=2, font =("Arial", 20 ),bg ="#e91e63", fg = "white" ,borderwidth=5,command=affine)
affinedec_ptn.place(x=320 , y= 210)
gui_dec.mainloop()
##-------------
