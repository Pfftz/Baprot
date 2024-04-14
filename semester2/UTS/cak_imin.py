from pyfiglet import Figlet


def ascii_art_generator(text):
    f = Figlet(font='slant')
    return f.renderText(text)


if __name__ == "__main__":
    text = input("Enter your text: ")
    print(ascii_art_generator(text))
