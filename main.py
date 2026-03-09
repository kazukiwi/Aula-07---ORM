# Importa a função responsável por criar a conexão com o banco
from sqlalchemy import create_engine

# Importa tipos de dados e estrutura das colunas
from sqlalchemy import Column, Integer, String, Float, Boolean

# Importa a classe Base usada para criar os modelos ORM
from sqlalchemy.orm import declarative_base

# Importa ferramenta para criar sessões de banco
from sqlalchemy.orm import sessionmaker