import tkinter 
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk 
from tkinter import messagebox

# - - - Importando barra de progresso do matplot Tkinter

from customtkinter import CTkProgressBar

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

# - - Importar tkcalendar
from tkcalendar import Calendar, DateEntry
from datetime import date

# - - Importando funções da view

from view import bar_valores, pie_valores, porcentagem_valor, inserir_categoria, inserir_receita, inserir_gasto, ver_categoria, tabela, deletar_gastos, deletar_receita




# cores
co0 = "#2e2db" # preta
co1 = "#feffff" #branca
co02 = "#4fa882" #verde
co03 = "#38576b" #valor
co04 = "#403dd3d" #letra
co05 = "#e06636"
co06 = "#038cfc"
co07 = "#3fbfb9"
co08 = "#263238"
co09 = "#e9edf5"

colors = ['#5588bb', '#66bbbb', '#99bb55', '#ee9944', '#444466', '#bb5555']









janela = ctk.CTk()

ctk.set_appearance_mode("Light")
janela.title("Orçamento pessoal")
janela.geometry("1050x680")
janela.resizable(False, False)
# - - Criando frame 1

frame_cima = ctk.CTkFrame(janela, width=1050, height=50, )
frame_cima.grid(row=0, column=0)

# - - Criando frame 2

frame_meio = ctk.CTkFrame(janela, width=1050, height=361)
frame_meio.grid(row=1, column=0, pady=1, padx=0)

# - - Criando frame 3

frame_baixo = ctk.CTkFrame(janela, width=1050, height=361)
frame_baixo.grid(row=2, column=0, pady=10, padx=0)

# - - frame gra_pie



# - - -Trabalhando no frame cima

# - - - Acessando a imgem

#app_img = ImageTk.open(photo='log.png')
#app_img = app_img.resize((45, 45))
#app_img = ImageTk.PhotoImage(app_img)

app_log = ctk.CTkLabel(master=frame_cima, text=" Controle de orçamento", width=900, font=ctk.CTkFont('Gills san', size=25))
app_log.place(relx=0.05, rely=0)

# - - Definindo tree como global
global tree

# - - Função inserir categoria 

def inserir_categoria_b():
    nome = combo_categoria_receitas.get()
    lista_inserir = [nome]
    
    for i in lista_inserir:
        if i=='':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return
    # - - Passando para a função inserir gastos presente na view
    inserir_categoria(lista_inserir)       
    messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')
    
    combo_categoria_receitas.delete(0, 'end')
    
    # - - Pegando os valores da categoria 
    categorias_funcao = ver_categoria()
    categoria = []
    
    for i in categorias_funcao:
        categoria.append(i[1])
        
    # - - Atualizando  lista de categorias 
    combo_categoria_despesas['values'] = (categoria)
    
    # - - Funçao inserir receitas
    
# - - Funçao inserir receitas
    
def inserir_receitas_b():
        
        nome = 'Receita'
        data = e_cal_receitas.get()
        quantia = e_valor_receitas.get()
        
        lista_inserir = [nome, data, quantia]
        
        
        for i in lista_inserir:
            if i=='':
               messagebox.showerror('Erro', 'Preencha todos os campos')
               return
        
        #chamando a função  inserir receita presente na view
        
        inserir_receita(lista_inserir)
        
        messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')
        
        e_cal_receitas.delete(0, 'end')
        e_valor_receitas.delete(0, 'end')
        
        # - - Atualizando dados 
        
        mostrar_renda()
        porcentagem()
        grafico_bar()
        resumo()
        grafico_pie()
        
# - - Função inserir despesas

def inserir_despesas_b():
        
        nome = combo_categoria_despesas.get()
        data = e_cal_despesas.get()
        quantia = e_valor_despesas.get()
    
        
        lista_inserir = [nome, data, quantia]
        
        
        for i in lista_inserir:
            if i=='':
               messagebox.showerror('Erro', 'Preencha todos os campos')
               return
        
        #chamando a função  inserir despesas presente na view
        
        inserir_gasto(lista_inserir)
        
        messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')
        
        combo_categoria_despesas.delete(0, 'end')
        e_cal_despesas.delete(0, 'end')
        e_valor_despesas.delete(0, 'end')
        
        # - - Atualizando dados 
        
        mostrar_renda()
        porcentagem()
        grafico_bar()
        resumo()
        grafico_pie()
        
