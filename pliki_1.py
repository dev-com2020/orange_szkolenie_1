import json
from xml.dom import minidom

json_text = str()
with open('json_example.json', 'r') as f:
    json_text = f.read()

data = json.loads(json_text)
# print(data)
# print(type(data))
#
# print(data['glossary']["GlossDiv"]["GlossList"])
# print(len(data['glossary']))

domTree = minidom.parse('books.xml')
# print(domTree.toxml())
nodes = domTree.childNodes

print(nodes[0].getElementsByTagName("book")[1].getAttribute('id'))

for i in nodes[0].getElementsByTagName("book"):
    print(i.getElementsByTagName("title")[0].toxml())

