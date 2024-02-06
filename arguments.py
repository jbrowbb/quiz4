import argparse

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(help='Enter a string', dest='string_path', type=str)
    parser.add_argument(help='Enter a number', dest='number', type=int)
    parser.add_argument(help='Enter a float', dest='float_num',type=float)

    args = parser.parse_args()

    str_word = args.string_path
    numbers = args.number
    floats = args.float_num

    print("The string word is: ", str_word)
    print("The number is: ", numbers)
    print("The float is: ", floats)


if __name__=='__main__':
    main()