import argparse
from typing import Any


def process_data(args: Any) -> None:
    try:
        with open(args.input, "r") as file:
            data = file.read()
            
        result = data.upper()

        if args.multiply:
            result *= 2
        if args.divide:
            result = result[:len(result)//2]

        with open(args.output, "w") as file:
            file.write(result)

        if args.verbose:
            print(f"Data from {args.input} was processed and written to {args.output}")

    except FileNotFoundError as e:
        print(f"File {args.input} not found", f"Error: {e}", sep="\n")


def additional_function() -> None :
    print("This is an additional function")



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process data form an input file to an output file")
    parser.add_argument("--input", required=True, help="Path to input file")
    parser.add_argument("--output", required=True, help="Path to output file")
    parser.add_argument("--verbose", action="store_true", help="Prints processing details")
    parser.add_argument("--multiply", action="store_true", help="Multiply the data by 2")
    parser.add_argument("--divide", action="store_true", help="Divide the data by 2")

    args = parser.parse_args()
    process_data(args)
    additional_function()