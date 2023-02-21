from PyPDF4 import PdfFileReader
import pyttsx3
import argparse


speak = pyttsx3.init()

argParser = argparse.ArgumentParser(
    exit_on_error=True, description="Welcome to the ConverterAudio, let's choose an operation")

argParser.add_argument(
    "-f", "--file",
    nargs='*',
    help="The fileName you want to select"
)
args = argParser.parse_args()

print(args.file)

def read_pdf(args : list):
    print(args)
    for pdf in args :
        try: 
            with open(pdf, 'rb') as f:
                pdf_read = PdfFileReader(f)
                for x in range (pdf_read.getNumPages()):
                    page = pdf_read.getPage(x)
                    page_content = page.extractText()
                    #print(page_content)
                    speak.save_to_file(page_content, pdf+'.mp3')
                    print(f" Le fichier contient {pdf_read.getNumPages()} pages")
                    speak.say(f" Le fichier contient {pdf_read.getNumPages()} pages")
                    speak.runAndWait()
                    speak.stop()
        except IOError:
            print (f"Could not read file : {pdf}")

read_pdf(args.file)