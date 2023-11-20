# - - - importando sqlite

import sqlite3 as lite

# - - - criando conexão 

con = lite.connect('dados.bd')

# - - - Criando tabela categoria 

with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Categoria(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)")
    
# - - - Criando tabela de receitas 

with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Receitas(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, adicionado_em DATE, valor DECIMAL)") 

# - - - Criando tabela de gastos

with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE gastos(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, retirado_em DATE, valor DECIMAL)")      
    