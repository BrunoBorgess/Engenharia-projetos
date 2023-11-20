import sqlite3 as lite

con = lite.connect('dados.bd')


with con:
    cur = con.cursor()
    cur.execute("DELETE FROM Categoria ")
    con.commit()
    
    
    print("Dados apagados!")
    
   # print("Operaçãor concluida")