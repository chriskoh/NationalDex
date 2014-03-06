#!/usr/bin/env python2

import requests
import os
from bs4 import BeautifulSoup

def pk_data_request():
   
    nat_dex_id = raw_input("Search by Pokemon ID number (001-549): ") # Set pokemon id number
    set_url = "http://www.serebii.net/pokedex-xy/"+str(nat_dex_id)+".shtml" # set web address
    pk_response = requests.get(set_url) # get webpage information
    pk_data = pk_response.text # Save web page information as text in "pk_data"
    return pk_data

def pk_data_parse(pk_data):
   
    soup = BeautifulSoup(pk_data) 
    print("\n"+soup.title.text+"\n") # print name / number of pokemon
    damage_modifier = soup.find_all(text=["*0", "*0.25", "*0.5", "*0.75", "*1", "*1.25", "*1.5", "*1.75", "*2"]) # Search for damage modifiers
    elemental_type = ['NRM', 'FIR', 'WTR', 'ELE', 'GRS', 'ICE', 'FGT', 'PSN', 'GND', 'FLY', 'PSY', 'BUG', 'RCK', 'GST', 'DRG', 'DRK', 'STL', 'FAR'] # Set variables for elements
    n = 0
    for every_damage_modifier in damage_modifier: # print "damage_modifier" with correct "elemental_type"
        print(elemental_type[n] + " " + every_damage_modifier)
        n = n + 1
    
def main():
   
    os.system("clear")
    pk_id = pk_data_request()
    pk_data_parse(pk_id)

if __name__ == "__main__":
    main()
