# 09. Cómo subir este repositorio a GitHub paso a paso

Este documento está escrito para subir el proyecto sin asumir experiencia previa con GitHub.

## Opción A: subir desde la página de GitHub

1. Entra a GitHub e inicia sesión.
2. Presiona el botón **New repository**.
3. Escribe un nombre, por ejemplo:

```text
sonorizacion-nudos
```

4. Agrega una descripción:

```text
Proyecto de sonorización y visualización de nudos matemáticos mediante Python y Sonic Pi.
```

5. Elige si será público o privado.
6. No marques todavía la opción de crear README, porque este repositorio ya tiene uno.
7. Crea el repositorio.
8. En la página del repositorio vacío, usa la opción para subir archivos.
9. Arrastra todos los archivos y carpetas de este proyecto.
10. Escribe un mensaje de commit, por ejemplo:

```text
Primer montaje del repositorio de sonorización de nudos
```

11. Presiona **Commit changes**.

## Opción B: subir desde terminal

Desde la carpeta del proyecto:

```bash
git init
git add .
git commit -m "Primer montaje del repositorio de sonorización de nudos"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/sonorizacion-nudos.git
git push -u origin main
```

Cambia `TU_USUARIO` por tu usuario real de GitHub.

## Cómo actualizar el repositorio después

Cada vez que modifiques archivos:

```bash
git status
git add .
git commit -m "Describe brevemente el cambio"
git push
```

## Recomendación de organización

No subir archivos pesados innecesarios. Para audio final se puede subir una selección breve al repositorio y colocar piezas más pesadas en YouTube, SoundCloud o una carpeta externa enlazada desde el README.

