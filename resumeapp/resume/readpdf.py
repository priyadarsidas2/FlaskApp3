import PyPDF2
import docx2txt

def extractTextFromPDF(fileName):
    
    if ".pdf" in fileName:
        pdfFileObj = open(fileName, 'rb')
        # creating a pdf reader object
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        # printing number of pages in pdf file
        # print(pdfReader.numPages)

        extractedText = ''
        for i in range(pdfReader.numPages):
            # creating a page object
            pageObj = pdfReader.getPage(i)
            # extracting text from page
            localText = pageObj.extractText()
            extractedText += localText
    
    if ".docx" in fileName:
        extractedText = docx2txt.process(fileName)
    
    return extractedText