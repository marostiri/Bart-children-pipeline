from selenium.webdriver.common.by import By

def recover_available_all_links(driver, url):
    driver.get(url)
    list_htlm_links_possible = driver.find_elements(by=By.CLASS_NAME, value="mw-category-group")
    list_links = []
    for html_link in list_htlm_links_possible:
        links_possible = html_link.find_elements(by=By.TAG_NAME, value="a")
        print(len(links_possible))
        for link in links_possible:
            list_links.append(link.get_attribute('href'))
    print("Qua")
    print(list_links)
    return list_links


class Crawler:
    def __init__(self, driver, starting_url, check_node_tree):
        self.driver = driver
        self.starting_url = starting_url
        self.check_node_tree = check_node_tree
        self.list_link_to_visit = [starting_url]
        self.visited_links = set()
        self.link_pages = []

    def bfs(self):
        while self.list_link_to_visit != []:
            visited = self.list_link_to_visit.pop()
            # Cycle on link on that page
            links_scraped = recover_available_all_links(self.driver, visited)
            for link in links_scraped:
                # If not found check_node_tree, it is leaf
                # if not cotrol, it is already visited, if new is to visit
                if self.check_node_tree not in link:
                    self.link_pages.append(link)
                elif len(self.visited_links & set([link])) == 0:
                    self.list_link_to_visit.append(link)
            self.visited_links.add(visited)

    def write_to_file(self, path):
        with open(path, "w") as f:
            f.writelines(self.link_pages)