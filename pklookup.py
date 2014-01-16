#!/usr/bin/env python2

import requests
import time
import os
from bs4 import BeautifulSoup as bs

def main():

        os.system("clear")

        var = raw_input("Enter pokemon number (Three digit format): ")
        url = "http://www.serebii.net/pokedex-xy/"+str(var)+".shtml"

        r = requests.get(url)
        soup = bs(r.text)

        print("\n" + soup.title.text + "\n")

        mod = soup.find_all(text=["*0", "*0.25", "*0.5", "*0.75", "*1", "*1.25", "*1.5", "*1.75", "*2"])
        element_type = ['NRM', 'FIR', 'WTR', 'ELE', 'GRS', 'ICE', 'FGT', 'PSN', 'GND', 'FLY', 'PSY', 'BUG', 'RCK', 'GST', 'DRG', 'DRK', 'STL', 'FAR']

        n = 0
        for eachmod in mod:
            print(element_type[n] + " " + eachmod)
            n=n+1

if __name__ == "__main__":
    main()
