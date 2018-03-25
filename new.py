import requests as requests



main_page = requests.get("https://114.by")
contact_page = requests.get("https://114.by/item/kontakty")
feedback_page = requests.get ("https://114.by/feedback")
statistika_page = requests.get("https://114.by/item/statistika-poiska")
error_page = requests.get("https://114.by/feedback/error/")


assert contact_page.status_code == 200
assert feedback_page.status_code == 200
assert statistika_page.status_code == 200
assert error_page.status_code == 200