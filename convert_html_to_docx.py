import win32com.client
import os

word = win32com.client.Dispatch('Word.Application')
word.Visible = False

html_path = os.path.abspath('public/assets/monsmecta_wave1-1_dm_letter_a4.html')
docx_path_1 = os.path.abspath('public/assets/monsmecta_wave1-1_dm_letter_a4.docx')
docx_path_2 = os.path.abspath('public/assets/tournament_variant_16.docx')

doc = word.Documents.Open(html_path)

# Format 16 = wdFormatXMLDocument (.docx)
doc.SaveAs(docx_path_1, FileFormat=16)
doc.SaveAs(docx_path_2, FileFormat=16)

doc.Close()
word.Quit()

print("Word (.docx) files successfully created directly from HTML template!")
