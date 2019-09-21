import sys
import json
from pydoc import locate


def call_controller(namespace: str, row_count: int, args: list):
    # controller_folder.type_folder.file.generate()
    instance = locate(f"controller.{namespace}.generate")
    if instance is None:
        print(f"Error: namespace {namespace} not found")
        exit(1)
    # TODO: do something...
    try:
        print(instance(row_count, args))
    except Exception as e:
        print(e)
        exit(1)


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

    # from argparse import ArgumentParser
    # sys.argv = params['name'].strip().split(' ')
    # sys.argv.insert(0, ".") # since the 1st arg is the filename argparse ignores it

    # TODO: pass args too
    local_param = params['name'].strip().split(' ')
    call_controller(local_param[0], 237, local_param[1:])


if __name__ == "__main__":
    main()
