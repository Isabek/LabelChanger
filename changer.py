import argparse

import os

import sys

from objectmapper import ObjectMapper
from reader import Reader


class Changer(object):
    def __init__(self, xml_dir, out_dir):
        self.xml_dir = xml_dir
        self.out_dir = out_dir

    def change(self, from_label, to_label):
        reader = Reader(self.xml_dir)
        xml_file_paths = reader.get_xml_files()
        object_mapper = ObjectMapper()

        for xml_file_path in xml_file_paths:
            annotation = object_mapper.bind(xml_file_path)
            for obj in annotation["objects"]:
                if obj["name"] == from_label:
                    obj["name"] = to_label
            object_mapper.serialize(annotation, os.path.join(self.out_dir, os.path.basename(xml_file_path)))

        print("%s file(s) updated" % len(xml_file_paths))


def main():
    parser = argparse.ArgumentParser(description="Changes labels from old to new")
    parser.add_argument("-xml", help="Location of xml files directory", required=True)
    parser.add_argument("-out", help="Location of updated xml files directory", default="out")
    parser.add_argument("-old_label", help="Old Label", required=True)
    parser.add_argument("-new_label", help="New Label", required=True)
    args = parser.parse_args()

    xml_dir = os.path.join(os.path.dirname(os.path.realpath('__file__')), args.xml)
    if not os.path.exists(xml_dir):
        print("Provide the correct folder for xml files.")
        sys.exit()

    out_dir = os.path.join(os.path.dirname(os.path.realpath('__file__')), args.out)
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    if not os.access(out_dir, os.W_OK):
        print("%s folder is not writeable.")
        sys.exit()

    changer = Changer(xml_dir, out_dir)
    changer.change(args.old_label, args.new_label)


if __name__ == "__main__":
    main()
