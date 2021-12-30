import requests
from bs4 import BeautifulSoups

import argparse
import connect
import sqlite3

url="https://www.oyorooms.com/hotel-in-bangalore/"
parser=argparse.ArgumentParser()

parser.add_argument("__dbname",help="enter the name of the data base ",type=int)



re=requests.get(url)
content=re.content
soups=BeautifulSoups(content,'html.parser')
scraped_list=[]
all_hotel=soups.find_all("div",{"class":"hotelcardlisting"})# it return a list

connect.connect(args.dbname)

for hotel in all_hotel:
    hotel_dict={}
    hotel_dict["name"]= hotel.find("h3",{"class":"listinghoteldescription__hotelname"}).text#inside the hotel we find the name of the hotel
    hotel_dict["address"]= hotel.find("span",{"itemprop":"streetaddress"}).text
    hotel_dict["price"]= hotel.find("span",{"class":"listingPrice__finalPrice"}).text
    try :
        hotel_dict["rating"]=hotel.find("span",{"class":"hotelRating__ratingSummary"}).text
    except AttributeError :
        hotel_dict["rating"] =None
    amenity_list=[]    
    parent_hotel_amenties=hotel.find("div",{"class":"amenityWrapper"})
    for amenity in parent_hotel_amenties.find_all("div",{"class":"amenityWrapper__amenity"}):
        hotel_dict["amenity"]= amenity_list.append(amenity.find("span",{"class":"d-body-smd-textEllipsis"}).text.strip())

    hotel_dict["amenity"]=','.join(amenity_list[:-1])
    scraped_list.append(hotel_dict)
    print(hotel_name,hotel_address,hotel_price,hotel_rating,amenity_list)
    connect.insert(args.dbname, tuple(hotel_dict.values()))



    connect.get_info(args.dbname)
    
