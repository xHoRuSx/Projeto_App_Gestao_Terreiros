import customtkinter as ctk
from tkinter import *
from PIL import Image

tela_login = ctk.CTk()

tela_login.title('Casa de Caridade Caboclo Estrela da Manhã e Cabocla Sete Ventos')
tela_login.geometry('700x500')
ctk.set_appearance_mode('system')
ctk.set_default_color_theme('dark-blue')

def clique_botao_login():
    print('Teste ok!')

logo = ctk.CTkImage(light_image=Image.open('C:/Users/Intel/OneDrive/Desktop/Meus_Projetos/Projeto_App_Gestao_Terreiro/Projeto_App_Gestao_Terreiros/imagens/Logo.jpg'), 
                    dark_image=Image.open('C:/Users/Intel/OneDrive/Desktop/Meus_Projetos/Projeto_App_Gestao_Terreiro/Projeto_App_Gestao_Terreiros/imagens/Logo.jpg'), 
                    size=(250, 250))
imagem_receptivo = ctk.CTkLabel(tela_login, image=logo, fg_color='transparent').pack()

texto_receptivo = ctk.CTkLabel(tela_login, text='Bem-Vindo a CCCEM!', font=('Times New Romama', 15))
texto_receptivo.pack(padx=10, pady=10)

cpf = ctk.CTkEntry(tela_login, placeholder_text='Login')
cpf.pack(padx=10, pady=10)

senha = ctk.CTkEntry(tela_login, placeholder_text='Senha', show='*')
senha.pack(padx=10, pady=10)

lembrar_login = ctk.CTkCheckBox(tela_login, text='Lembrar login', font=('Times New Romam', 12))
lembrar_login.pack(padx=10, pady=10)

botao = ctk.CTkButton(tela_login, text='Acessar', command=clique_botao_login)
botao.pack(padx=10, pady=10)

texto_mensagem = ctk.CTkLabel(tela_login, text='')
texto_mensagem.pack(padx=10, pady=10)

tela_login.mainloop()