# - - Inserir receitas - salario 





        
# - - Função deletar

def deletar_dados():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']
        valor = treev_lista[0]
        nome = treev_lista[1]
        
        if nome == 'Receita':
            deletar_receita([valor])
            messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso')
        
            # - - Atualizando dados        
            mostrar_renda()
            porcentagem()
            grafico_bar()
            resumo()
            grafico_pie()

        else:
            deletar_gastos([valor])
            messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso')    
        
            # - - Atualizando dados        
            mostrar_renda()
            porcentagem()
            grafico_bar()
            resumo()
            grafico_pie()
        
    except IndexError:
        messagebox.showerror('Erro', 'Selecione um dos dados na tabela')
        


    






# - - - Porcentagem 

def porcentagem():
    l_nome = ctk.CTkLabel(master=frame_meio, text="Saldo restante", height=1, font=ctk.CTkFont('Gills san', size=15))
    l_nome.place(x=7, y=5)
    valor = porcentagem_valor()[0]
    bar = ttk.Progressbar(frame_meio, maximum=100)
    #bar.start()
    #bar.stop()
    #bar.step()
    bar.place(x=7, y=35, height=10, width=100)
    bar['value'] = porcentagem_valor()[0]
    
    
    valor = porcentagem_valor()[0]
    
    l_porcentagem = ctk.CTkLabel(master=frame_meio, text="{:,.2f}%".format(valor), height=1, font=ctk.CTkFont('Gills san', size=15))
    l_porcentagem.place(x=203, y=32)
    
    
    
# - - Função para gráfico bar

def grafico_bar():
    lista_categorias = ['Renda', 'Despesas', 'Saldo']
    lista_valores = bar_valores()
    
    #faça figura e atribua objetos de eixo
    figura = plt.Figure(figsize=(4, 3.45), dpi=60)
    ax = figura.add_subplot(111)
    #ax.autoscale(enable=True, axis='both', tight=None)

    ax.bar(lista_categorias, lista_valores,  color=colors, width=0.9)
    #create a list to collect the plt.patches data

    c = 0
    #set individual bar lables using above list
    for i in ax.patches:
        #get_x pulls left or right; get_height pushes up or down
        ax.text(i.get_x()-.001, i.get_height()+.5,
                str("{:,.0f}".format(lista_valores[c])), fontsize=17, fontstyle='italic',  verticalalignment='bottom',color='dimgrey')
        c += 1

    ax.set_xticklabels(lista_categorias, fontsize=16)
    #plt.rcParams['axes.facecolor'] = '#252ae2'
    ax.patch.set_facecolor('#ffffff')
    ax.spines['bottom'].set_color('#9a9a9a')
    ax.spines['bottom'].set_linewidth(1)
    ax.spines['right'].set_linewidth(0)
    ax.spines['top'].set_linewidth(0)
    ax.spines['left'].set_color('#3e4144')
    ax.spines['left'].set_linewidth(1)
    #plt.rcParams['figure.facecolor'] = '#ffffff'
    

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(bottom=False, left=False)
    ax.set_axisbelow(True)
    ax.yaxis.grid(False, color='#EEEEEE')
    ax.xaxis.grid(False)

    canva = FigureCanvasTkAgg(figura, frame_meio)
    canva.get_tk_widget().place(x=10, y=70)


