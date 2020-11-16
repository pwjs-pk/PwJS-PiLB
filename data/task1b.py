from xml.dom import minidom
import re

if __name__ == '__main__':
    discount = 0.7
    path = './samples/simple.xml'
    parsed = minidom.parse(path)
    collection = parsed.documentElement
    foods = collection.getElementsByTagName('food')

    regex = re.compile('\d+?\.\d*')

    for food in foods:
        current_price = food.getElementsByTagName('price')[0].childNodes[0].data
        value = float(re.findall(regex, current_price)[0])
        new_value = format(value * discount, '.2f')
        food.getElementsByTagName('price')[0].childNodes[0].data = f"${new_value}"

    with open('./samples/result_simple1b.xml', 'w') as f:
        f.write(parsed.toxml())
