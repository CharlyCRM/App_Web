from flask import Flask, render_template, request, redirect, url_for
from api.routes.product_routes import producto_api
from api.routes.user_routes import usuario_api
from models.products import Producto
from models.users import Usuario
import requests
from db import session
import db


app = Flask(__name__)

# Importa el blueprint producto_api y usuario_api desde el directorio api/product_routes.py y api/user_routes.py
app.register_blueprint(producto_api) 
app.register_blueprint(usuario_api)

####################
# Pagina Principal #
####################

@app.route('/')
def index():
    '''Función que activa la página principal index.html
    Realiza a la URL indicada, una petición GET a la API con el objetivo de obtener los datos del producto interesado
    mediante su ref_producto.'''
    # Utilizo un lista con los ref_producto que quiero mostrar y realizo un bucle for para enviarselas a la API
    # Si quisiera mostrar otros producto, simplemente hay que modificar esta lista
    obj_list = [requests.get('http://127.0.0.1:5000/producto/' + str(ref)).json() for ref in [111, 112, 221, 222, 223, 224]]
    return render_template('index.html', data=obj_list)
#------------------------------------------------------------------------------------------------------------------------

###############
# Tienda.html #
###############

@app.route('/tienda')
def tienda():
    '''Función que activa la pagina de tienda.html
    Recoge la valirable len_lista que es creada en la función carro_compra para poder generar un contador en el boton carrito'''
    len_lista = request.args.get('len_lista', 0)
    obj_list = [requests.get('http://127.0.0.1:5000/producto/' + str(ref)).json() for ref in [111, 112, 221, 222, 223, 224, 999]]
    return render_template('tienda.html', data=obj_list, len_lista=len_lista)

lista = [] # Contiene los productos que se van a comprar

@app.route('/carro_compra')
def carro_compra():
    '''Función que recibe desde un formulario un producto que a sido añadido al carro de la compra.
    Recoge todos los productos que se añaden al carro de la compra, en una lista.'''
    data_product = request.args.get('ref_producto')
    response = requests.get('http://127.0.0.1:5000/producto/' + str (data_product))
    data = response.json()
    lista.append(data)
    len_lista = len(lista)
    
    print(lista)
    print("Productos en la lista ->>", len_lista)
    return redirect(url_for('tienda',len_lista=len_lista))
#------------------------------------------------------------------------------------------------------------------------

######################
# Tienda_Hombre.html #
######################

@app.route('/tienda_hombre')
def tienda_hombre():
    '''Función que activa la pagina de tienda_hombre.html
    Recoge la valirable len_lista que es creada en la función carro_compra para poder generar un contador en el boton carrito'''
    len_lista = request.args.get('len_lista', 0)
    obj_list = [requests.get('http://127.0.0.1:5000/producto/' + str(ref)).json() for ref in [111, 112, 113, 114, 115, 225, 999]]
    return render_template('tienda_hombre.html', data=obj_list, len_lista=len_lista)

######################
# Tienda_Mujer.html #
######################

@app.route('/tienda_mujer')
def tienda_mujer():
    '''Función que activa la pagina de tienda_mujer.html
    Recoge la valirable len_lista que es creada en la función carro_compra para poder generar un contador en el boton carrito'''
    len_lista = request.args.get('len_lista', 0)
    obj_list = [requests.get('http://127.0.0.1:5000/producto/' + str(ref)).json() for ref in [221, 222, 223, 224, 113, 225, 999]]
    return render_template('tienda_mujer.html', data=obj_list, len_lista=len_lista)
#------------------------------------------------------------------------------------------------------------------------

#################
# Producto.html #
#################

@app.route('/ver_producto')
def verproducto():
    '''Función que se activa cuando se hace click sobre la imagen de un producto en la tienda
    Muestra todos los datos del producto en la pagina producto.html'''
    len_lista = request.args.get('len_lista', 0)
    data_product = request.args.get('ref_producto')
    response = requests.get('http://127.0.0.1:5000/producto/' + str (data_product))
    data = response.json()
    return render_template('/producto.html', data=data, len_lista=len_lista)
#------------------------------------------------------------------------------------------------------------------------

################
# Carrito.html #
################

@app.route('/carrito')
def carrito():
    '''Función que activa la pagina carrito.html'''
    user = request.args.get('user') # Obtiene el valor user desde la URL enviada desde la funcion usuario

    data=lista # Lista que contiene los productos que se van a comprar
    return render_template('carrito.html',data=data, user=user)

