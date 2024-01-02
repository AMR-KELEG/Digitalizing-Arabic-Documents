# Arabic OCR using Tesseract
This repository serves as a guide for digitalizing Arabic documents using [Tesseract](https://github.com/tesseract-ocr/tesseract).

### Steps

- Convert the **pdf** file into multiple **pngs**
`mkdir -p pngs && convert -density 150 -trim PDF_FILE.pdf pngs/page%d.png`
- Download the Arabic model to the `tessdata/` directory from the tessdata repository: https://github.com/tesseract-ocr/tessdata/blob/main/ara.traineddata
- Run the OCR generation script: `python run_ocr.py`

### Archive of Datasets Generated Using the Pipeline

- Parallel Tunisian Constitution Corpus (PTCC): [![PTCC](https://img.shields.io/badge/🤗-PTCC%20-yellow.svg)](https://huggingface.co/datasets/AMR-KELEG/PTCC)
