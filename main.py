from fpdf import FPDF
import pandas as pd

# Create and format the PDF object
pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

# Create dataframe to read .csv file
df = pd.read_csv('topics.csv')

# Iterate over csv data to create/format the main topic page
for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family='Times', style='B', size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row['Topic'], align='L', ln=1)


    # Add lines to the page
    for y in range(21, 291, 10):
        pdf.line(10, y, 200, y)

#     Alternate 'Add Lines' method
#   ll = 21
#   while ll < 291:
#       pdf.line(10, ll, 200, ll)
#       ll = ll + 10

    # Set the footer
    pdf.ln(265)
    pdf.set_font(family='Times', style='I', size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row['Topic'], align='R')

    # Add and format "extra" pages
    for i in range(row['Pages'] - 1):
        pdf.add_page()

        # Add lines to the page
        for y in range(21, 291, 10):
            pdf.line(10, y, 200, y)

        # Set the footer
        pdf.ln(277)
        pdf.set_font(family='Times', style='I', size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row['Topic'], align='R')

pdf.output('output.pdf')

