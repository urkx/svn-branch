# Librerías usadas:
#   - svn (pip intall svn)
#   - os
#   - shutil

import svn.local
import svn
import os
import shutil

def trunkEnBranch(origen, destino):
    try:
        shutil.copytree(origen, destino)
    except shutil.Error as e:
        print('Error al copiar el contenido del trunk al branch. Error: %s\n' %e)
    except OSError as e:
        print('Error al copiar el contenido del trunk al branch. Error: %s\n' %e)

if __name__ == '__main__':
    print('Ruta del repositorio local: ')
    path = input()
    r = svn.local.LocalClient(path)

    print('Nombre del nuevo branch: ')
    b = input()

    print('Copiando contenido del trunk en el nuevo branch...\n')
    svn.local.LocalClient(path+'\\trunk').update()
    trunkEnBranch(path+'\\trunk', path + '\\branches\\' + b)

    print('Añadiendo branch al repositorio...\n')
    r.add(path + '/branches/' + b)

    print('Commiteando branch al repositorio...\n')
    r.commit('Contenido inicial de la rama ' + b)

    print('Branch creado! :-)')

