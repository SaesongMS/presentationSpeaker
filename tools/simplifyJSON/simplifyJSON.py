# Usage: python simplifyJSON.py <json_path> <output_path>
# Example: python simplifyJSON.py "data.json" "output.json"

import sys
import json

def simplify_json(json_path, output_path):
    with open(json_path, 'r', encoding='UTF-8') as f:
        data = json.load(f)
    title = data["title"]
    chapters = data["contents"]
    simplified_data = {f"{title}":{}}
    for i, chapter in enumerate(chapters):
        chapter_title = chapter["title"]
        #the chapter always has a title
        #it can have text, caption, bullet_points, table
        #if it has text, it will be the value of the key "text"
        #if it has caption, it will be the value of the key "caption"
        #if it has bullet_points, it will be the value of the key "bullet_points" as a list
        #if it has table, it will be the value of the key "table" as a dictionary
        #the table will have headers and rows
        #the headers will be a list of strings
        #the rows will be a list of lists of strings
        #check for every type besides title
        #and save it as a string, adding to a value of the chapter title

        simplified_data[title][f"{chapter_title}"] = ""
        if "text" in chapter:
            simplified_data[title][f"{chapter_title}"] += chapter["text"]
            print(simplified_data[title][f"{chapter_title}"])
        if "caption" in chapter:
            simplified_data[title][f"{chapter_title}"] += chapter["caption"]
        if "bullet_points" in chapter:
            simplified_data[title][f"{chapter_title}"] += " ".join(chapter["bullet_points"])
        if "table" in chapter:
            simplified_data[title][f"{chapter_title}"] += " ".join(chapter["table"]["headers"])
            for row in chapter["table"]["rows"]:
                simplified_data[title][f"{chapter_title}"] += " ".join(row)

    with open(output_path, "w", encoding='UTF-8') as f:
        json.dump(simplified_data, f)

    #count words in the simplified json
    count = 0
    for key in simplified_data[title]:
        count += len(simplified_data[title][key].split())
    print(f"Total words in simplified json: {count}")

json_path = sys.argv[1]
output_path = sys.argv[2]

simplify_json(json_path, output_path)

