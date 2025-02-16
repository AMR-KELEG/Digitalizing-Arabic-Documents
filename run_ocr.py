import re
import os

import pytesseract
from PIL import Image

# The model for Arabic was downloaded from the tessdata repository
os.environ["TESSDATA_PREFIX"] = "tessdata/"

import pandas as pd
from tqdm import tqdm
from glob import glob

from argparse import ArgumentParser


def extract_text(png_directory, output_filename):
    """Extract the Arabic text from the pages in the png_directory and save it in a tsv file.

    Args:
        png_directory: A directory containing the png files of the pages.
        output_filename: The name of the output tsv file.
    """
    files = sorted(glob(f"{png_directory}/*"))

    ocred_text = []
    for file in tqdm(files):
        img = Image.open(file)
        # TODO: understand and optimize the following commands
        text = pytesseract.image_to_string(img, lang="ara", config="--oem 3 --psm 6")
        ocred_text.append(text)

    df = pd.DataFrame({"page_filename": files, "text": ocred_text})

    # The page number is extracted from the image's filename
    df["page_number"] = df["page_filename"].apply(
        lambda s: int(re.findall(r"\d+", s)[0])
    )
    df.sort_values(by="page_number", inplace=True)

    df.to_csv(f"{output_filename}.tsv", index=False, sep="\t")


def main():
    parser = ArgumentParser(
        "Extract the Arabic text from the pages in the png_directory and save it in a tsv file."
    )
    parser.add_argument(
        "--png_directory",
        help="A directory containing the png files of the pages.",
        required=True,
    )
    parser.add_argument(
        "--output_filename", help="The name of the output tsv file.", required=True
    )
    args = parser.parse_args()

    extract_text(args.png_directory, args.output_filename)


if __name__ == "__main__":
    main()
