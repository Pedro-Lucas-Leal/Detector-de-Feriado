import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
import os
from pypdf import PdfReader

def exibir_texto_pdf(texto):
    
    janela_texto = tk.Toplevel()
    janela_texto.title("Conteúdo do PDF")
    janela_texto.geometry("600x400")
    area_texto = scrolledtext.ScrolledText(janela_texto, wrap=tk.WORD, font=("Arial", 10))
    area_texto.pack(expand=True, fill='both', padx=10, pady=10)
    area_texto.insert(tk.INSERT, texto)
    area_texto.config(state=tk.DISABLED)

def extrair_pdf():
    
    caminho_arquivo = filedialog.askopenfilename(
        title="Selecione um Arquivo PDF",
        filetypes=(("Arquivos PDF", "*.pdf"), ("Todos os Arquivos", "*.*"))
    )

    reader = PdfReader(caminho_arquivo)
    texto_completo = ""
            
    for pagina in reader.pages:
        texto_completo += pagina.extract_text()   
    exibir_texto_pdf(texto_completo)

janela = tk.Tk()
janela.title("Abrir PDF")
janela.geometry("300x120")

rotulo = tk.Label(janela, text="Selecione um PDF para abrir.")
rotulo.pack(pady=15)

botao_abrir = tk.Button(
    janela, 
    text="Selecionar PDF", 
    command=extrair_pdf
)
botao_abrir.pack(pady=5)

janela.mainloop()
