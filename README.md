# PresentationSpeaker

## Project description
The project "PresentationSpeaker" was aimed at creating a "text-to-speech" (TTS) system to convert text into a speaker's voice. It will use text-to-speech processing to generate recordings in both Polish and English from JSON and PDF files.

## 1. Installation
### [Venv](https://code.visualstudio.com/docs/python/python-tutorial)
A Python environment that is separate and completely independent from the main Python installation. Using it is optional but it is strongly recommended.

### [Cuda](https://developer.nvidia.com/cuda-downloads)
CUDA is NVIDIA's computing platform that enables accelerated computing using a GPU. Installing CUDA is optional but nevertheless recommended as it improves the performance of model processing operations.

### PyTorch
PyTorch is a flexible and powerful library used to build and train machine learning models. It is used to implement and run `text-to-speech` models. 

To install, download the chosen version from the Pytorch website.
```
https://pytorch.org/get-started/locally/
```
### [Bark](https://github.com/suno-ai/bark)
Bark is a library that supports natural language processing (NLP) and voice generation. It is used for converting text into speech. It provides tools for the efficient extraction and conversion of text into sound sequences which is crucial in text-to-speech processing. 

Installation:
```
pip install git+https://github.com/suno-ai/bark.git
```

### FFmpeg
FFmpeg is essential for processing media files. In our project, it is used to combine images with video files. Its installation is required and you should make sure that it is available in the `PATH`.

Installation (choco required):
```
choco install ffmpeg
```

### [pdf2jpg](https://github.com/Belval/pdf2image)
pdf2jpg is a tool for extracting each page of a PDF as an image. 

To install it use:
```
pip install pdf2jpg
```
With this library we can easily convert any PDF page into an image. 

### [Poppler](https://github.com/oschwartz10612/poppler-windows/releases/)
Library used to render PDF files. A download of it is required. Use the `\tools\poppler\Library\bin` path in the code leading to `pdfimages.exe`. Optionally, it is possible to add the `bin/` folder to the `PATH`.

### CustomTkinter
CustomTkinter is an extension to the Tkinter library for creating modern user interfaces. It was used by us to create a graphical application interface for ease of use.

Installation:
```
pip install customtkinter
```

### Numpy
Library providing, among other things, multidimensional arrays and a set of functions to operate on them.

Installation:
```
pip install numpy
```

### NLTK
A set of libraries and programs for symbolic and statistical natural language processing. 

Installation:
```
pip install nltk
```

In addition, we use built-in libraries and Python language modules such as: `os`, `sys`, `JSON` or `subprocess`.

## 2. Operation
### Frontend / Self-executing scripts
The system provides two different modes of operation

#### 1. Using the graphical user interface (GUI)
With CustomTkinter, it is possible to launch a graphical application interface in which we can easily perform the following operations:
* Selecting the PDF file containing the presentation,
* Selecting the JSON file containing the presentation (there are two types to choose from - extended or simplified),
* Selecting the speaker (there are 3 types - two in Polish, one in English),
* Generate the sound of each chapter - choose one from the list,
* Generate audio for all chapters,
* Generating images based on a PDF file (JSON is required to have the article title, as the images are saved in a folder with the name of the title of this article),
* Generating a video file based on the images and sounds,
* Carrying out a test of the length of the generation of the sample audio (if JSON is loaded a prediction of the generation time of the entire audio is made).

When generating the audio, a new folder is created and the photos and video are created with the latest one.
Launching the GUI is possible with the command:
```
python program.py
```

#### 2. Self-executing scripts
You can call the scripts yourself in the console to get the output in the console and for easier debugging. The scripts can be found in the tools folder.
### Simplified JSON file example
```
{"Exploring Api Behaviours Through Generated Examples": 
    {
        "1 **Introduction**": "Understanding and verifying the behaviour of an API can be a difficult task. One way of alleviating some of this burden is through access to examples of the API's behaviour (McLellan et al., 1998; Novick & Ward, 2006; Nykaza et al., 2002; Robillard, 2009; Robillard & DeLine, 2011; Shull et al., 2000).",
        "2 Problem": "However, generating examples of an API's behaviour can be a difficult task. This is because the behaviour of an API is often complex and can be difficult to understand. Furthermore, generating examples of an API's behaviour can be time-consuming and error-prone."
    }
}
```
### Extended JSON file example
```
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
      "title": "Zastosowania IoT",
      "text": "Office 365 jest najlepszym przykładem, który oferuje zarówno funkcje tekstowe, jak i dyktowanie, co jest doskonałym przykładem zastosowania NLP. IoT przyniosło nowoczesne trendy w komunikacji i tłumaczeniu kontekstu językowego. Ułatwia to komunikację dla uczących się języków, badaczy i turystów. Wprowadzono na rynek kilka urządzeń IoT do komunikacji i tłumaczenia, takich jak inteligentne tłumacze językowe, C-Pen, TT-easy."
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
```
### Example of generated audio in Polish
https://github.com/SaesongMS/tts-laby/assets/76967271/91e3c169-3c67-4570-8bb9-7937e5e6f5b8

### Example of generated audio in English
https://github.com/SaesongMS/tts-laby/assets/76967271/6a95e815-38ca-4317-9203-398dd6aa12d2
