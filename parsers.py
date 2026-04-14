from bs4 import BeautifulSoup

def synonyms_antonyms_parser_v2(response):
    """
    Parses the HTML returned by the website.
    This should work for both antonyms and synonyms

    I believe this could be done better with a fields list (wordtype, tabdesc... and so on)
    and then using another list/dictionary inside the loop to check if we came across one of these fields and thus detect the boundary
    """
    result = []
    soup = BeautifulSoup(response.text, 'html.parser')
    outer_table = soup.find("table", {"id":"contenttable"})
    inner_table = outer_table.find("table")

    current_word={}
    to_find = {"wordtype":0, "tabdesc":0, "relatedwords":0, "tabexample":0}
    elements = inner_table.find_all()
    for element in elements:
        element_class = (element.attrs.get("class"))
        if (element_class) and ((element_class[0] in to_find)):
            if (to_find[element_class[0]]==0):
                current_word[element_class[0]] = element.text
                to_find[element_class[0]] += 1
            elif (to_find[element_class[0]]>0):
                if len(current_word)>0:
                    result.append(current_word)
                    current_word={}
                    current_word[element_class[0]]=element.text
                to_find = {"wordtype":0, "tabdesc":0, "relatedwords":0, "tabexample":0}
                to_find[element_class[0]]=1

    if current_word:
        result.append(current_word)

    print(result)