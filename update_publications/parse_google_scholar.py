
from bs4 import BeautifulSoup
import sys

page_text = ""
with open(sys.argv[1]) as inf:
    page_text = inf.read()

def parsePage(page):
    soup = BeautifulSoup(page,features="lxml")
    # print(soup)
    res = soup.find(name="table",attrs={"id":"gsc_a_t"}) #,attrs={"id":"main"}
    tr_list = res.findAll("tr",class_="gsc_a_tr")

    tr_string = "\n".join([x.prettify() for x in  tr_list if x.get("get") != "gsc_a_trh"]) 
    if "There are no articles in this profile." not in tr_string:
        return tr_string
    else:
        return ""


table_str = "<table>\n<tr><td><b>Title</b></td><td><b>Cite</b></td><td><b>Year</b></td></tr>\n"




table_str += parsePage(page_text)

table_str += "</table>"

# table_str.replace(
#     """<tr class="gsc_a_tr">""",
# """<br/><br/>
# <tr class="gsc_a_tr">""")

# Update the links to be absolute paths
table_str = table_str.replace('href="/citations?', 'href="https://scholar.google.com/citations?')

# Write the output to a daily publication HTML file
# with open("./daily_pub.html", "w") as outf:
#     outf.write(table_str)

# Assuming you need to inject this into a template file
with open("./publications_template.html") as inf, open("../_includes/publications.html", "w") as outf:
    template = inf.read()
    updated_template = template.replace("<!--Injection_Point_Do_Not_delete-->", table_str)
    outf.write(updated_template)
