import os

def read_and_print_file_content(file_name, file_format):
    try:
        file_path = os.path.join(file_name, file_format)
        with open(file_path, 'r') as file:
            content = file.read()
            print("Ievadītā faila saturs:")
            print(content)
    except FileNotFoundError:
        print("Kļūda: Nekorekts faila nosaukums vai paplašinājums.")
    except PermissionError:
        print("Kļūda: Nesaknes vairs failu skatīt.")
    except Exception as e:
        print("Nepareizā kļūda:", str(e))

file_name = input("Ievadiet faila nosaukumu: ")
file_format = input("Ievadiet faila paplašinājumu (pvz: .txt): ")

read_and_print_file_content(file_name, file_format)