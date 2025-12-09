import pycountry

def letter_count():
    return [chr(x)for x in range(65, 91)]

country_list = {}
country_name = []

for letter in letter_count():
    for country in pycountry.countries:
        if country.name.startswith(letter):
            country_name.append(country.name)
    country_list.update({letter: country_name.copy()})
    country_name.clear()

for key, value in country_list.items():
    print(f"{key} : {" , ".join(value)} - \nTotal Country Starts with {key} : {len(value)}")