# - - - Função de resumo total 
def resumo():
    valor = bar_valores()
    # - - Total da renda
    l_linha = ctk.CTkLabel(master=frame_meio, text=" ", height=1, width=215, font=ctk.CTkFont('Arial', size=1), bg_color="White")
    l_linha.place(x=309, y=60)
    l_sumario = ctk.CTkLabel(master=frame_meio, text="Total Renda Mensal      ".upper(), font=ctk.CTkFont('Verdana', size=12))
    l_sumario.place(x=309, y=30)
    l_sumario = ctk.CTkLabel(master=frame_meio, text="R$ {:,.2F}".format(valor[0]), font=ctk.CTkFont('Arial', size=17))
    l_sumario.place(x=309, y=70)
    # - - Total despesas mensal
    l_linha = ctk.CTkLabel(master=frame_meio, text=" ", height=1, width=215, font=ctk.CTkFont('Arial', size=1), bg_color="White")
    l_linha.place(x=309, y=140)
    l_sumario = ctk.CTkLabel(master=frame_meio, text="Total de despesas mensais      ".upper(), font=ctk.CTkFont('Verdana', size=12))
    l_sumario.place(x=309, y=110)
    l_sumario = ctk.CTkLabel(master=frame_meio, text="R$ {:,.2F}".format(valor[1]), font=ctk.CTkFont('Arial', size=17))
    l_sumario.place(x=309, y=150)
    # - - Total de saldo
    l_linha = ctk.CTkLabel(master=frame_meio, text=" ", height=1, width=215, font=ctk.CTkFont('Arial', size=1), bg_color="White")
    l_linha.place(x=309, y=220)
    l_sumario = ctk.CTkLabel(master=frame_meio, text="Total do saldo      ".upper(), font=ctk.CTkFont('Verdana', size=12))
    l_sumario.place(x=309, y=190)
    l_sumario = ctk.CTkLabel(master=frame_meio, text="R$ {:,.2F}".format(valor[2]), font=ctk.CTkFont('Arial', size=17))
    l_sumario.place(x=309, y=230)
    
    
    
# - - - Função gráfico pie
 

def grafico_pie():
   # faça figura e atribua objetos de eixo
    figura = plt.Figure(figsize=(5, 3), dpi=90)
    ax = figura.add_subplot(111)

    lista_valores = pie_valores()[1]
    lista_categorias = pie_valores()[0]
    #only "explode" the 2nd slice (i.e. 'Hogs')

    explode = []
    for i in lista_categorias:
        explode.append(0.05)

    ax.pie(lista_valores, explode=explode, wedgeprops=dict(width=0.2), autopct='%1.1f%%', colors=colors,shadow=True, startangle=90)
    ax.legend(lista_categorias, loc="center right", bbox_to_anchor=(1.55, 0.50))

    canva_categoria = FigureCanvasTkAgg(figura, frame_meio)
    canva_categoria.get_tk_widget().place(x=560, y=40)
    




porcentagem()
grafico_bar()
resumo()
grafico_pie()

# - - Criando frame dentro do frame_baixo
frame_renda = ctk.CTkFrame(master=frame_baixo, width=490, height=250, )
frame_renda.grid(row=1, column=0)

frame_operacoes = ctk.CTkFrame(master=frame_baixo, width=220, height=250, )
frame_operacoes.grid(row=1, column=1, padx=4)

frame_configuracao = ctk.CTkFrame(master=frame_baixo, width=312, height=250, )
frame_configuracao.grid(row=1, column=4, padx=5)

# - - Tabela renda mensal

app_tabela = ctk.CTkLabel(master=frame_meio, text="Tabela receitas e despesas", font=ctk.CTkFont('Gills san', size=15))
app_tabela.place(x=5, y=318)

# - - Função para mostrar renda

def mostrar_renda():

 #creating a treeview with dual scrollbars
    tabela_head = ['#Id','Categoria','Data','Quantia', '      ']

    lista_itens = tabela()
    
    global tree

    tree = ttk.Treeview(master=frame_renda, selectmode="extended",columns=tabela_head, show="headings")
    #vertical scrollbar
    vsb = ctk.CTkScrollbar(master=frame_renda, orientation="vertical", command=tree.yview, width=15, )
    #horizontal scrollbar
    hsb = ctk.CTkScrollbar(master=frame_renda, orientation="horizontal", command=tree.xview, width=430)
    #hsb.place(x=0, y=1)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, padx=0, pady=1, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    hd=["center","center","center", "center", "center"]
    h=[30,100,100,100,130]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title())
        #adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in lista_itens:
        tree.insert('', 'end', values=item)

mostrar_renda()

# - - Configurações de despesas

el_info = ctk.CTkLabel(master=frame_operacoes, text="Insira novas despesas", font=ctk.CTkFont('Gills san', size=15), height=1)
el_info.place(x=10, y=10)

