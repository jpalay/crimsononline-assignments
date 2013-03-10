import re
from lxml import etree

def parse_links_regex(filename):
    """question 2a

    Using the re module, write a function that takes a path to an HTML file
    (assuming the HTML is well-formed) as input and returns a dictionary
    whose keys are the text of the links in the file and whose values are
    the URLs to which those links correspond. Be careful about how you handle
    the case in which the same text is used to link to different urls.
    
    For example:

        You can get file 1 <a href="1.file">here</a>.
        You can get file 2 <a href="2.file">here</a>.
        <a title="hello" href="google.com">lol</a>

    What does it make the most sense to do here? 
    """
    # dict has format {text: [link1, link2]}
    file = None
    try:
        file = open(filename, 'r')
    except IOError:
        print 'I can\'t find "{}"'.format(filename)
        return

    file_contents = file.read()
    file.close()

    match = re.findall(r"<[aA][^href]href=\"([^\"]*)\"[^>]*>[\s]*([^<]*)", file_contents)
    result = dict()
    for m in match:
        if m[1] not in result.keys():
            result[m[1]] = [m[0]]
        elif m[0] not in result[m[1]]:
            result[m[1]].append(m[0])
    return result

def parse_links_xpath(filename):
    """question 2b

    Do the same using xpath and the lxml library from http://lxml.de rather
    than regular expressions.
    
    Which approach is better? (Hint: http://goo.gl/mzl9t)
    """
    # This is way better
    links = etree.parse(filename, etree.HTMLParser()).xpath("//a")
    result = dict()
    for l in links:
        if l.text not in result.keys():
            result[l.text] = [l.get("href")]
        elif l.get("href") not in result[l.text]:
            result[l.text].append(l.get("href"))
    return result


















