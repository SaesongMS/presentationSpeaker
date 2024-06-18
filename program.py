import os

import time

import tkinter
import tkinter.messagebox
import customtkinter
from customtkinter import filedialog   
import json 
import subprocess
import sys


def run_generate_command(title, chapter_title, i, chapter_content,speaker):
    
    command = [
        f'{os.path.dirname(sys.executable)}/python.exe',
        "tools/tts/generateChapter.py",
        title,
        chapter_title,
        str(i),
        chapter_content,
        speaker
    ]
    
    print("Running command:", command)  # Debug print statement
    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        print("Command output:", result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        print("Command output:", e.output)



def run_generate_all_command(path,speaker):
    
    command = [
        f'{os.path.dirname(sys.executable)}/python.exe',
        "tools/tts/generateJSON.py",
        path,
        speaker
        
    ]
    
    print("Running command:", command)  # Debug print statement
    try:
        #result = subprocess.Popen(['tree'], shell=True)
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        print("Command output:", result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        print("Command output:", e.output)


def run_generate_jpg_command(data_pdf,output_folder):
    
    command = [
        f'{os.path.dirname(sys.executable)}/python.exe',
        "tools/pdf2jpg/generateImages.py",
        data_pdf,
        f'{output_folder}'
    ]
    
    print("Running command:", command)  # Debug print statement
    try:
        #result = subprocess.Popen(['tree'], shell=True)
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        print("Command output:", result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        print("Command output:", e.output)


def run_generate_video_command(output_folder):
    
    command = [
        f'{os.path.dirname(sys.executable)}/python.exe',
        "tools/slides2mp4/slides2mp4.py",
        f'{output_folder}',
    ]
    
    print("Running command:", command)  # Debug print statement
    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        print("Command output:", result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        print("Command output:", e.output)


def run_generate_script_command(title,output_folder,speaker):
    
    command = [
        f'{os.path.dirname(sys.executable)}/python.exe',
        "tools/tts/generateScript.py",
        title,
        "title",
        output_folder,
        speaker
    ]
    
    print("Running command:", command)  # Debug print statement
    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        print("Command output:", result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        print("Command output:", e.output)



def run_simplifyJSON_command(json_path,output_path):
    
    command = [
        f'{os.path.dirname(sys.executable)}/python.exe',
        "tools/simplifyJSON/simplifyJSON.py",
        json_path,
        output_path
    ]
    
    print("Running command:", command)  # Debug print statement
    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        print("Command output:", result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        print("Command output:", e.output)


customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    speaker = ""
    textbox = None
    data_json = ""
    data_json_path = ""
    data_pdf = ""
    output_folder_path="generations/"
    total_time = 0
    time_per_word= 0
    new_path = ""
    count = 0

    def run_generate_script_time_command(self,title,output_folder,speaker):
        start_time = time.time()
        run_generate_script_command(title,output_folder,speaker)
        end_time = time.time()
        self.total_time = end_time - start_time
        self.time_per_word = self.total_time/3
        print(f"Czas wykonania skryptu: {self.total_time:.2f} sekund")
        self.label_test = customtkinter.CTkLabel(self.generate_test, text=f"The time to produce the sound from the sentence 'Hi I'm Bark' was {self.total_time:.2f}s")
        self.label_test.grid(row=0, column=0, padx=10, pady=10, sticky="")
        self.label_test2 = customtkinter.CTkLabel(self.generate_test, text=f"Time per word {self.time_per_word:.2f}s")
        self.label_test2.grid(row=1, column=0, padx=10, pady=10, sticky="")
        if self.count !=0:
            self.label_test3 = customtkinter.CTkLabel(self.generate_test, text=f"Total aproximated time {self.time_per_word*self.count:.2f}s")
            self.label_test3.grid(row=2, column=0, padx=10, pady=10, sticky="")
        
       
    def select_file_json_ext(self):
        file_path = filedialog.askopenfilename(title="Select file", initialdir="/", filetypes=(("Pliki JSON", [".json"]),("Wszystkie pliki", "*.*")))
        if(file_path!=""):
            filename = os.path.basename(file_path)
            if not os.path.exists("generations"):
                os.mkdir("generations")
            run_simplifyJSON_command(file_path,f"generations/simplified_{filename}")
            self.new_path=f"generations/simplified_{filename}"
            self.select_file_json()


    def select_file_json(self):
        if self.new_path=="":
            file_path = filedialog.askopenfilename(title="Select file", initialdir="/", filetypes=(("Pliki JSON", [".json"]),("Wszystkie pliki", "*.*")))
        else:
            file_path = self.new_path
            
        self.data_json_path=file_path
        if file_path:
            try:
                with open(file_path) as f:
                    self.data_json = json.load(f)
                    self.textbox.configure(state='normal')
                    self.textbox.delete(1.0, "end")  # Access textbox using self
                    self.textbox.insert("1.0", self.data_json)
                    self.textbox.configure(state='disabled')
                    self.new_path=""
                    self.output_folder_path="generations/"
            except Exception as e:
                print(f"Error reading file: {e}")
        
        shortened_data = self.data_json
        title = list(shortened_data.keys())[0]

        #count words in the simplified json
        self.count=0
        for key in shortened_data[title]:
            self.count += len(shortened_data[title][key].split())
        print(f"Total words in simplified json: {self.count}")

        if self.time_per_word !=0:
            self.label_test3 = customtkinter.CTkLabel(self.generate_test, text=f"Total aproximated time {self.time_per_word*self.count:.2f}s")
            self.label_test3.grid(row=2, column=0, padx=10, pady=10, sticky="")

        self.output_folder_path=self.output_folder_path+title
        chapter_titles = self.data_json.get(title, {}).keys()
        self.scrollable_frame_buttons = []
        label = customtkinter.CTkLabel(master=self.scrollable_frame, text=f"{title}")
        label.grid(row=0, column=0, padx=10, pady=(0, 20), sticky="w")
        button = customtkinter.CTkButton(master=self.scrollable_frame, text="Generate", command = lambda: run_generate_script_command(title, self.output_folder_path,self.speaker))
        button.grid(row=0, column=1, padx=10, pady=(0, 20))
        self.scrollable_frame_buttons.append(button)
        for i, chapter_title in enumerate(chapter_titles):
            chapter_content = self.data_json[title][chapter_title]
            label = customtkinter.CTkLabel(master=self.scrollable_frame, text=f"{chapter_title}")
            label.grid(row=i+1, column=0, padx=10, pady=(0, 20), sticky="w")
            button = customtkinter.CTkButton(master=self.scrollable_frame, text="Generate", command = lambda: run_generate_command(title, chapter_title, i+1, chapter_content,self.speaker))
            button.grid(row=i+1, column=1, padx=10, pady=(0, 20))
            self.scrollable_frame_buttons.append(button)
        self.main_button_1.configure(state="normal")

    
    def select_file_pdf(self):
        file_path = filedialog.askopenfilename(title="Select file", initialdir="/", filetypes=(("Pliki PDF", [".pdf"]),("Wszystkie pliki", "*.*")))
        if file_path:
            try:
                self.data_pdf = file_path
                self.textbox2.configure(state='normal')
                self.textbox2.delete(1.0, "end")  # Access textbox using self
                self.textbox2.insert("1.0", file_path)
                self.textbox2.configure(state='disabled')
            except Exception as e:
                print(f"Error reading file: {e}")

        self.main_button_2.configure(state="normal")
        self.main_button_3.configure(state="normal")
    
    



    def __init__(self):
        super().__init__()

        # configure window
        self.title("TTS")
        self.geometry(f"{1300}x{780}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(2, weight=5)
        self.logo_label2 = customtkinter.CTkLabel(self.sidebar_frame, text="Select file .pdf\nwhich contains the presentation.", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label2.grid(row=0, column=0, padx=20, pady=(20, 10))
        # przycisk wyboru
        self.select_button2 = customtkinter.CTkButton(self.sidebar_frame, text="Select file", command=self.select_file_pdf)
        self.select_button2.grid(row=1, column=0, padx=20, pady=10)


         # create textbox
        self.textbox2 = customtkinter.CTkTextbox(self.sidebar_frame, width=230,height=20)  # Assign textbox to class variable
        self.textbox2.grid(row=2, column=0, padx=20, pady=10)

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Select file .json\nwhich contains the presentation.", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=3, column=0, padx=20, pady=(20, 10))

        # przycisk wyboru
        self.select_button = customtkinter.CTkButton(self.sidebar_frame, text="Select file (Simplify)", command=self.select_file_json)
        self.select_button.grid(row=4, column=0, padx=5, pady=5)
        self.select_button = customtkinter.CTkButton(self.sidebar_frame, text="Select file (Extension)", command=self.select_file_json_ext)
        self.select_button.grid(row=5, column=0, padx=5, pady=5)



         # create textbox
        self.textbox = customtkinter.CTkTextbox(self.sidebar_frame, width=230,height=150)  # Assign textbox to class variable
        self.textbox.grid(row=6, column=0, padx=20, pady=10)
    

        # create optionMennu for speaker
        self.option_frame = customtkinter.CTkFrame(self)
        self.option_frame.grid(row=0, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.label_radio_group = customtkinter.CTkLabel(master=self.option_frame, text="Choose a speaker:")
        self.label_radio_group.grid(row=0, column=0, columnspan=1, padx=10, pady=10, sticky="")
        self.optionmenu_1 = customtkinter.CTkOptionMenu(self.option_frame, dynamic_resizing=False,
                                                        values=["v2/pl_speaker_3", "v2/pl_speaker_0", "v2/en_speaker_6"],
                                                        command=self.update_speaker)
        self.optionmenu_1.grid(row=1, column=0, padx=10, pady=5)
        self.optionmenu_1.set("Default")



        # create label and button to generate each chapter
        # create optionMennu for speaker
        # create scrollable frame
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self, label_text="Chapter list")
        self.scrollable_frame.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)

        self.generate_all_frame = customtkinter.CTkFrame(self)
        self.generate_all_frame.grid(row=2, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.main_button_1 = customtkinter.CTkButton(self.generate_all_frame,text="Generate all chapters", border_width=2,command= lambda: run_generate_all_command(self.data_json_path,self.speaker))
        self.main_button_1.grid(row=3, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.main_button_1.configure(state="disabled")


        self.main_button_2 = customtkinter.CTkButton(self.generate_all_frame,text="Generate photos", border_width=2,command= lambda: run_generate_jpg_command(self.data_pdf,self.output_folder_path))
        self.main_button_2.grid(row=3, column=2, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.main_button_2.configure(state="disabled")

        self.main_button_3 = customtkinter.CTkButton(self.generate_all_frame,text="Generate video", border_width=2,command= lambda: run_generate_video_command(self.output_folder_path))
        self.main_button_3.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.main_button_3.configure(state="disabled")

        self.main_button_4 = customtkinter.CTkButton(self.generate_all_frame,text="Test generate audio", border_width=2,command= lambda: self.run_generate_script_time_command("Hi I'm Bark", "generations/test",self.speaker))
        self.main_button_4.grid(row=3, column=4, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.main_button_4.configure(state="normal")

       
        self.generate_test = customtkinter.CTkFrame(self)
        self.generate_test.grid(row=5, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.label_test = customtkinter.CTkLabel(self.generate_test, text=f"")
        self.label_test.grid(row=0, column=1, padx=10, pady=10, sticky="")
        

        

        # configure
        self.textbox.configure(state='disabled')
        self.textbox2.configure(state='disabled')

    def update_speaker(self, choice):
        self.speaker = choice
        print(f"Selected speaker: {self.speaker}")



if __name__ == "__main__":
    app = App()
    app.mainloop()