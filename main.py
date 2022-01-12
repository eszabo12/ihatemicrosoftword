from docx2pdf import convert
import os

def crawl():
    for path, dirs, files in os.walk("~/Documents/"):
        convert(path)

def main():
    crawl()

main()