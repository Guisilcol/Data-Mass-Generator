import sys
import json
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

    # params = load_json(sys.argv[1])
    params = load_json("../tests/paramtest.json")

    try:
        mc = MainControl()
        mc.init(params)
    except Exception as e:
        print(e)
        exit(1)


if __name__ == "__main__":
    main()
