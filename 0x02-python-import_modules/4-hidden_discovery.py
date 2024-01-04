#!/usr/bin/python3
import importlib


if __name__ == "__main__":
    module = importlib.import_module("__pycache__/calculator_1")
    names = dir(module).sort

    for name in names:
        if (name[0] == '_'):
            continue
        print(name)
