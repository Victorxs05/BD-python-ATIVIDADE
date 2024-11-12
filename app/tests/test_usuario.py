import pytest
import os 
from app.models.usuario_models import Usuario
from app.config.database import db

os.system("cls||clear")

@pytest.fixture 

def usuario_valido():
    usuario = Usuario("Neymar", "neymar@gmail.com", "1234")
    return usuario

def test_nome_valido(usuario_valido):
    assert usuario_valido.nome == "Neymar"

def test_email_valido(usuario_valido):
    assert usuario_valido.email == "neymar@gmail.com"

def test_senha_valida(usuario_valido):
    assert usuario_valido.senha == "1234"

def test_nome_vazio():
    with pytest.raises(ValueError, match="O que está sendo solicitado está inválido."):
        Usuario("", "neymar@gmail.com", "1234")

def test_usuario_nome_invalido():
    with pytest.raises(TypeError, match="O que está sendo solicitado está inválido."):
        Usuario(000, "neymar@gmail.com", "1234")

def test_usuario_email_vazio():
    with pytest.raises(ValueError, match="O que está sendo solicitado está inválido."):
        Usuario("Neymar", "", "1234")

def test_usuario_email_invalido():
    with pytest.raises(TypeError, match= "O que está sendo solicitado está inválido." ):
        Usuario("Neymar", 000, "1234")

def test_usuario_senha_vazio():
    with pytest.raises(ValueError, match="O que está sendo solicitado está inválido."):
        Usuario("Neymar", "neymar@gmail.com", "")

def test_usuario_senha_invalida():
    with pytest.raises(TypeError, match="O que está sendo solicitado está inválido."):
        Usuario("Neymar", "neymar@gmail.com", 000)
    