from xml.etree.ElementTree import parse

f = open('demo.xhtml')

et = parse(f)
root = et.getroot()
print(root.tag)
print(root.attrib)
print(root.getchildren())
print(root.findall('head/title'))
for child in root:
    print(child.get('name'))