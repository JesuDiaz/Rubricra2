**Documentación para el proyecto de aplicación web Flask**

**Descripción**

Este proyecto es una aplicación web Flask simple que se conecta a una base de datos Access y permite a los usuarios agregar, editar y eliminar tareas.

**Archivos**

* **config.py:** Contiene la configuración de la conexión a la base de datos Access.
* **init.py:** Inicializa la aplicación Flask y crea una instancia de la aplicación.
* **routes.py:** Define las rutas de la aplicación web.

**Instalación**

Para instalar el proyecto, descarga el código y guárdalo en una carpeta. Luego, abre un terminal en la carpeta y ejecuta el siguiente comando:

```
pip install -r requirements.txt
```

**Ejecución**

Para ejecutar la aplicación web, ejecuta el siguiente comando en la terminal:

```
python init.py
```

Esto iniciará la aplicación web en el puerto 5000. Puedes visitar la aplicación web en tu navegador en la siguiente dirección:

```
http://localhost:5000
```

**Requisitos**

Para ejecutar el proyecto, se necesita lo siguiente:

* Python 3.8 o superior
* Pip
* Base de datos Access

**Uso**

La aplicación web tiene las siguientes rutas:

* `/`: Muestra todas las tareas en la base de datos.
* `/add`: Permite a los usuarios agregar una nueva tarea a la base de datos.
* `/toggle/<int:task_id>`: Permite a los usuarios marcar una tarea como hecha o no hecha.
* `/delete/<int:task_id>`: Permite a los usuarios eliminar una tarea de la base de datos.

**Explicación**

El archivo `config.py` contiene la configuración de la conexión a la base de datos Access. El archivo `init.py` inicializa la aplicación Flask y crea una instancia de la aplicación. El archivo `routes.py` define las rutas de la aplicación web.

La ruta `/` utiliza la biblioteca `pyodbc` para conectarse a la base de datos Access y recuperar todas las tareas. La ruta `/add` utiliza la biblioteca `pyodbc` para agregar una nueva tarea a la base de datos. La ruta `/toggle/<int:task_id>` utiliza la biblioteca `pyodbc` para marcar una tarea como hecha o no hecha. La ruta `/delete/<int:task_id>` utiliza la biblioteca `pyodbc` para eliminar una tarea de la base de datos.
