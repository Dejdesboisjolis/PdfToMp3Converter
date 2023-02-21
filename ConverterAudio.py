from PyPDF4 import PdfFileReader
import pyttsx3
import argparse


class AudioConverter:
    args = list()
    print(args)

    def __init__(self):
        argParser = argparse.ArgumentParser(
            exit_on_error=True, description="Welcome to the ConverterAudio, let's choose an operation")

        argParser.add_argument(
            "-f", "--file",
            nargs='*',
            help="The fileName you want to select")
        AudioConverter.args = argParser.parse_args()
        print(AudioConverter.args.file)

    def convert_to_pdf(self):
        print(AudioConverter.args.file)
        speak = pyttsx3.init()
        for pdf in AudioConverter.args.file:
            try:
                with open(pdf, 'rb') as f:
                    pdf_read = PdfFileReader(f)
                    for x in range(pdf_read.getNumPages()):
                        page = pdf_read.getPage(x)
                        page_content = page.extractText()
                        # print(page_content)
                        speak.save_to_file(page_content, pdf+'.mp3')
                        print(
                            f" Le fichier contient {pdf_read.getNumPages()} pages")
                        speak.say(
                            f" Le fichier contient {pdf_read.getNumPages()} pages")
                        speak.runAndWait()
                        speak.stop()
            except IOError:
                print(f"Could not read file : {pdf}")


audioConv = AudioConverter()
audioConv.convert_to_pdf()
