import sys
import json
from os import unlink
from controller._maincontrol import MainControl


def load_json(file):
    try:
        with open(file) as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error: file not found")
        exit(1)
    except json.JSONDecodeError:
        print("Error: bad formatted json")
        exit(1)


def main():
    if len(sys.argv) < 2:
        print("Error: no file specified")
        return

    params = load_json(sys.argv[1])
    output_f = open(sys.argv[2], 'w+') if len(sys.argv) > 2 else sys.stdout

    try:
        mc = MainControl(output_f)
        mc.init(params)
        if output_f.name != sys.stdout.name:
            print(f"Data saved in {output_f.name}.")
    except Exception as e:
        print(e)
        try:
            if output_f.name != sys.stdout.name:
                unlink(output_f.name)
        except PermissionError:
            pass
        exit(1)
    finally:
        output_f.close()


if __name__ == "__main__":
    main()
