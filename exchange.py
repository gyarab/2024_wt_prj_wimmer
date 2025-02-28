import httpx # type: ignore
from os import system


def prepare() -> float:

    site = httpx.get("https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt")

    in_array: list = site.text.split("\n")
    row_eur: str = ""

    for line in in_array:
        if "|EUR|" in line:
            row_eur = line

    return float(row_eur.split("|")[-1].replace(",", "."))


def is_only_number(text: str) -> bool:

    for c in range(len(text)):
        if (text[c] != '0' and text[c] != '1' and text[c] != '2' and text[c] != '3' and text[c] != '4' and text[c] != '5' and text[c] != '6' and text[c] != '7' and text[c] != '8' and text[c] != '9'):
            return False
        
    return True


def collect_input(text: str) -> str:

    print(text)

    return input("\n>>>")


def reset_and_print_header() -> None:

    system("cls")
    print("Online prevodnik men dle cnb.cz\n")

    return


def calculate_exchange(regime: str, exchange_rate: float) -> bool:

    if (regime != "0" and regime != "1"):
        return False
        
    money_amount: str = ""

    while (True):
        reset_and_print_header()

        if (regime == "0"):
            money_amount = input("Zadej castku v CZK: ")

        else:
            money_amount = input("Zadej castku v EUR: ")

        if (not is_only_number(money_amount)):
            continue

        if (regime == "0"):
            print(f"To je v EUR: {int(money_amount) / exchange_rate}")

        else:
            print(f"To je v CZK: {int(money_amount) * exchange_rate}")

        return True
    
    return False


def main() -> None:

    exchange_rate: float = prepare()
    regime: str = ""

    while (True):
        reset_and_print_header()
        regime = collect_input("0 = CZK -> EUR\n1 = EUR -> CZK")
        
        if (not calculate_exchange(regime, exchange_rate)):
            continue

        regime = collect_input("\n0 = konec programu\ncokoliv = nový převod")

        if (regime == "0"):
            system("cls")
            
            break

    return


if (__name__ == "__main__"): 
    main()