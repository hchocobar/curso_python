# Paquetes

<!-- TOC -->
* [Paquetes](#paquetes)
  * [Definición](#definición)
  * [¿Cómo crear un paquete?](#cómo-crear-un-paquete)
<!-- TOC -->

## Definición

Un paquete es un contenedor de módulos.

## ¿Cómo crear un paquete?

1. Creamos un directorio,
2. Dentro del directorio creamos dos archivos
   - `main.py`
   - `module.py` (este nombre es genérico, reemplaza `module` por el nombre del módulo deseas crear)
3. Edita `main.py` e importa tu modulo:
   - `import module`
4. Ejecuta main.py y sucederá lo siguiente:
   - Se ejecutó main.py y no hizo nada (porque tu módulo aún está vacío)
   - Se creó un subdirectorio `__pycache__`
   - Dentro de `__pychache__` se creó un archivo.
   - El nombre del archivo será `module.cpython-xy.pyc`, donde:
     - `module` es el nombre de tu módulo.
     - `xy` hacen referencia a la version de Python que estás utilizando.
     - `pyc` determina que es un archivo python compilado.
