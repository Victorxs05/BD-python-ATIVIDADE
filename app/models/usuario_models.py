from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
from app.config.database import db 

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"
    #Definindo caracteristicas da tabela no banco de dados.

    id = Column (Integer, primary_key = True, autoincrement=True)
    nome = Column(String(150))
    email = Column(String(150), unique=True) #unique=True não aceita email ou dado repetido 
    senha = Column(String(150))

    #Definindo caracteristicas da classe.
    def __init__(self, nome: str, email: str, senha: str):
        self.nome = self._verificar_nome_usuario(nome)
        self.email = self._verficar_email_usuario(email) 
        self.senha = self._verificar_email_usuario(senha) 

    def _verificar_nome_usuario(self,nome):

        self._verificar_nome_invalido(nome)
        self._verificar_nome_vazio(nome)

        self.nome = nome
        return self.nome

    def _verificar_email_usuario(self, email):

        self._verificar_email_invalido(email)
        self._verificar_email_vazio(email)

        self.email = email
        return self.email
    
    def _verificar_senha_usuario(self, senha):

        self._verificar_senha_invalido(senha)
        self._verificar_senha_vazio(senha)

        self.senha = senha
        return self.senha
#Criando Tabela no banco de dados.
Base.metadata.create_all(bind=db)