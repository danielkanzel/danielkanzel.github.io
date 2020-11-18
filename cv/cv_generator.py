from jinja2 import Template
import json
from bs4 import BeautifulSoup as bs


me = json.loads(open("cv.json",encoding="utf-8").read())

template = Template(open('template.html', encoding="utf-8").read())


f = open("index.html", "w", encoding="utf-8")
f.write(bs(template.render(person=me), 'html.parser').prettify())
f.close()