import requests
from dotenv import load_dotenv
import os

from simulated_interface import user_input

load_dotenv()

host = os.getenv("HOST_SRV")
port = os.getenv("PORT_SRV")

#--- ENDPOINTS ---
# /api/room
# /api/temperature
# /api/average

#---Requests to API----------------------------
def post_api_room(response):
    url = f"http://{host}:{port}/api/room"
    requesting = requests.post(url=url, json={"name": response})   # PRECISO ESTUDAR PARA ENTENDER SE O JSON= CONVERTE O TIPO DICT PARA JSON JA NO CAMPO DE REQUISICAO
    return requesting

def post_api_temperature(id, temperature, date):
    request_dict = {"room": id, "temperature": temperature, "date": date}

    url = f"http://{host}:{port}/api/temperature"
    requesting = requests.post(url=url, json=request_dict)   
    return requesting
#----------------------------------------------
#---Client MENU--------------------------------
def show_menu():
    print()
    print("=" * 45)
    print("        MENU")
    print("=" * 45)
    print("  [1] Add Items into API")
    print("  [2] Show infos")
    print("  [3] Exit menu")
    print("=" * 45)


def add_items():
    menu_options_list = ["1","2"]

    print()
    print("-" * 45)
    print(" ADD ITEM ")
    print("-" * 45)

    print("=" * 45)
    print("        MENU")
    print("=" * 45)
    print("  [1] ADD a Room - /api/room")
    print("  [2] ADD a Temperature in a Existent Room - /api/temperature")
    print("=" * 45)

    menu_options = input("> ").strip()
    
    if menu_options not in menu_options_list:
        print("  [!] INVALID OPTION [!]")
        return
    else:
        match menu_options:
            case "1":
                request_to_api_room = user_input.getting_room_name()
                post_api_room(request_to_api_room)
            case "2":
                request_to_api_temperatures_ID = user_input.getting_room_ID()
                request_to_api_temperatures_temp = user_input.getting_room_temperature()
                request_to_api_temperatures_date = user_input.getting_date()

                post_api_temperature(id=request_to_api_temperatures_ID, temperature=request_to_api_temperatures_temp, date=request_to_api_temperatures_date)
    
    print(f"  [OK]!")


def show_info():
    print()
    print("-" * 45)
    print("  LOADING ")
    print("-" * 45)
    print()
    print("-" * 45)

def main():
    while True:
        show_menu()
        option = input("> ").strip()

        match option:
            case "1":
                add_items()
            case "2":
                show_info()
            case "3":
                print()
                print("=" * 45)
                print("  Exiting menu... BYE! 👋")
                print("=" * 45)
                break
                               
            case _:
                print()
                print("  [!] Invalid Option. Try Again.")
#----------------------------------------------

# Ponto de entrada
if __name__ == "__main__":
    main()
