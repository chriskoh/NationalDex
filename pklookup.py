#!/usr/bin/env python2

import requests
import time
import os
from bs4 import BeautifulSoup

def pk_data_request():
    nat_dex_id = raw_input("Search by Pokemon ID number (001-549): ")
    set_url = "http://www.serebii.net/pokedex-xy/"+str(nat_dex_id)+".shtml"
    pk_response = requests.get(set_url)
    pk_data = pk_response.text
    return pk_data

def pk_data_parse(pk_data):
    soup = BeautifulSoup(pk_data)
    print("\n"+soup.title.text+"\n")
    damage_modifier = soup.find_all(text=["*0", "*0.25", "*0.5", "*0.75", "*1", "*1.25", "*1.5", "*1.75", "*2"])
    elemental_type = ['NRM', 'FIR', 'WTR', 'ELE', 'GRS', 'ICE', 'FGT', 'PSN', 'GND', 'FLY', 'PSY', 'BUG', 'RCK', 'GST', 'DRG', 'DRK', 'STL', 'FAR']
    n = 0
    for every_damage_modifier in damage_modifier:
        print(elemental_type[n] + " " + every_damage_modifier)
        n = n + 1
    
def main():
    os.system("clear")
    pk_id = pk_data_request()
    pk_data_parse(pk_id)


if __name__ == "__main__":
    main()
