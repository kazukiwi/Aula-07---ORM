# Importa a função responsável por criar a conexão com o banco
from sqlalchemy import create_engine

# Importa tipos de dados e estrutura das colunas
from sqlalchemy import Column, Integer, String, Float, Boolean

# Importa a classe Base usada para criar os modelos ORM
from sqlalchemy.orm import declarative_base

# Importa ferramenta para criar sessões de banco
from sqlalchemy.orm import sessionmaker

# Criar classe base do ORM
Base = declarative_base()

# Classe - Tabela
# Objeto - linha Tabela
# Atributos - Coluna

# Classe Produto representando uma tabela no banco de dados
class Produto(Base):
    #Nome da tabela no banco
    __tablename__ = "produtos"

    #Criar coluna id
    # Integer > número inteiro
    # Primary_key > True
    id = Column(Integer, primary_key=True)

    #Nome do produto
    # String > texto
    nome = Column(String(100))

    #Preço do produto
    # Float > Número decimal
    preco = Column(Float)

    #Quantidade em estoque
    estoque = Column(Integer)

    #Produto ativo ou não
    ativo = Column(Boolean)

    # Metodo Construtor
    def __init__(self, nome, preco, estoque, ativo):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        self.ativo = ativo

    # Representação do objeto para imprimir
    def __repr__(self):
        return f"Produto(id= {self.id})\n nome= {self.nome}\n preco=R$ {self.preco}\nestoque= {self.estoque}\nativo= {self.ativo}"
    
#Criar a conexão com sqlite
engine = create_engine("sqlite:///estoque.db", echo=True)

#Criar as tabelas no banco se ainda não existirem
Base.metadata.create_all(engine)