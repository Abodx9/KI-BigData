import pdfplumber


# This line ask the user to drag and drop the file to the terminal (its path)
#pdf_in = input("Paste your PDF file path here: ")


# I have tried to extract the text according to the font name and size , It somehow works but need more work
pdf_in = "D:\\Projects\\UNI\\KI und Big Data\\KI-BigData\\DIE_LINKE.pdf"
with pdfplumber.open(pdf_in) as pdf:
    for page in pdf.pages:
        # Extract the strings with specific font
        words = [word['text'] for word in page.extract_words(extra_attrs=["fontname", "size"]) 
                 if word['fontname'] == 'HANCAD+CorporateS-ExtraBold' and word['size'] == 10.5]
        
        # Extract the strings with all other fonts
        words2 = [word['text'] for word in page.extract_words(extra_attrs=["fontname", "size"])
                 if not word['fontname'] == 'HANCAD+CorporateS-ExtraBold' and word['size'] == 10.5 or word['fontname'] == 'HANCAD+CorporateS-Bold' and word['size'] == 10.5]
        print(' '.join(words))
        print(",")
        print(' '.join(words2))