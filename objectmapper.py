import declxml as xml
import os


class ObjectMapper(object):
    def __init__(self):
        self.processor = xml.dictionary("annotation", [
            xml.string("filename"),
            xml.dictionary("size", [
                xml.integer("width"),
                xml.integer("height"),
            ]),
            xml.array(
                xml.dictionary("object", [
                    xml.string("name"),
                    xml.dictionary("bndbox", [
                        xml.integer("xmin"),
                        xml.integer("ymin"),
                        xml.integer("xmax"),
                        xml.integer("ymax"),
                    ], alias="box")
                ]),
                alias="objects"
            ),
        ])

    def bind(self, xml_file_path):
        return xml.parse_from_file(self.processor, xml_file_path=xml_file_path)

    def serialize(self, annotation, xml_file):
        if os.path.exists(xml_file):
            os.remove(xml_file)

        with open(xml_file, "a+") as f:
            f.write(xml.serialize_to_string(self.processor, annotation, indent='    '))
