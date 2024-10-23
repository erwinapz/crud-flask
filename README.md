## Configuracion para levantar el proyecto.

* Clonar el repositorio.
   * ```git clone https://github.com/erwinapz/crud-flask.git```
 
* Entrar al directorio clonado.
  * ```cd crud-flask```

* Crear los directorios:
  * static: ```mkdir static```
  * templates: ```mkdir templates```
    
* El archivo styles.css mover al directorio static ```mv styles.css static```.
  
* Los siguientes archivos mover al directorio templates:
  * agregar_producto.html: ```mv agregar_producto.html templates```
  * base.html: ```mv base.html templates```
  * editar_producto.html: ```mv editar_producto.html templates```
  * index.html: ```mv index.html templates```

* Instalar Flask si no esta instalado.
  * ```pip install Flask```

* Ejecuta la aplicación desde la terminal.
  * ```python3 app.py```
 
* Entrar al navegador.
  * ```http://127.0.0.1:5000```
