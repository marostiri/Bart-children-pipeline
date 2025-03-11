import time
import re
from bs4 import BeautifulSoup


def access_retrieve_main_data(link, by, value, driver):
    driver.get(link)
    time.sleep(2)
    return driver.find_element(by=by, value=value)


def remove_table(html_string):
    pattern = re.compile(r'<table.*?>(.*?)</table>', re.DOTALL)
    return re.sub(pattern, '', html_string)


def remove_figure(html_string):
    pattern_figure = re.compile(r'<figure.*?>(.*?)</figure>', re.DOTALL)
    first_sub = re.sub(pattern_figure, '', html_string)
    return first_sub


def remove_infobox(page_bs):
    for tag in page_bs.find_all(class_='infobox'):
        tag.decompose()


def remove_thumbnails(page_bs):
    for tag in page_bs.find_all(class_='thumb'):
        tag.decompose()


def remove_note(page_bs):
    for tg in page_bs.find_all( attrs={"role": "note"}):
        tg.decompose()


def remove_sup(page_bs):
    for tg in page_bs.find_all('sup'):
        tg.decompose()


def remove_style(page_bs):
    for tg in page_bs.find_all('style'):
        tg.decompose()


def remove_figcap(page_bs):
    for tg in page_bs.find_all('figcaption'):
        tg.decompose()


def remove_editSection(page_bs):
    for tag in page_bs.find_all(class_='mw-editsection'):
        tag.decompose()


def remove_math(page_bs):
    for tag in page_bs.find_all('math'):
        tag.decompose()

def remove_img(page_bs):
    for tag in page_bs.find_all('img'):
        tag.decompose()

def remove_final_part(page_bs):
    start_text = "<h2>General</h2>"
    blocked_sources = ('Collegamenti_esterni',
                       "Galleria_d'immagini",
                       'Voci_correlate',
                       'Altri_progetti',
                       'Galleria',
                       'Note',
                       'Bibliografia')
    if page_bs.find(class_="avviso-disambigua"):
        return start_text + "ambiguo"

    if page_bs.find(class_="noarticletext"):
        return start_text + "inesistente"

    print( len(tuple((page_bs.find(class_="mw-content-ltr").children))))
    for tag in page_bs.find(class_="mw-content-ltr").children:
        #print("a0")
        #print(tag)
        if tag.name == 'div':
            #print(tag)
            print("in-div")
            try:
                if "mw-heading" in tag.get("class"):
                    id_h_span = tag.contents[0].get('id')
                    print("in-div-id")
                    name_first_child = tag.contents[0].name
                    print("in-div-name")
                    if id_h_span in blocked_sources:
                        print("STOP NOW")
                        break
                    else:
                        print("in-div-title-ok")
                        text_h = tag.contents[0].text
                        start_text = start_text + "<" + name_first_child + ">" + text_h + "</"+name_first_child+">"
            except Exception as inst:
                print("skip")
        elif tag.name == 'p':
            #print("--------------------p---------------")
            #print(tag.get_text())
            start_text = start_text + tag.get_text()
        elif tag.name in ("h1", "h2", "h3", "h4"):
            try:
                out = False
                for tagC in tag.children:
                    if tagC.name in blocked_sources:
                            print("STOP NOW")
                            out = True
                            break
                
                if out:
                    break
            except Exception as inst:
                print("skip")
            start_text = start_text +  "<" + tag.name + ">" + tag.get_text() +"</" + tag.name + ">"
        elif tag.name == 'ul' or tag.name == 'ol' or tag.name == 'dl':
            start_text = start_text + tag.get_text()+".\n"
    print("--------------------FINAL---------------")
    #print(start_text)
    print("--------------------END---------------")
    return start_text


def remove_final_part_viki(page_bs):
    start_text = "<h2>General</h2>"
    blocked_sources = ('Collegamenti_esterni',
                       "Galleria_d'immagini",
                       'Voci_correlate',
                       'Altri_progetti',
                       'Galleria',
                       'Note',
                       'Bibliografia')
    if page_bs.find(class_="avviso-disambigua"):
        return start_text + "ambiguo"

    if page_bs.find(class_="noarticletext"):
        return start_text + "inesistente"

    for tag in page_bs.find(class_="mw-parser-output").children:
        print(tag.name)
        if tag.name == 'div':
            print(tag)
            print("in-div")
            try:
                if "mw-headline" in tag.get("class"):
                    id_h_span = tag.contents[0].get('id')
                    print("in-div-id")
                    name_first_child = tag.contents[0].name
                    print("in-div-name")
                    if id_h_span in blocked_sources:
                        print("STOP NOW")
                        break
                    elif tag.get("class") not in ('floatnone', 'thumb'):
                        print("in-div-title-ok")
                        text_h = tag.contents[0].text
                        start_text = start_text + "<" + name_first_child + ">" + text_h + "</"+name_first_child+">"
            except Exception as inst:
                print("skip")
        elif tag.name == 'p' or tag.name == 'blockquote':
            start_text = start_text + tag.get_text()
        elif tag.name in ("h1", "h2", "h3", "h4"):
            try:
                out = False
                for tagC in tag.children:
                    if tagC.get('id') in blocked_sources:
                            print("STOP NOW")
                            out = True
                            break
                
                if out:
                    break
            except Exception as inst:
                print("skip")
            start_text = start_text +  "<" + tag.name + ">" + tag.get_text() +"</" + tag.name + ">"
        elif tag.name == 'ul' or tag.name == 'ol' or tag.name == 'dl':
            start_text = start_text + tag.get_text()+".\n"
    return start_text


def compose_page_wiki(page):
    page_encoded = str(page.get_attribute('innerHTML').encode("utf_8").decode())

    page_html_format = "<html><head></head><body>" + page_encoded + "</body></html>"

    page_no_table_figure = remove_table(page_html_format)
    page_no_table_figure = remove_figure(page_no_table_figure)

    page_to_bs = BeautifulSoup(page_html_format, 'html.parser')
    remove_infobox(page_to_bs)
    remove_figcap(page_to_bs)
    remove_style(page_to_bs)
    remove_thumbnails(page_to_bs)
    remove_sup(page_to_bs)
    remove_editSection(page_to_bs)
    remove_math(page_to_bs)
    remove_img(page_to_bs)
    page_cleaned = remove_final_part(page_to_bs)

    return page_cleaned


def compose_page_vikidia(page):
    page_encoded = str(page.get_attribute('innerHTML').encode("utf_8").decode())

    page_html_format = "<html><head></head><body>" + page_encoded + "</body></html>"
    page_no_table_figure = remove_table(page_html_format)
    page_no_table_figure = remove_figure(page_no_table_figure)
    
    page_to_bs = BeautifulSoup(page_no_table_figure, 'html.parser')
    
    remove_infobox(page_to_bs)
    remove_figcap(page_to_bs)
    remove_style(page_to_bs)
    remove_thumbnails(page_to_bs)
    remove_sup(page_to_bs)
    remove_editSection(page_to_bs)
    remove_math(page_to_bs)
    remove_img(page_to_bs)

    page_cleaned = remove_final_part_viki(page_to_bs)

    return page_cleaned


def page_scrape(url_animal, link,  by, value_by, driver, path, type):
    wiki_page = access_retrieve_main_data(link+url_animal,
                                          by,
                                          value_by,
                                          driver)
    if type == "wiki":
        page_cleaned = compose_page_wiki(wiki_page)
    else:
        page_cleaned = compose_page_vikidia(wiki_page)
    
    with open(path, 'w', encoding="utf_8") as animal_wiki:
        animal_wiki.write(page_cleaned)