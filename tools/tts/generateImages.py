from pdf2image import convert_from_path
import sys

# Usage: python generateImages.py <pdf_file> <output_folder>
# Example: python generateImages.py "data/1.pdf" "generations/The Art of War"
# output_folder should be an generations/{Article Title}

if len(sys.argv) != 3:
    print("Usage: python generateImages.py <pdf_file> <output_folder>")
    exit()

pdf_file = sys.argv[1]
output_folder = sys.argv[2]

poppler_path = "tools/poppler/Library/bin"

images = convert_from_path(pdf_file, poppler_path=poppler_path)

# Create output folder
import os
if not os.path.exists(f"{output_folder}/imgs"):
    os.mkdir(f"{output_folder}/imgs")

for i, image in enumerate(images):
    image.save(f"{output_folder}/imgs/{i}.jpg", "JPEG")

print(f"Generated {len(images)} images in {output_folder}/imgs")