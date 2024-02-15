def read_and_print_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        if len(lines) >= 4:
            print("Trešā rinda:", lines[2].strip())
            print("Ceturtā rinda:", lines[3].strip())
        else:
            print("Failā nav pietiekami daudz rindu.")