"""
{
  "title": "Rozdział - 1",
  "bibliography": [],
  "authors": [],
  "universities": [],
  "contents": [
    {
      "title": "Przetwarzanie Języka Naturalnego: Zastosowania, Techniki i Wyzwania",
      "text": "Abstrakt\nPrzetwarzanie języka naturalnego (ang. NLP) jest gałęzią sztucznej inteligencji, która zajmuje się przetwarzaniem i interpretacją języka naturalnego przez komputery. Wyzwania w dziedzinie sztucznej inteligencji koncentrują się na interpretacji języka i jego złożonościach. Praktyczne zastosowania obejmują wyszukiwanie informacji, ekstrakcję informacji, tłumaczenie maszynowe, uproszczenie tekstu, analizę sentymentu i podsumowywanie tekstu. NLP jest obecnie głównym obszarem badań. Oprogramowanie tekstowe, takie jak MS Word, jest ważnym przykładem NLP do automatycznej poprawy gramatyki i pisowni."
    },
    {
      "title": "",
      "image": "photo1.jpeg",
      "caption": "Rysunek 1: Przykład Office 365"
    },
    {
      "title": "Zastosowania IoT",
      "text": "Office 365 jest najlepszym przykładem, który oferuje zarówno funkcje tekstowe, jak i dyktowanie, co jest doskonałym przykładem zastosowania NLP. IoT przyniosło nowoczesne trendy w komunikacji i tłumaczeniu kontekstu językowego. Ułatwia to komunikację dla uczących się języków, badaczy i turystów. Wprowadzono na rynek kilka urządzeń IoT do komunikacji i tłumaczenia, takich jak inteligentne tłumacze językowe, C-Pen, TT-easy."
    },
    {
      "title": "",
      "image": "photo2.jpg",
      "caption": "Rysunek 2: Urządzenia IoT"
    },
    {
      "title": "Słowa kluczowe",
      "bullet_points": ["przetwarzanie języka naturalnego (NLP)", "wyszukiwanie informacji", "ekstrakcja informacji", "tłumaczenie maszynowe", "uproszczenie tekstu"]
    },
    {
      "title": "Wprowadzenie",
      "text": "Język naturalny lub język zwyczajny to każdy język, który naturalnie wyewoluował wśród ludzi. Język człowieka pojawił się przez użycie i powtarzanie bez formalnego i celowego planowania. Naturalny język można uznać za różne formy, takie jak mowa, śpiew, mimika, znaki i gesty ciała. Naturalnie rozwinięty język jest wynikiem ludzkich nawyków opartych na różnych słowach, znakach, gestach i innych czynnościach. W ostatnich latach sztuczna inteligencja ma duże znaczenie w aplikacjach w życiu człowieka."
    },
    {
      "title": "",
      "image": "graphic1.png",
      "caption": "Rysunek 3: Przykład analizy składni"
    },
    {
      "title": "Porównanie technik NLP",
      "table": {
        "headers": ["Technika", "Opis", "Przykładowe Zastosowania"],
        "rows": [
          ["Tokenizacja", "Dzielenie tekstu na pojedyncze słowa lub zdania", "Przetwarzanie tekstu, analiza sentymentu"],
          ["Lematyzacja", "Sprowadzanie słów do ich podstawowej lub źródłowej formy", "Wyszukiwanie informacji, normalizacja tekstu"],
          ["Stemming", "Usuwanie przyrostków, aby sprowadzić słowa do ich podstawowej formy", "Wyszukiwarki, indeksowanie"],
          ["Tagowanie części mowy", "Identyfikacja części mowy (rzeczowniki, czasowniki, przymiotniki, itp.) w zdaniu", "Analiza składni, ekstrakcja informacji"],
          ["Rozpoznawanie nazwanych jednostek (NER)", "Wykrywanie i klasyfikacja nazwanych jednostek w tekście (np. ludzi, organizacji, lokalizacji)", "Kategoryzacja treści, grafy wiedzy"],
          ["Analiza zależności", "Analiza struktury gramatycznej zdania i ustalanie relacji między słowami", "Zrozumienie zdania, tłumaczenie maszynowe"],
          ["Analiza sentymentu", "Określanie sentymentu lub emocji wyrażonych w tekście", "Analiza opinii klientów, monitorowanie mediów społecznościowych"],
          ["Tłumaczenie maszynowe", "Tłumaczenie tekstu z jednego języka na inny", "Komunikacja wielojęzyczna, lokalizacja"]
        ]
      }
    }
  ]
}
"""

#changing above json to below json
"""
{"Exploring Api Behaviours Through Generated Examples": 
{
    "1 **Introduction**": "Understanding and verifying the behaviour of an API can be a difficult task. One way of alleviating some of this burden is through access to examples of the API's behaviour (McLellan et al., 1998; Novick & Ward, 2006; Nykaza et al., 2002; Robillard, 2009; Robillard & DeLine, 2011; Shull et al., 2000).",
    "2 Problem": "However, generating examples of an API's behaviour can be a difficult task. This is because the behaviour of an API is often complex and can be difficult to understand. Furthermore, generating examples of an API's behaviour can be time-consuming and error-prone."
}
}
"""

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

json_path = sys.argv[1]
output_path = sys.argv[2]

simplify_json(json_path, output_path)

