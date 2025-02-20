from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Gerenciador de usuários
class UsuarioManager(BaseUserManager):
    def create_user(self, email, senha=None, **extra_fields):
        if not email:
            raise ValueError('O campo email é obrigatório')
        email = self.normalize_email(email)
        usuario = self.model(email=email, **extra_fields)
        usuario.set_password(senha)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, email, senha=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, senha, **extra_fields)

# Modelo base para usuários
class Usuario(AbstractBaseUser):
    email = models.EmailField(unique=True)
    nome = models.CharField(max_length=255)
    senha = models.CharField(max_length=128)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']

    def __str__(self):
        return self.nome

# Modelo Locador
class Locador(Usuario):
    cnpj = models.CharField(max_length=18, unique=True)

    def gerenciar_imoveis(self):
        pass  # Lógica para gerenciar imóveis

    def gerenciar_reservas(self):
        pass  # Lógica para gerenciar reservas

# Modelo Cliente
class Cliente(Usuario):
    cpf = models.CharField(max_length=14, unique=True)

    def pesquisar_imoveis(self, filtros):
        pass  # Lógica para pesquisa de imóveis

    def reservar_imovel(self, id_imovel, datas):
        pass  # Lógica para reserva de imóvel