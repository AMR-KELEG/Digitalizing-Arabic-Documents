# Arabic OCR using Tesseract
This repository serves as a guide for digitalizing Arabic documents using [Tesseract](https://github.com/tesseract-ocr/tesseract).

### Steps

- Install the python packages using pip
`pip install -r requirements.txt`

- Convert the **pdf** file into multiple **pngs**
`mkdir -p pngs && convert -density 150 -trim PDF_FILE.pdf pngs/page%d.png`.
  - Note: Replace **PDF_FILE.pdf** with your file's name.
- Download the Arabic model to the `tessdata/` directory from the tessdata repository: https://github.com/tesseract-ocr/tessdata/blob/main/ara.traineddata
- Run the OCR generation script: `python run_ocr.py`.
- Inspect the output tsv file and the input pdf file for ad-hoc text preprocessing operations to clean the text.

### Archive of Datasets Generated Using the Pipeline

- Parallel Tunisian Constitution Corpus (PTCC): [![PTCC](https://img.shields.io/badge/🤗-PTCC%20-yellow.svg)](https://huggingface.co/datasets/AMR-KELEG/PTCC)
