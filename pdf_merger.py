# merge PDFs by running script with list of PDFs as args

import PyPDF2
import sys

inputs = sys.argv[1:]

merger = PyPDF2.PdfFileMerger()

for pdf in inputs:
    merger.append(pdf)

merger.write("mergeddoc.pdf")
merger.close()
