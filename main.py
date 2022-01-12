# from docx2pdf import convert
import os

def second():


def first():
    for root, dirs, files in os.walk("/Users/Elle/Documents/fall2021/201/"):
        for i in files:
            fullpath = os.path.join(root, i)
            # print(fullpath)
            try:
                convert(fullpath)
            except AssertionError:
                pass

def main():
    # first()
    second()

main()