from flask import jsonify, request, redirect, url_for
from models.users import Usuario
from db import session

'''Este fichero contiene las funciones API REST. Conectan con la base de datos y devuelven un JSON'''

#######
# GET #
#######
def getUsuario(nombre_usuario):
    '''Realiza una consulta a la base de datos utilizando SQLAlchemy para obtener el usuario correspondiente
    a la referencia proporcionada (ref_usuario). Si se encuentra un usuario con esa referencia, se devuelve un objeto JSON que contiene los detalles 
    del usuario: con la referencia, nombre, apellidos, nombre_usuario, etc.
    Si no se encuentra ningún usuario con la referencia proporcionada, se devuelve un objeto JSON con un mensaje indicando que el usuario 
    no se encontró.'''
    usuario_query = session.query(Usuario).filter_by(nombre_usuario=nombre_usuario).first()
    if usuario_query:
        return jsonify({
            'ref_usuario': usuario_query.ref_usuario,
            'nombre': usuario_query.nombre,
            'apellidos': usuario_query.apellidos,
            'nombre_usuario': usuario_query.nombre_usuario,
            'email': usuario_query.email,
            'direccion': usuario_query.direccion,
            'comunidad_autonoma': usuario_query.comunidad_autonoma,
            'provincia': usuario_query.provincia,
            'codigo_postal': usuario_query.codigo_postal,
            'password': usuario_query.password
            })
    return jsonify({
        'Mensaje': 'Usuario no Encontrado'
    })
#------------------------------------------------------------------------------------------------------------------------------
########
# POST #
########
def postUsuario():
    '''Recibe los datos del nuevo usuario en formato JSON desde la solicitud HTTP. Se utilizan las claves del diccionario JSON para obtener 
    los valores correspondientes.
    A continuación, se crea una instancia de la clase Usuario (objeto) con los datos recibidos y se verifica si la referencia del usuario ya existe 
    en la base de datos. Si la referencia ya existe, se genera una excepción y se captura para devolver un mensaje de error indicando 
    que la referencia existe.'''
    try:
        # Obtengo los datos del nuevo usuario del cuerpo de la solicitud JSON
        data = request.form # indico que los datos recibidos desde el servidor vendrán de un formulario
        
        nombre = data['nombre']
        apellidos = data['apellidos']
        nombre_usuario = data['nombre_usuario']
        email = data['email']
        direccion = data['direccion']
        comunidad_autonoma = data['comunidad_autonoma']
        provincia = data['provincia']
        codigo_postal = data['codigo_postal']
        password = data['password']

        # Creo una instancia (objeto) de Usuario con los datos recibidos
        nuevo_usuario = Usuario(
            nombre = nombre,
            apellidos = apellidos,
            nombre_usuario = nombre_usuario,
            email = email,
            direccion = direccion,
            comunidad_autonoma = comunidad_autonoma,
            provincia = provincia,
            codigo_postal = codigo_postal,
            password = password
        )
        
        # Verifico si el nombre_usuario ya existe en la base de datos. Si ya existe capturo la execpcion con raise y la envio a Exception
        usuario_existe = session.query(Usuario).filter_by(nombre_usuario=nombre_usuario).first()
        if usuario_existe:
            mensaje = 'El usuario ya existe'
            return redirect(url_for('registro', mensaje=mensaje))

        
        # Agregar el nuevo objeto a la base de datos, tabla usuario
        session.add(nuevo_usuario)
        session.commit()
        mensaje = 'Usuario creado correctamente'
        
        return redirect(url_for('registro', mensaje=mensaje))
    except KeyError:
        return jsonify({'mensaje': 'Error en los datos introducidos'})
    except Exception as e:
        return jsonify({'mensaje': f'Error en el servidor: {str(e)}'})
#----------------------------------------------------------------------------------------------------------------------
########
# PUT #
########
def putUsuario(nombre_usuario):
    '''Recibe los datos actualizados del usuario en formato JSON desde el cuerpo de la solicitud HTTP. Se utilizan las claves del diccionario JSON 
    para obtener los valores correspondientes.A continuación, se verifica si el usuario con la referencia proporcionada existe en la tabla Usuario 
    de la base de datos. Si el usuario existe, se actualizan los datos del usuario existente con los valores recibidos en la solicitud JSON. 
    Esto se realiza asignando los valores correspondientes a los atributos del objeto usuario_existe.'''
    try:
        data = request.get_json()

        # Verifico si el usuario existe en la tabla Producto
        usuario_existe = session.query(Usuario).filter_by(nombre_usuario=nombre_usuario).first()
        if usuario_existe:
            # Actualizar los datos del usuario existente con los valores recibidos en la solicitud JSON
            usuario_existe.ref_producto = data['ref_usuario']
            usuario_existe.nombre = data['nombre']
            usuario_existe.apellidos = data['apellidos']
            usuario_existe.nombre_usuario = data['nombre_usuario']
            usuario_existe.email = data['email']
            usuario_existe.direccion = data['direccion']
            usuario_existe.comunidad_autonomna = data['comunidad_autonoma']
            usuario_existe.provincia = data['provincia']
            usuario_existe.codigo_postal = data['codigo_postal']
            usuario_existe.password = data['password']

            session.commit()
            return jsonify({'mensaje': 'Usuario actualizado correctamente'})
        
        else:
            return jsonify({'mensaje': 'La ref_usuario no existe'})
    
    except KeyError:
        return jsonify({'mensaje': 'Error en los datos introducidos'})
    except Exception as e:
        return jsonify({'mensaje': f'Error en el servidor: {str(e)}'})
#----------------------------------------------------------------------------------------------------------------------------------
##########
# DELETE #
#########
def deleteUsuario(nombre_usuario):
    '''Verifica si el usuario con la referencia proporcionada existe en la tabla Usuario de la base de datos. Si el producto existe, 
        se utiliza la función delete de la sesión SQLAlchemy para eliminarlo de la base de datos.'''
    try:
        # Verifico si el usuario existe en la tabla Producto
        usuario_existe = session.query(Usuario).filter_by(nombre_usuario=nombre_usuario).first()
        if usuario_existe:
            session.delete(usuario_existe)
            session.commit()
            
            return jsonify({'mensaje': 'Usuario eliminado correctamente'})

        else:
            return jsonify({'mensaje': 'La ref_usuario no existe'})
        
    except KeyError:
        return jsonify({'mensaje': 'Error en los datos introducidos'})
    except Exception as e:
        return jsonify({'mensaje': f'Error en el servidor: {str(e)}'})



# GET = Método por defeto
# POST = Se usa para guardar datos
# PUT = Se usa para actualizar datos
# DELETE = Se usa para eliminar datos