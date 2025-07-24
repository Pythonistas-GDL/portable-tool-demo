#!/usr/bin/env python3
import argparse
import getpass
import os
import sys
import xml.etree.ElementTree as ET


def parse_arg(args: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Portable tool generada con Pyinstaller"
    )
    parser.add_argument('-n', '--name', help="Nombre del usuario", default=getpass.getuser())
    parser.add_argument('-s', '--show-details', action='store_true', help="Muestra detalles del ambiente de ejecución")
    parser.add_argument('-d', '--developers', action='store_true', help="Muestra lista de desarrolladores")
    return parser.parse_args(args)

def print_developers():
    # read developers from ./developers.xml
    developers_file = os.path.join(os.path.dirname(__file__), 'developers.xml')
    tree = ET.parse(developers_file)
    root = tree.getroot()
    print('-----------------------------------------------------')
    print('Lista de desarrolladores:')
    for developer in root.findall('developer'):
        name = developer.find('name')
        if name is not None:
            print(f"  {name.text}")
    print('-----------------------------------------------------')


def main():
    parsed_args = parse_arg(sys.argv[1:])
    print(f"Hola, {parsed_args.name}!")
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        print('Corriendo como un executable de PyInstaller')
        if parsed_args.show_details:
            print('-----------------------------------------------------')
            print(f'Path temporal creado por el bootloader: {sys._MEIPASS}')
            print('Archivos en el directorio temporal:')
            for root, dirs, files in os.walk(sys._MEIPASS):
                for file in files:
                    print(f"  {os.path.join(root, file)}")
            print('-----------------------------------------------------')
    else:
        print('Corriendo como un proceso de Python')

    if parsed_args.developers:
        print_developers()

if __name__ == '__main__':
    main()
