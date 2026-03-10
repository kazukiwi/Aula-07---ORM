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
engine = create_engine("sqlite:///estoque.db", echo=False)

#Criar as tabelas no banco se ainda não existirem
Base.metadata.create_all(engine)

# Cria uma fábrica de sessões conectadas ao banco
Session = sessionmaker(bind=engine)

# carrinho de compras - Sessão Ativa
session = Session()

#Criar objetos produtos
produto1 = Produto("Notebook", 5500, 5, True)
produto2 = Produto("Teclado", 500, 100, True)
produto3 = Produto("Mouse", 150, 55, True)

#Adicionar os produtos na sessão
#session.add(produto1)
#session.add(produto2)
#session.add(produto3)

# Confirmar a inserção no banco
# Salvar no banco de dados
#session.commit()

#Listar 
#Buscar todos os produtos do banco
#produtos = session.query(Produto).all()

#for p in produtos:
#    print(f"Produto(id= {p.id})\n nome= {p.nome}\n preco=R$ {p.preco}\nestoque= {p.estoque}\nativo= {p.ativo}")

#Buscar produto com id = 1

#produto_id = session.query(Produto).filter(Produto.id == 1).first()
#print(produto_id)

#produto_estoque = session.query(Produto).filter(Produto.estoque >= 10).all()
#print(produto_estoque[1].nome)

#for p in produto_estoque:
#    if p.estoque >= 60:
#        print(f"Estoque cheio")
#    else:
#        print(f"Estoque de produtos: {p.estoque}")

#produto_id2 = session.query(Produto).filter_by(id=1).first()
#print(produto_id2)

#Order by
# desc() -> descrescente
# asc() -> crescente
#produtos_organizados = session.query(Produto).order_by(Produto.estoque.asc()).all()
#for produto in produtos_organizados:
#    print(f"Nome: {produto.nome}\nQtd de produtos {produto.estoque}")

#Limitar a quantidade de resultado
#produtos_mais_caros = session.query(Produto).order_by(Produto.preco.asc()).limit(5).all()
#for p in produtos_mais_caros:
    #print(f"Nome: {p.nome}, Valor: R${p.preco}")

#UPDATE (atualizar)
#Busquei o produto
notebook = session.query(Produto).filter_by(id=1).first()
notebook.preco= 7800

#Confirmar essa alteração
session.commit()
print("Preço atualizado com sucesso")

produtos = session.query(Produto).all()

for p in produtos:
    print(f"Produto(id= {p.id})\n nome= {p.nome}\n preco=R$ {p.preco}\nestoque= {p.estoque}\nativo= {p.ativo}")
