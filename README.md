# svn-branch

### Herramienta para crear branches en repositorios SVN locales

Ejecutar el script con Python 3. El script pedirá la ruta local del repositorio y el nombre del nuevo branch a crear.
Una vez obtenidos estos datos, lo que hará será:

- Update en el trunk
- Copiar el contenido del trunk en el nuevo branch
- Añadir el contenido del nuevo branch
- Commitear el contenido del nuevo branch con un mensaje de commit por defecto (Contenido inicial de la rama xxx) 

Las librerías usadas en el script son:

- svn (pip install svn)
- os
- shutil
