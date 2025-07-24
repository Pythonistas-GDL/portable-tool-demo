import argparse
import getpass
import sys


def parse_arg(args: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Portable tool generada con Pyinstaller"
    )
    parser.add_argument('-n', '--name', help="Nombre del usuario", default=getpass.getuser())
    return parser.parse_args(args)


def main():
    parsed_args = parse_arg(sys.argv[1:])
    print(f"Hola, {parsed_args.name}!")


if __name__ == '__main__':
    main()
