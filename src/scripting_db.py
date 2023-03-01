import argparse

def input_parse(): #args will be specified in teh cmd line
    # initialize the parser
    parser = argparse.ArgumentParser()
    # add argument
    parser.add_argument("--name", type=str, default="Kevin")
    parser.add_argument("--age", type=int, required=True)
    #parse the arguments from the command line
    args = parser.parse_args()

    return args

def hello(name, age):
    print("Hello my name is " + name + "!")
    print("I am " + str(age) + " years old.")

def main():
    # run input parse to get name
    args = input_parse()
    # pass name to hello()
    hello(args.name, args.age)

# if this script imported another script, X,
# that other script would also be read
# and any functions in X will have its output
# in the terminal. The code below prevents this. 
if __name__ == "__main__":
    main()