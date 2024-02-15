def write_to_file(name):
    try:
        with open('lietotajs.txt', 'w') as f:
            f.write(name)
        print("Vaiksmīgi uzrakstīts fails!")
    except Exception as e:
        print("Atradas kļūda: ", str(e))

if __name__ == "__main__":
    while True:
        try:
            user_input = input("Ievadi savu vārdu: ")
            if user_input.strip() != "":
                write_to_file(user_input)
                break
            else:
                print("Error: Vārds nevar būt tukšs.")
        except KeyboardInterrupt:
            print("\nProgrammu pārtraucis lietotājs.")
            break
        except Exception as e:
            print("Atradās kļūda: ", str(e))