import sys
import sys

from generation import generate_chapter, check_output_path

# Usage: python generateChapter.py <Article Title> <Chapter Title> <Chapter number> <Chapter Text>
# Example: python generateChapter.py "The Art of War" "Chapter 1" "1" "Sun Tzu said: The art of war is of vital importance to the State."

if len(sys.argv) == 5:
    article_title = sys.argv[1]
    title = sys.argv[2]
    chapter_number = sys.argv[3]
    chapter_text = sys.argv[4]

    output_path = check_output_path(f"generations/{article_title}")

    title = ''.join(e for e in title if e.isalnum())
    generate_chapter(title, chapter_number, chapter_text, output_path)

    print(f"Chapter {title} generated and saved")
else:
    print("Usage: python generateChapter.py <Article Title> <Chapter Title> <Chapter number> <Chapter Text>")
    print("Example: python generateChapter.py \"The Art of War\" \"Chapter 1\" \"1\" \"Sun Tzu said: The art of war is of vital importance to the State.\"")




    

