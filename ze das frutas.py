import tkinter as tk
from tkinter import messagebox

# Definindo a classe de produtos
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

# Definindo a classe de cliente
class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

# Funções do menu
produtos = []
clientes = []
vendas = []

# Função para cadastrar produtos
def cadastrar_produto():
    def salvar_produto():
        nome = entry_nome_produto.get()
        preco = entry_preco_produto.get()
        if nome and preco:
            produtos.append(Produto(nome, float(preco)))
            messagebox.showinfo("Cadastro de Produto", "Produto cadastrado com sucesso!")
            janela_produto.destroy()
        else:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")

    janela_produto = tk.Toplevel()
    janela_produto.title("Cadastro de Produto")
    tk.Label(janela_produto, text="Nome do Produto:").pack()
    entry_nome_produto = tk.Entry(janela_produto)
    entry_nome_produto.pack()
    
    tk.Label(janela_produto, text="Preço do Produto:").pack()
    entry_preco_produto = tk.Entry(janela_produto)
    entry_preco_produto.pack()
    
    tk.Button(janela_produto, text="Cadastrar", command=salvar_produto).pack()

# Função para cadastrar clientes
def cadastrar_cliente():
    def salvar_cliente():
        nome = entry_nome_cliente.get()
        telefone = entry_telefone_cliente.get()
        if nome and telefone:
            clientes.append(Cliente(nome, telefone))
            messagebox.showinfo("Cadastro de Cliente", "Cliente cadastrado com sucesso!")
            janela_cliente.destroy()
        else:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")

    janela_cliente = tk.Toplevel()
    janela_cliente.title("Cadastro de Cliente")
    tk.Label(janela_cliente, text="Nome do Cliente:").pack()
    entry_nome_cliente = tk.Entry(janela_cliente)
    entry_nome_cliente.pack()

    tk.Label(janela_cliente, text="Telefone do Cliente:").pack()
    entry_telefone_cliente = tk.Entry(janela_cliente)
    entry_telefone_cliente.pack()

    tk.Button(janela_cliente, text="Cadastrar", command=salvar_cliente).pack()

# Função para realizar vendas
def realizar_venda():
    def finalizar_venda():
        cliente_nome = entry_cliente_nome.get()
        produto_nome = entry_produto_nome.get()
        quantidade = entry_quantidade.get()

        if cliente_nome and produto_nome and quantidade:
            # Encontra cliente e produto
            cliente = next((c for c in clientes if c.nome == cliente_nome), None)
            produto = next((p for p in produtos if p.nome == produto_nome), None)
            
            if cliente and produto:
                total = produto.preco * int(quantidade)
                vendas.append((cliente.nome, produto.nome, quantidade, total))
                messagebox.showinfo("Venda Realizada", f"Venda concluída! Total: R${total:.2f}")
                janela_venda.destroy()
            else:
                messagebox.showerror("Erro", "Cliente ou produto não encontrado!")
        else:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")

    janela_venda = tk.Toplevel()
    janela_venda.title("Realizar Venda")
    
    tk.Label(janela_venda, text="Nome do Cliente:").pack()
    entry_cliente_nome = tk.Entry(janela_venda)
    entry_cliente_nome.pack()
    
    tk.Label(janela_venda, text="Nome do Produto:").pack()
    entry_produto_nome = tk.Entry(janela_venda)
    entry_produto_nome.pack()
    
    tk.Label(janela_venda, text="Quantidade:").pack()
    entry_quantidade = tk.Entry(janela_venda)
    entry_quantidade.pack()

    tk.Button(janela_venda, text="Finalizar Venda", command=finalizar_venda).pack()

# Função para visualizar vendas
def visualizar_vendas():
    vendas_str = "Vendas Realizadas:\n"
    if vendas:
        for venda in vendas:
            vendas_str += f"Cliente: {venda[0]} | Produto: {venda[1]} | Quantidade: {venda[2]} | Total: R${venda[3]:.2f}\n"
    else:
        vendas_str = "Nenhuma venda realizada até o momento."
    
    messagebox.showinfo("Visualizar Vendas", vendas_str)

# Função para exibir o menu principal
def menu_principal():
    janela_menu = tk.Tk()
    janela_menu.title("Bem-vindo ao Hotifruti")
    
    tk.Label(janela_menu, text="Menu de Opções", font=("Arial", 16)).pack(pady=10)
    
    tk.Button(janela_menu, text="Cadastro de Produtos", width=30, command=cadastrar_produto).pack(pady=5)
    tk.Button(janela_menu, text="Cadastro de Clientes", width=30, command=cadastrar_cliente).pack(pady=5)
    tk.Button(janela_menu, text="Realizar Venda", width=30, command=realizar_venda).pack(pady=5)
    tk.Button(janela_menu, text="Visualizar Vendas", width=30, command=visualizar_vendas).pack(pady=5)
    tk.Button(janela_menu, text="Sair", width=30, command=janela_menu.quit).pack(pady=5)
    
    janela_menu.mainloop()

# Iniciar o programa
if __name__ == "__main__":
    menu_principal()
