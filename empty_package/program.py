import sys
import empty_package


def main():
    print(f"Hello from empty package ({empty_package.__version__})!")
    print()
    print(f"Python version: {__import__('sys').version}")
    print()
    print(f"Executable: {sys.executable}")


if __name__ == "__main__":
    main()
