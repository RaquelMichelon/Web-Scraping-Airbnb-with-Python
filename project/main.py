from webScraping import WebScraping

url = "https://www.airbnb.com.br/s/Florian%C3%B3polis-~-SC/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=june&flexible_trip_dates%5B%5D=may&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&query=Florian%C3%B3polis%20-%20SC&place_id=ChIJ1zLGsk45J5URRscEagtVvIE&checkin=2022-05-09&checkout=2022-05-15&source=structured_search_input_header&search_type=autocomplete_click"
web_scraping = WebScraping(url)
# print(web_scraping.get_rooms())
print(web_scraping.pick_all_rooms())
