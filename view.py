# - - - importando sqlite

import sqlite3 as lite
import pandas as pd

# - - - criando conexão 

con = lite.connect('dados.bd')


# - - - inserir categoria  - - Criando nova categoria
def inserir_categoria(i):   
 with con:
  cur = con.cursor()
  query = "INSERT INTO Categoria (nome) VALUES (?)"
  cur.execute(query,i)


# - - - inserir receitas  - - Criando nova receita
def inserir_receita(i):    
 with con:
  cur = con.cursor()
  query = "INSERT INTO Receitas (categoria, adicionado_em,valor) VALUES (?,?,?)"
  cur.execute(query,i)
 
 
# - - - inserir gatos  - - Criando nova tabela gastos 
def inserir_gasto(i):   
 with con:
  cur = con.cursor()
  query = "INSERT INTO gastos (categoria, retirado_em,valor) VALUES (?,?,?)"
  cur.execute(query,i)
 
 
 #  - - - - Funções para deletar
 
 #  - - - - Deletar receitas
 
def deletar_receita(i):
  with con:
      cur = con.cursor()
      query = "DELETE FROM Receitas WHERE id=?"
      cur.execute(query,i)
     
     
 #  - - - - Deletar gastos
 
def deletar_gastos(i): 
 with con:
     cur = con.cursor()
     query = "DELETE FROM gastos WHERE id=?"
     cur.execute(query,i)
     
# - - - - FUNÇÕES PARA VER DADOS

# - - - Ver categoria

def ver_categoria():
    lista_itens = []
 
    with con:
      cur = con.cursor()
      cur.execute("SELECT * FROM Categoria")
      linha = cur.fetchall()
      for l in linha:
          lista_itens.append(l)
          
    return lista_itens

         
         
# - - - Ver receitas

def ver_receitas():
    lista_itens = []
 
    with con:
      cur = con.cursor()
      cur.execute("SELECT * FROM Receitas")
      linha = cur.fetchall()
      for l in linha:
          lista_itens.append(l)
          
    return lista_itens

# - - - Ver gastos

def ver_gastos():
    lista_itens = []
 
    with con:
      cur = con.cursor()
      cur.execute("SELECT * FROM gastos")
      linha = cur.fetchall()
      for l in linha:
          lista_itens.append(l)
          
    return lista_itens 
          
# - -Função para dados tabela
def tabela():
    gastos = ver_gastos()
    receitas = ver_receitas()
    
    tabela_lista = []
    
    for i in gastos:
      tabela_lista.append(i)
      
    for i in receitas:
      tabela_lista.append(i)           
    
    return tabela_lista


          
          
# - Função para grafico de barras

def bar_valores():
   # - - Valor total da receita
     receitas = ver_receitas()
     receitas_lista = []
  
     for i in receitas:
         receitas_lista.append(i[3])
  
     receita_total = sum(receitas_lista)
   
   # = - Despesas total
     gastos = ver_gastos()
     gastos_lista = []
   
     for i in gastos:
         gastos_lista.append(i[3])
     
     gasto_total = sum(gastos_lista)
    
   # - - Saldo total
     saldo_total = receita_total - gasto_total
   
     return[receita_total,gasto_total,saldo_total]
     
# - - Função grafico pie
def pie_valores():
  gastos = ver_gastos()
  tabela_lista = []
  
  for i in gastos:
      tabela_lista.append(i)
    
  dataframe = pd.DataFrame(tabela_lista, columns = ['id', 'categoria', 'Data', 'valor'])
  dataframe = dataframe.groupby('categoria')['valor'].sum()
    
  lista_quantias = dataframe.values.tolist()
  lista_categorias = []
    
  for i in dataframe.index:
      lista_categorias.append(i)
      
  return([lista_categorias, lista_quantias])
    
# - Função porcentagem

def porcentagem_valor():
   # - - Valor total da receita
     receitas = ver_receitas()
     receitas_lista = []
  
     for i in receitas:
         receitas_lista.append(i[3])
  
     receita_total = sum(receitas_lista)
   
   # = - Despesas total
     gastos = ver_gastos()
     gastos_lista = []
   
     for i in gastos:
         gastos_lista.append(i[3])
     
     gasto_total = sum(gastos_lista)
    
   # - - Porcentagem total
     total = ((receita_total - gasto_total) / receita_total) * 100
   
     return[total]
  
