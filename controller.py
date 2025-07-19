import pdfplumber
import re


Cr_total = 0.0
Dr_total = 0.0
cr_count = dr_count = 0
with pdfplumber.open("Kotak.pdf") as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        if text:
            lines = text.split('\n')
            for line in lines:
                if 'statement summary' in line.lower():
                    break
                match = re.search(r'([\d,]+\.\d+)\((Cr|Dr)\)', line)
                if match:
                    amount = float(match.group(1).replace(',', ''))
                    type_ = match.group(2)

                    if type_ == "Cr":
                        Cr_total += amount
                        cr_count+=1
                    else:
                        Dr_total -= amount
                        dr_count+=1
    
    print("Credit Amount:", Cr_total)
    print("Debit Amount:", Dr_total)
    print(cr_count, dr_count)