# - - Categoria label
e_receitas_categoria = ctk.CTkLabel(master=frame_operacoes, text="Categoria", font=ctk.CTkFont('Ivy', size=13), height=1)
e_receitas_categoria.place(x=10, y=44)

# - - Pegando categorias
categoria_funcao = ver_categoria()
categoria = []

for i in categoria_funcao:
    categoria.append(i[1])
    
combo_categoria_despesas = ttk.Combobox(master=frame_operacoes, width=8, font=('Ivy'))
combo_categoria_despesas['values'] = (categoria)
combo_categoria_despesas.place(x=95, y=38)

# - - despesas label
l_cal_despesas = ctk.CTkLabel(master=frame_operacoes, text="Data", font=ctk.CTkFont('Ivy', size=13), height=1)
l_cal_despesas.place(x=10, y=74)

e_cal_despesas = DateEntry(master=frame_operacoes, width=9, bg_color='darkblue', year=2023, fareground='Black', theme='Dark')
e_cal_despesas.place(x=95, y=74)

# - - Valor

l_valor_despesas = ctk.CTkLabel(master=frame_operacoes, text="Quantia total", font=ctk.CTkFont('Ivy', size=13), height=1)
l_valor_despesas.place(x=10, y=112)

e_valor_despesas = ctk.CTkEntry(master=frame_operacoes, width=96)
e_valor_despesas.place(x=95, y=107)

# - - Botão inserir
botao_inserir_despesas = ctk.CTkButton(master=frame_operacoes, command=inserir_despesas_b, text='Inserir', width=96, hover_color='green')
botao_inserir_despesas.place(x=95, y=150)

# - - Botão excluir
l_excluir = ctk.CTkLabel(master=frame_operacoes, text="Excluir ação", font=ctk.CTkFont('Ivy', size=13), height=1)
l_excluir.place(x=10, y=194)


botao_deletar = ctk.CTkButton(master=frame_operacoes, command=deletar_dados, text='Excluir', width=96, hover_color='red')
botao_deletar.place(x=95, y=190)

# - - Configurações receitas

el_info = ctk.CTkLabel(master=frame_configuracao, text="Insira novas receitas", font=ctk.CTkFont('Gills san', size=15), height=1)
el_info.place(x=10, y=10)

# - -  Calendario 2
l_cal_receitas = ctk.CTkLabel(master=frame_configuracao, text="Data", font=ctk.CTkFont('Ivy', size=13), height=1)
l_cal_receitas.place(x=10, y=44)

e_cal_receitas = DateEntry(master=frame_configuracao, width=9, bg_color='darkblue', year=2023, fareground='Black', theme='Dark')
e_cal_receitas.place(x=95, y=42)

# - - Valor receitas

l_valor_receitas = ctk.CTkLabel(master=frame_configuracao, text="Quantia total", font=ctk.CTkFont('Ivy', size=13), height=1)
l_valor_receitas.place(x=10, y=76)

e_valor_receitas = ctk.CTkEntry(master=frame_configuracao, width=96)
e_valor_receitas.place(x=95, y=73)


# - - Botão inserir receitas
botao_inserir_receitas = ctk.CTkButton(master=frame_configuracao, command=inserir_receitas_b, text='Inserir', width=96, hover_color='green')
botao_inserir_receitas.place(x=95, y=108)

# - - Categoria receitas label
el_categoria_receitas = ctk.CTkLabel(master=frame_configuracao, text="Categoria", font=ctk.CTkFont('Ivy', size=13), height=1)
el_categoria_receitas.place(x=10, y=155)

combo_categoria_receitas = ctk.CTkEntry(master=frame_configuracao, width=94, font=ctk.CTkFont('Ivy', size=12))
#combo_categoria_receitas['values'] = (categoria)
combo_categoria_receitas.place(x=95, y=150)

# - - Botão inserir receitas
botao_inserir_categoria = ctk.CTkButton(master=frame_configuracao, command=inserir_categoria_b,text='Inserir', width=96, hover_color='green')
botao_inserir_categoria.place(x=95, y=190)

janela.mainloop()
