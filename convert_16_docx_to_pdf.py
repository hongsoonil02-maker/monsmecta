import win32com.client
import os

word = win32com.client.Dispatch('Word.Application')
word.Visible = False

for i in range(1, 17):
    docx_path = os.path.abspath(f'public/assets/tournament_variant_{i}.docx')
    pdf_path = os.path.abspath(f'public/assets/tournament_variant_{i}.pdf')
    doc = word.Documents.Open(docx_path)
    doc.SaveAs(pdf_path, FileFormat=17)
    doc.Close()
    print(f"Converted variant {i} to PDF")

word.Quit()
print("All 16 PDFs converted successfully!")
