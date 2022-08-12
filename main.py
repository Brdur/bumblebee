import os
import telebot


def main():
    my_input = os.environ.get("INPUT_MYINPUT")
    my_input = os.environ.get("INPUT_ASS")
    my_output = f"Hello {my_input2}"

    print(f"::set-output name=myOutput::{my_output}")


if __name__ == "__main__":
    main()
