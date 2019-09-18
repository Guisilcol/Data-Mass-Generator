import sys
import json
from pydoc import locate


def call_controller(namespace: str):
    # controller_folder.type_folder.file.generate()
    instance = locate('controller.' + namespace + '.generate')
    if instance is None:
        print("Error: namespace {0} not found".format(namespace))
        exit(1)
    # TODO: do something...
    print(instance())


def load_json(file):
    try:
        with open(file) as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                print("Error: Bad formatted json")
                exit(1)
    except FileNotFoundError:
        print("Error: File not found")
        exit(1)


def main():
    if len(sys.argv) < 2:
        print("Error: No file specified")
        return
    # params = load_json(sys.argv[1])
    params = load_json("../tests/paramtest.json")
    # pegar args globais como dbname e rows
    # checar se namespace existe
    # mandar sub param ("name": "ns.c -args") para o controller do namespace
    #   junto com args globais

    # TODO: pass args too
    call_controller('integer.smallint')


if __name__ == "__main__":
    main()
