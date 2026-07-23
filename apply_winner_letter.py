import win32com.client
import os

word = win32com.client.Dispatch('Word.Application')
word.Visible = False

best_id = 16  # Variant 16: Orca Emerald Supreme
docx_best = os.path.abspath(f'public/assets/tournament_variant_{best_id}.docx')
pdf_best = os.path.abspath(f'public/assets/tournament_variant_{best_id}.pdf')

doc = word.Documents.Open(docx_best)
doc.SaveAs(os.path.abspath('public/assets/monsmecta_wave1-1_dm_letter_a4.docx'))
doc.SaveAs(os.path.abspath('public/assets/monsmecta_wave1-1_dm_letter_a4.pdf'), FileFormat=17)
doc.Close()
word.Quit()

print("Winner Orca Variant 16 successfully updated to monsmecta_wave1-1_dm_letter_a4.docx & .pdf!")
