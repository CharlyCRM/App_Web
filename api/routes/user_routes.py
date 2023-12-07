from flask import Blueprint
from api.controllers.user_controller import getUsuario, postUsuario, putUsuario, deleteUsuario

'''Este fichero contiene las funciones vista relacionadas con User_controller'''

usuario_api = Blueprint('usuario_api', __name__) # ver comentario de más abajo

#######
# GET #
#######
@usuario_api.route('/usuario/<string:nombre_usuario>', methods=['GET'])
def vista_getUsuario(nombre_usuario):
    return getUsuario(nombre_usuario)
#------------------------------------------------------------------------------------------------------------------
########
# POST #
########
@usuario_api.route('/usuario', methods=['POST'])
def vista_postUsuario():
    return postUsuario()
#--------------------------------------------------------------------------------------------------------------------
#######
# PUT #
#######
@usuario_api.route('/usuario/<string:nombre_usuario>', methods=['PUT'])
def vista_putUsuario(nombre_usuario):
    return putUsuario(nombre_usuario)
#------------------------------------------------------------------------------------------------------------------
##########
# DELETE #
#########
@usuario_api.route('/usuario/<string:nombre_usuario>', methods=['DELETE'])
def vista_deleteUsuario(nombre_usuario):
    return deleteUsuario(nombre_usuario)






'''Un blueprint es un objeto que nos permite organizar las rutas y las funciones relacionadas en módulos separados. 
Proporciona una forma de definir rutas y funciones en un archivo separado y luego registrar ese blueprint en la aplicación principal.
Un blueprint puede contener rutas, funciones de vista y cualquier otra lógica relacionada con una parte específica de una aplicación. 
Al registrar un blueprint en la aplicación principal, las rutas y las funciones del blueprint se incorporan a la aplicación y se pueden acceder 
y utilizar como cualquier otra ruta o función de vista.
Al utilizar blueprints, podemos dividir nuestra aplicación en módulos más pequeños y manejar diferentes partes de la aplicación de manera modular. 
Esto facilita la organización del código, el mantenimiento y la escalabilidad de la aplicación a medida que crece.

1-. Crea una variable que contenga la función Blueprint.
2.- Añade el decorador @nombre_variable para enlazar la función de vista y así poder ser ejecutada desde el fichero principal del programa (main.py)
'''