from bs4 import BeautifulSoup


def synonyms_antonyms_parser(response):
    """
    Parses the HTML that is returned by the website.
    This works both for the antonyms and synonyms
    """
    result = []
    soup = BeautifulSoup(response.text, 'html.parser')
    word_type_divs = soup.find_all("div", class_="wordtype")

    # for i in word_type_divs:
    #         print(i.text)
    #         print("++++++++")
    
    for word_type_div in word_type_divs:
        temp_result = {}
        tabdesc_div = word_type_div.find_next_sibling("div", class_="tabdesc")
        if tabdesc_div:
            relatedwords_div = tabdesc_div.find_next_sibling("div", class_="relatedwords")
            # related_words = relatedwords_div.find_all("div", class_="wb")
            related_words_list = [related_word.get_text(strip=True) for related_word in relatedwords_div.find_all("div", class_="wb")]
            if relatedwords_div:
                tabexample_div = relatedwords_div.find_next_sibling("div", class_="tabexample")

        temp_result.update({
            "word_type":word_type_div.text, 
            "tabdesc": tabdesc_div.text if tabdesc_div else "", 
            "related_words":related_words_list, 
            "table_example": tabexample_div.get_text() if tabexample_div else ""})
        
        result.append(temp_result)

    print(result[0])


def parser_v2(response):
    result = []
    soup = BeautifulSoup(response.text, 'html.parser')
    outer_table = soup.find("table", {"id":"contenttable"})
    inner_table = outer_table.find("table")

    print(inner_table)