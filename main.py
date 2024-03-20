# -*- coding: utf-8 -*-
from html_auto_extractor.extractors.list import extract_list
from html_auto_extractor.utils.tools import open_html

html = open_html('html/demo.html')
# print(html)
r = extract_list(html)
print(r)
