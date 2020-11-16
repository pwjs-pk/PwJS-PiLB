import xml.sax
import xml.sax.saxutils
from math import floor


class Food:

    def __init__(self):
        self.name = None
        self.price = None
        self.description = None
        self.calories = None


class Parser(xml.sax.handler.ContentHandler):

    def __init__(self, file):
        super().__init__()
        self.file = file
        self.CurrentData = ""
        self.current_element = Food()
        self.elements = []

    def startElement(self, tag, attributes):
        self.CurrentData = tag

    def endElement(self, tag):
        self.CurrentData = ""

    def characters(self, content):
        if self.CurrentData == "name":
            self.current_element.name = content
        elif self.CurrentData == "price":
            self.current_element.price = content
        elif self.CurrentData == "description":
            self.current_element.description = content
        elif self.CurrentData == "calories":
            self.current_element.calories = content

        if self.is_element_ready():
            self.elements.append(self.current_element)
            self.current_element = Food()

    def is_element_ready(self):
        return self.current_element.name is not None and \
               self.current_element.price is not None and \
               self.current_element.description is not None and \
               self.current_element.calories is not None

    def parse(self):
        parser = xml.sax.make_parser()
        parser.setContentHandler(self)
        parser.parse(self.file)
        return self.elements


class Writer:

    def __init__(self, foods, file):
        self.foods = foods
        self.file = file

    def write(self):
        with open(self.file, 'w') as f:
            generator = xml.sax.saxutils.XMLGenerator(f)

            generator.startDocument()
            generator.startElement('breakfast_menu', {})

            for food in self.foods:
                generator.startElement('food', {})
                generator.startElement('name', {})
                generator.characters(food.name)
                generator.endElement('name')
                generator.startElement('price', {})
                generator.characters(food.price)
                generator.endElement('price')
                generator.startElement('description', {})
                generator.characters(food.description)
                generator.endElement('description')
                generator.startElement('calories', {})
                generator.characters(food.calories)
                generator.endElement('calories')
                generator.endElement('food')

            generator.endElement('breakfast_menu')
            generator.endDocument()


if __name__ == '__main__':
    file = './samples/simple.xml'
    output_file = './samples/result_simple1a.xml'
    parser = Parser(file)
    foods = parser.parse()

    for food in foods:
        food.calories = str(floor(int(food.calories) * 1.1))

    writer = Writer(foods, output_file)
    writer.write()
