from bs4 import BeautifulSoup
import requests

class WebScraping:
    def __init__(self, url):
        self.url = url
        self.soup = self.__get_html()

    def __get_html(self):
        req = requests.get(self.url)
        soup = BeautifulSoup(req.content, "html.parser")
        return soup

    def __get_rooms(self):
        return self.soup.find_all("div", class_ = "_1e9w8hic")

    def __get_title(self, room):
        return room.find("span", class_ = "ts5gl90 tl3qa0j t1nzedvd dir dir-ltr").text

    def __get_subtitle(self, room):
        return room.find("div", class_ = "mj1p6c8 dir dir-ltr").text

    def __get_atributes(self, room):
        atributes_room = {}
        details = room.find("div", class_ = "i1wgresd dir dir-ltr")
        atributes = details.find_all("span", class_ = "mp2hv9t dir dir-ltr")
        for atribute in atributes:
            atribute_info = atribute.text.split()
            atributes_room[f"{atribute_info[1][:3]}"] = atribute_info[0] 
        return atributes_room


    def __get_price(self, room_html):
        return room_html.find("div", class_ = "p1qe1cgb dir dir-ltr").find("span", class_ = "_tyxjp1").text[2:]
        
    def pick_all_rooms(self):
            list_of_rooms = []
            for room in self.__get_rooms():
                room_info = {}
                room_info["Title"] = self.__get_title(room)
                room_info["Subtitle"] = self.__get_subtitle(room)
                room_info["Price for 1 night (R$)"] = self.__get_price(room)
                atributes = self.__get_atributes(room)
                room_info["Guests"] = atributes.get("hós", None)
                room_info["Bedrooms"] = atributes.get("qua", None)
                room_info["Beds"] = atributes.get("cam", None)
                room_info["Bathrooms"] = atributes.get("ban", None)

                list_of_rooms.append(room_info)

            return list_of_rooms
