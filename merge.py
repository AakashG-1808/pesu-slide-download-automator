import os
import argparse
from PyPDF2 import PdfMerger


def get_unique_output_path(folder, base_name):
    name, ext = os.path.splitext(base_name)
    ext = ext or ".pdf"

    candidate = f"{name}{ext}"
    counter = 1
    while os.path.exists(os.path.join(folder, candidate)):
        candidate = f"{name}[{counter}]{ext}"
        counter += 1

    return os.path.join(folder, candidate)


def merge(folder, output_name=None):
    if not os.path.exists(folder) or not os.path.isdir(folder):
        print(f"Folder doesn't exist: {folder}")
        return

    pdfs = [f for f in os.listdir(folder) if f.lower().endswith(".pdf")]
    if len(pdfs) < 2:
        print("Nothing to merge.")
        return

    pdfs = sorted(
        pdfs,
        key=lambda x: int(os.path.splitext(x)[0]) if x.split(".")[0].isdigit() else float("inf")
    )

    if not output_name:
        output_name = "merged.pdf"
    if not output_name.lower().endswith(".pdf"):
        output_name += ".pdf"

    output_path = get_unique_output_path(folder, output_name)

    merger = PdfMerger()
    for pdf in pdfs:
        merger.append(os.path.join(folder, pdf))

    merger.write(output_path)
    merger.close()

    print(f"Merged PDF created → {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge PDFs in a folder")
    parser.add_argument("--folder", required=True, help="Folder containing PDF files")
    parser.add_argument("--output", help="Output PDF name (optional)")
    args = parser.parse_args()

    merge(args.folder, args.output)
