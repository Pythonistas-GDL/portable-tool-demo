# portable-tool-demo
Demo sobre cómo crear un ejecutable con pyinstaller

### Creación del ejecutable

Para crear un folder con el ejecutable y sus dependencias:
```console
pyinstaller src/portable_tool/main.py
```

Para crear el ejecutable con sus dependencias en un solo archivo:
```console
pyinstaller --onefile src/portable_tool/main.py
```
### Agregar archivos adicionales

Si el ejecutable requiere de archivos adicionales, como por ejemplo un archivo
de configuración, se pueden agregar al ejecutable con la opción `--add-data`:

```console
pyinstaller --onefile src/portable_tool/main.py --add-data "src/portable_tool/developers.xml:."
```

### Contenido del ejecutable

Pyinstaller cuenta con una herramienta para revisar el contenido del
ejecutable.
```console
pyi-archive_viewer dist/main --brief
```

### Revisar dependencias

Este comando únicamente muestra las dependencias del ejecutable. No considera
las dependencias de las dependencias de empaquetadas.
```console
pyi-bindepend dist/main
```

Para más detalles revisar:
- https://pyinstaller.org/en/stable/index.html
- https://github.com/pyinstaller/pyinstaller
