from lxml.html import etree
from ..schemas.element import Element
from ..utils.element import children, remove_element, remove_children

LIST_EXTRACTOR_USELESS_TAGS = ['meta', 'style', 'script', 'link', 'video', 'audio', 'iframe', 'source', 'svg',
                               'path', 'symbol', 'img', 'footer', 'header']
LIST_EXTRACTOR_STRIP_TAGS = ['span', 'blockquote']
LIST_EXTRACTOR_NOISE_XPATHS = [
    '//div[contains(@class, "comment")]',
    '//div[contains(@class, "advertisement")]',
    '//div[contains(@class, "advert")]',
    '//div[contains(@style, "display: none")]',
]


def preprocess4list_extractor(element: Element):
    """
    preprocess element for list extraction
    :param element:
    :return:
    """
    # remove tag and its content
    etree.strip_elements(element, *LIST_EXTRACTOR_USELESS_TAGS)
    # only move tag pair
    etree.strip_tags(element, *LIST_EXTRACTOR_STRIP_TAGS)

    remove_children(element, LIST_EXTRACTOR_NOISE_XPATHS)

    for child in children(element):

        # merge text in span or strong to parent p tag
        if child.tag.lower() == 'p':
            etree.strip_tags(child, 'span')
            etree.strip_tags(child, 'strong')

            if not (child.text and child.text.strip()):
                remove_element(child)

        # if a div tag does not contain any sub node, it could be converted to p node.
        if child.tag.lower() == 'div' and not child.getchildren():
            child.tag = 'p'