@app.route('/eliminar_producto/<int:index>', methods=['POST'])
def eliminar_producto(index):
    '''Elimina un producto del carrito'''
    data=lista # Lista que contiene los productos que se van a comprar
    lista.pop(index) # Extraigo el producto de la lista de la compra en función de su posición en la lista
    return render_template('/carrito.html', data=data)

@app.route('/comprobar_usuario')
def usuario():
    '''Función que recibe desde un formulario un usuario que a sido añadido al carro de la compra.
    Recoge todos los productos que se añaden al carro de la compra, en una lista.'''
    data_usuario = request.args.get('nombre_usuario')
    response = requests.get('http://127.0.0.1:5000/usuario/' + str (data_usuario))
    user = response.json()
    print(type(user))
    return redirect(url_for('carrito', user=user))
#------------------------------------------------------------------------------------------------------------------------

#################
# registro.html #
#################

@app.route('/registro')
def registro():
    '''Función que renderiza la pagina de registro de nuevo usuario.
    La incorporación de sus datos a la base de datos se hace directamente desde el html llamando a la API'''
    mensaje = request.args.get('mensaje')
    return render_template('/registro.html', mensaje=mensaje)
#------------------------------------------------------------------------------------------------------------------------

###############
# login.html #
###############

@app.route('/login')
def login():
    '''Función que activa la pagina de login.html'''
    return render_template('/login.html')

@app.route('/validar_usuario', methods=['POST'])
def validar_usuario():
    '''Funcion que valida si el nombre de usuario y contraseña sean:
    admin - 1234'''
    # Recojo los valores nombre_usuario y password desde el formulario login.htmll
    nombre_usuario = request.form['nombre_usuario']
    password = request.form['password']

    # Validar las credenciales
    if nombre_usuario == 'admin' and password == '1234':
        # Si el uausuariourio es correcto, lanza la pagina admin.html y carga todos los productos de la tabla producto
        obj_list = session.query(Producto).all()
        return render_template('/admin.html', data=obj_list)  # Redirigir a la página admin.html si las credenciales son válidas
    else:
        return render_template('/login.html', error='Contraseña Inválida')
#------------------------------------------------------------------------------------------------------------------------

###############
# admin.html #
###############

@app.route('/admin')
def admin():
    '''Función que renderiza la página admin y realiza una consulta a la base de datos para obtener todos los productos'''
    obj_list = session.query(Producto).all()
    return render_template('admin.html', data=obj_list)
#------------------------------------------------------------------------------------------------------------------------

#######################
# admin_eliminar.html #
#######################

@app.route('/admin_eliminar')
def vista_eliminar():
    '''Funcion que renderiza la página admin_eliminar.html'''
    data = request.args.get('data')
    return render_template('admin_eliminar.html', data=data)

@app.route('/delete', methods=['POST'])
def delete():
    '''Funcion que recoge la ref_producto recibiva desde la pagina admin_eliminar.
    A continuacion se conecta a la API para eliminar el producto'''
    ref_producto = request.form['ref_producto']
    response = requests.delete('http://127.0.0.1:5000/producto/' + str(ref_producto))
    data = response.json()
    return redirect(url_for('vista_eliminar', data=data))
#------------------------------------------------------------------------------------------------------------------------

#####################
# admin_crear.html #
#####################

@app.route('/admin_crear')
def vista_crear():
    '''Funcion que renderiza la página admin_crear'''
    mensaje = request.args.get('mensaje')
    return render_template('admin_crear.html', data=mensaje)
#------------------------------------------------------------------------------------------------------------------------

########################
# admin_modificar.html #
########################

@app.route('/admin_modificar')
def vista_modificar():
    '''Funcion que renderiza la página admin_modificar'''
    data = request.args.get('data')
    return render_template('admin_modificar.html', data=data)



@app.route('/modificar', methods=['POST'])
def modificar():
    '''Funcion que recoge la ref_producto recivida desde la pagina admin_modificar y la pasa a la API para validar si
    el producto existe.
    A continuacion se conecta a la API para modificar el producto'''
    ref_producto = request.form['ref_producto']
    data = {
        'ref_producto': ref_producto,
        'nombre': request.form['nombre'],
        'descripcion': request.form['descripcion'],
        'precio': request.form['precio'],
        'cantidad': request.form['cantidad'],
        'categoria': request.form['categoria'],
        'fecha_fabricacion': request.form['fecha_fabricacion'],
        'imagen': request.form['imagen']
    }
    response = requests.put('http://127.0.0.1:5000/producto/' + str(ref_producto), data=data)
    data = response.json()
    return redirect(url_for('vista_modificar', data=data))
#------------------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    db.Base.metadata.create_all(db.engine) # Creamos el modelo de datos
    app.run(debug=True) # Ejecutamos el servidor
    
