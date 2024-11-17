import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import platform

def get_hosts_path():
    if platform.system() == "Windows":
        return r"C:/Windows/System32/drivers/etc/hosts"
    elif platform.system() == "Linux":
        return "/etc/hosts"
    else:
        return None
    
def bloquear_sites():
    host_path = get_hosts_path()
    
    if not host_path:
        messagebox.showerror("Erro", "Sistema operacional não suportado.")
    return

    ip_address = "127.0.0.1"
    
    try:
        with open (hosts_path, "r+") as file:
            content = file.read()
            for palavra in palavras_bloqueadas:
                file.write(f"{ip_address} www.{palavra}.com\n")
                file.write(f"{ip_address} {palavra}.com\n")
        messagebox.showinfo("Sucesso", "Sites bloqueados com sucesso!")
        
    except PermissionError:
         messagebox.showerror("Erro", "Execute o programa como administrador.")


# Função para adicionar palavras-chave
def adicionar_palavra():
    palavra = entry_palavra.get().strip().lower()
    if palavra and palavra not in palavras_bloqueadas:
        palavras_bloqueadas.append(palavra)
        listbox_palavras.insert(tk.END, palavra)
        entry_palavra.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "Palavra inválida ou já adicionada.")
# Função para remover palavras-chave
def remover_palavra():
    try:
        selected_index = listbox_palavras.curselection()[0]
        palavra = listbox_palavras.get(selected_index)
        palavras_bloqueadas.remove(palavra)
        listbox_palavras.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Aviso", "Selecione uma palavra para remover.")
        
# Inicializar lista de palavras bloqueadas
palavras_bloqueadas = []

# Criar janela principal
janela = tk.Tk()
janela.title("Website Blocker")
janela.geometry("850x600")
janela.configure(background="lightcyan")

imagem = tk.PhotoImage(file="icon2.png")
# Criar um Label para exibir a imagem
label_imagem = tk.Label(janela, image=imagem)
label_imagem.pack()

# Campo de entrada para nova palavra-chave
label_palavra = tk.Label(janela, text="Adicionar Palavra-Chave:", font="Times", background="lightcyan")
label_palavra.pack(pady=8)
entry_palavra = tk.Entry(janela)
entry_palavra.pack(pady=8)

# Botão para adicionar palavra-chave
btn_adicionar = tk.Button(janela, text="Adicionar", font="Times", command=adicionar_palavra)
btn_adicionar.pack(pady=10)

# Lista de palavras bloqueadas
label_lista = tk.Label(janela, text="Palavras Bloqueadas:", font="Times", background="lightcyan")
label_lista.pack(pady=10)
listbox_palavras = tk.Listbox(janela)
listbox_palavras.pack(pady=10, fill=tk.BOTH, expand=True)

# Botão para remover palavra-chave
btn_remover = tk.Button(janela, text="Remover", font="Times", command=remover_palavra)
btn_remover.pack(pady=10)

# Botão para ativar bloqueio
btn_bloquear = tk.Button(janela, text="Bloquear Sites", font="Times", command=bloquear_sites)
btn_bloquear.pack(pady=10)

# Iniciar a interface
janela.mainloop()
