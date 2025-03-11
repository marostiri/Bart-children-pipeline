s = None
# File in folder 'Scraping'
PATH_LINKS_SCRAPED = ""
PATH_LINKS_SCRAPED_CLEAN = ""

with open(PATH_LINKS_SCRAPED, "r") as f:
    s = f.read()
    s = s.replace("https://", "\nhttps://")

list_link = s.split("\n")
print(len(list_link))
list_link_filterd = list(set(list_link))
print(len(list_link_filterd))

with open(PATH_LINKS_SCRAPED_CLEAN, "w") as f:
    for link in list_link_filterd:
        if "Vikidia:" not in link:
            link_substr = link[link.find("/wiki/"):]
            f.write(link_substr)
            f.write("\n")
