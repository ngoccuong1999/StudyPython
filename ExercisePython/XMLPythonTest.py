import xml.etree.ElementTree as ET
input = '''<stuff>
    <users>
        <user x = "2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x = "7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input)
listUser = stuff.findall('users/user')
print("List User: ", listUser)
print("length: ", len(listUser))

for items in listUser :
    print('id: ', items.find('id').text)
    print('name: ', items.find('name').text)
    print('Attribute', items.get('x'))
