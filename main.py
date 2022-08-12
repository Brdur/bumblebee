import os
import telebot


def main():
    my_input2 = os.environ.get("INPUT_FAF")
    my_output = f"DON'T WORRY, {my_input2}"

    print(f"::set-output name=myOutput::{my_output}")


if __name__ == "__main__":
    main()
