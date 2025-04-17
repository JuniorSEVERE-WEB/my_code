def convert(s):
    return s.replace(":)", "🙂").replace(":(", "🙁")

def main():
    text = input("Tape yon bagay: ")
    print(convert(text))

if __name__ == "__main__":
    main()