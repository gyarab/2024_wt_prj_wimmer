import httpx
from pprint import pprint

print("Online prevodnik men dle cnb.cz")

url = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt?date=13.02.2025"

r = httpx.get(url)
# print(r.text)

in_array = r.text.split("\n")

# print(in_array)

radek_eur = ""

for line in in_array:
    if "|EUR|" in line:
        radek_eur = line

radek_array = radek_eur.split("|")
pprint(radek_array)

kurz_str = radek_array[-1]

kurz_str = kurz_str.replace(",", ".")

kurz = float(kurz_str)

rezim = input("0 = CZK -> EUR ; 1 = EUR -> CZK")

if (rezim == "0"):
    castka = input("Zadej castku v CZK: ")
    result = int(castka) / kurz
    print(f"To je v EUR: {result}")

elif (rezim == "1"):
    castka = input("Zadej castku v EUR: ")
    result = int(castka) * kurz
    print(f"To je v CZK: {result}")