# Écrivez votre code ici !
from bs4 import BeautifulSoup


# extraction des informations avec beautifulsoup
with open("index.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# extraction du titre
title = soup.title.string if soup.title and soup.title.string else ""
print("titre de la page", title)
# extraction du text de la base h1
h1_tag = soup.find("h1")
h1_text = h1_tag.string if h1_tag and h1_tag.string else ""
print("contenu de h1:", h1_text)

# dictionnaire pour stocker tous les produits
all_products = dict()

# extraction des informations des produits dans la liste
products = soup.find_all("li")
for product in products:
    # récupère le nom
    h2_tag = product.find("h2")
    name = h2_tag.string.strip() if h2_tag and h2_tag.string else ""

    # récupère le prix (sécurisé)
    price_tag = product.find("p", class_="price")
    price_str = price_tag.string if price_tag and price_tag.string else ""
    price_list = price_str.split(" ") if price_str else []
    prix_val = ""
    if len(price_list) > 1:
        prix_val = price_list[1]
    elif len(price_list) == 1:
        prix_val = price_list[0]

    all_products[name] = {"prix": prix_val}

    # description (dernier <p>)
    p_tags = product.find_all("p")
    description = p_tags[-1].string if p_tags and p_tags[-1].string else ""
    all_products[name]["description"] = description
    print("produits :", all_products)


# conversion du prix€ en prix$
for name in all_products.keys():
    price_str = all_products[name].get("prix", "")
    # nettoyage du symbole euro et formatage
    cleaned = price_str.replace("€", "").replace(",", ".").strip()
    try:
        price = float(cleaned) if cleaned else 0.0
    except ValueError:
        price = 0.0

    dollar_price = price * 1.2
    all_products[name]["prix_dollar"] = f"{dollar_price}$"
    print("tous les produits :", all_products)
