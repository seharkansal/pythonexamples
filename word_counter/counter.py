import os.path
def fetch_input():
    while True:
        file_name = input("enter file name:")
        if os.path.isfile(file_name):
            break
        else:
            print ("File does not exist... Try again.")
    with open(file_name, 'r') as file:
        data = file.read()
    string = input("enter the string you want to find in the text: ")
    return data, string


def calculate(data, string):
    word_count = data.count(string)
    return word_count


def main():
    print("Welcome to the word counter....")
    while True:
        text_sample, test_str = fetch_input()
        word_count = calculate(text_sample, test_str)
        print("'", test_str, "' appears '", word_count, "' times.. ")


def test_function():
    result=calculate("alice in wonderland alice in wonderland alice in wonderland alice in wonderland alice in wonderland alice in wonderland","in")
    assert result==6

    result=calculate("alice in wonderland alice in wonderland alice in wonderland alice in wonderland alice in wonderland alice in wonderland","hello")
    assert result==0

    result=calculate("short stories,scary stories,comedy stories","stories")
    assert result==3

    print("passed")    


if __name__ == "__main__":
    #main()
    test_function()        
