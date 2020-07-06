import sqlite3

conn = sqlite3.connect("clientes.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes(
    Name TEXT NOT NULL,
    Cpf TEXT NOT NULL,
    Number TEXT NOT NULL,
    Data TEXT NOT NULL,
    Horario TEXT NOT NULL,
    Profissional TEXT NOT NULL);
""")

print('Conectado ao banco de dados')
