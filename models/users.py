from sqlalchemy import Column, Integer, String
from db import Base
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, Length
from wtforms import StringField, IntegerField, PasswordField

class Usuario(Base):
    '''Clase Usuario -> Contiene los atributos de los productos de la tienda
        Args:
            ref_usuario: Número de identificación del usuario
            Nombre: El nombre del usuario.
            Apellidos: Apellidos del usuario.
            Nombre_usuario: Alias del usuario.
            Email: Correo electrónico.
            Dirección: Dirección de residencia principal.
            Comunidad_autonoma: Comunidad Autonoma en España.
            Provincia: Provincia de residencia en España
            Código_postal: Código postal de residencia en España'''
    
    __tablename__ = "usuario"
    __table_args__ = {'sqlite_autoincrement': True} # Automaticamente la PK se convierte en autoincremental
    ref_usuario = Column(Integer, primary_key = True)
    nombre = Column(String(30), nullable = True)
    apellidos = Column(String(30), nullable= True)
    nombre_usuario = Column(String(10))
    email = Column(String(30), nullable = True)
    direccion = Column(String(100),nullable = True)
    comunidad_autonoma = Column(String(20), nullable= True)
    provincia = Column(String(20), nullable= True)
    codigo_postal = Column(Integer, nullable = True)
    password = Column(String(10))


    '''al utilizar el ORM de SQLAlchemy, no es necesario definir explícitamente los métodos getter y setter 
    para los atributos. SQLAlchemy los generará automáticamente. '''
    def __init__(self, nombre, apellidos, nombre_usuario, email, direccion, comunidad_autonoma, provincia, codigo_postal, password): 
        self.nombre = nombre
        self.apellidos = apellidos
        self.nombre_usuario = nombre_usuario
        self.email = email
        self.direccion = direccion
        self.comunidad_autonoma = comunidad_autonoma
        self.provincia = provincia
        self.codigo_postal = codigo_postal
        self.password = password


    def __str__(self):
        return f"""
        Ref_usuario: {self.ref_usuario}
        Nombre: {self.nombre}
        Apellidos: {self.apellidos}
        Nombre Usuario: {self.nombre_usuario}
        Email: {self.email}
        Contraseña: {self.password}"""
    


class UsuarioForm(FlaskForm):
    '''Esta clase usa la libreria Flask_wtf para comprobar los datos introducidos por el usuario en el formulario definido en
    carrito.html'''
    nombre = StringField('Nombre', validators=[Length(max=30)])
    apellidos = StringField('Apellidos', validators=[Length(max=30)])
    nombre_usuario = StringField('Nombre de Usuario', validators=[DataRequired(), Length(max=10)])
    email = StringField('Email', validators=[Email(), Length(max=50)])
    direccion = StringField('Dirección', validators=[Length(max=100)])
    comunidad_autonoma = StringField('Comunidad Autónoma', validators=[Length(max=20)])
    provincia = StringField('Provincia', validators=[Length(max=20)])
    codigo_postal = IntegerField('Código Postal')
    password = PasswordField('Password', validators=[DataRequired(), Length(max=10)])

# DataRequired = Verifica que el campo se ha cumplimentado