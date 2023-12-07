# App_Web
Este documento describe el trabajo realizado en el proyecto final del curso de **Programación Python Certificación PCAP**.
El proyecto consiste en el desarrollo de una tienda online para una empresa de venta al público de juguetes eróticos. El objetivo de dicha web es la venta de productos online en toda España, 
la gestión del inventario y seguimiento de ventas y stock.

## Contexto
Se ha seleccionado esta temática para la realización de este proyecto debido a varios factores, con el objetivo de otorgarle una mayor presencia y reivindicación.

En primer lugar, se buscaba una temática que fuera divertida, original y motivadora tanto para mí, en mi papel como desarrollador y máximo responsable del proyecto, como para las personas encargadas de evaluarlo. Era fundamental captar su interés y entusiasmo desde el principio.

En segundo lugar, tras realizar una exhaustiva investigación de varias temáticas que tenía en mente, y considerando mis limitadas habilidades en ilustración y creación de contenido gráfico, pude constatar que en internet hay una gran cantidad de material de calidad y gratuito relacionado con artículos eróticos.

Sin embargo, el punto más destacado y reivindicativo de este proyecto es el tercero. Con este proyecto, se busca dar visibilidad y romper con las antiguas estructuras mentales que catalogan este tipo de productos como tabú, oscuros o inapropiados para ser discutidos abiertamente. Por tanto, este aspecto será crucial en el diseño de la página web, que se esforzará por transmitir una imagen divertida, amigable, luminosa y accesible para todo tipo de clientes. Así, se pretende desafiar las concepciones preestablecidas y generar un entorno inclusivo y abierto al diálogo en torno a estos temas.

## Estructura del Proyecto
El diseño de este proyecto está determinado por dos factores clave. 

En primer lugar, se utiliza la librería FlasK, la cual impone una estructura organizativa que debe respetarse para garantizar el correcto funcionamiento del programa.

En segundo lugar, se ha implementado la arquitectura hexagonal, también conocida como arquitectura de puertos y adaptadores. 
Este enfoque de diseño se emplea para desarrollar aplicaciones web y sistemas de software, con el objetivo fundamental de mantener una alta modularidad y flexibilidad que facilite la evolución y el mantenimiento del código a lo largo del tiempo. 

La arquitectura hexagonal se basa en el principio de invertir las dependencias, lo que implica que las dependencias internas de una aplicación deben depender de abstracciones en lugar de implementaciones concretas.

En el contexto de este proyecto de aplicación web, se ha aplicado la arquitectura hexagonal para separar el frontend del backend mediante el uso de una API REST. Esto asegura una clara delimitación de responsabilidades y promueve la interoperabilidad, permitiendo que el frontend se comunique con el backend de manera eficiente y flexible.

Para puntualizar, Una API (Application Programming Interface) es un conjunto de reglas y protocolos que permiten a diferentes aplicaciones o sistemas comunicarse y compartir datos entre sí. Se puede pensar en una API como un intermediario que facilita la interacción entre diferentes componentes de software.

Las API son utilizadas para permitir la integración y la interoperabilidad entre diferentes sistemas, aplicaciones y servicios. Proporcionan una forma estandarizada de acceso a la funcionalidad y los datos de una aplicación o plataforma, permitiendo que otros programas utilicen dicha funcionalidad sin necesidad de conocer los detalles internos de cómo se implementa.

## Descripción de cada Directorio
**Models/** : Contiene el diseño de las tablas que componen la base de datos
**Templates/** : Contiene los ficheros HTML de la aplicación web.
**Static/** : Contiene los ficheros CSS y los directorios de las imágenes
**Carousel/** : Contiene las imágenes que se muestran en el componente carrusel de la pagina índex.html
**car_group/** : Contiene las imágenes de cada uno de los productos disponibles en la tienda
**Api/** : Contiene la estructura principal de la API REST
**Controllers/** : Controladores de Flask para manejar las solicitudes y respuestas HTTP, mediante las peticiones GET, POST, PUSH, DELETE.
**Routes/** : Contiene l

*ver fichero structure.txt para más detalle*

# Entorno Virtual
El proyecto cuenta con su propio entorno virtual creado directamente desde el shell utilizado para este proyecto zsh.

Evidentemente, este entorno no se encuentra dentro del fichero del programa, el cual es necesario crear mediante el uso del archivo **requierements.txt**.
