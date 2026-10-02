# Tienda web con Flask — proyecto de formación

Este fue mi proyecto final del curso de Programación Python orientado a la certificación PCAP. Elegí una tienda ficticia de productos eróticos para practicar una aplicación con catálogo, carrito, formularios y operaciones sobre una base de datos.

Lo conservo como trabajo académico de desarrollo web, no como una tienda operativa ni como una plataforma preparada para clientes reales.

## Qué permite revisar

El código conecta plantillas HTML con rutas de Flask, modelos SQLAlchemy y endpoints de productos y usuarios. Incluye navegación por categorías, consulta de productos, un carrito y vistas de administración.

La estructura separa `models/`, `api/routes/`, `api/controllers/`, `templates/` y `static/`. Esa organización me ayudó a distinguir responsabilidades; no la presento como una implementación completa de arquitectura hexagonal.

## Leer o ejecutar el proyecto

Empieza por `main.py` para seguir el recorrido entre páginas y por `api/` para revisar las operaciones de datos. `structure.txt` conserva el mapa de archivos del ejercicio.

Para una revisión local, usa una copia del repositorio y un entorno aislado:

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requierements.txt
python main.py
```

El nombre `requierements.txt` corresponde al archivo existente. La aplicación usa el puerto 5000 y hace peticiones a su propia API en `127.0.0.1:5000`; cambiar el puerto requiere revisar esas direcciones. Las dependencias y la base de datos pertenecen al entorno de formación y no se han modernizado en esta revisión.

## Límites del prototipo

El carrito se guarda en una lista global, no en una sesión independiente por cliente. El acceso administrativo utiliza credenciales de ejemplo y el servidor arranca en modo debug. No lo utilices con datos reales ni lo expongas a Internet sin revisar autenticación, sesiones, validación, protección de formularios y tratamiento de errores.

Los flujos de catálogo y administración no equivalen a una integración de pagos ni a un sistema completo de pedidos. Las imágenes y materiales del ejercicio tampoco deben asumirse libres de restricciones de reutilización.

## Qué aprendí

El proyecto me permitió conectar una interfaz con persistencia y entender mejor las peticiones entre componentes. Mis proyectos actuales se presentan por separado en [el portfolio](https://carlos-ramirez-martin.up.railway.app/es/).
