import os


class Reader(object):
    def __init__(self, xml_dir):
        self.xml_dir = xml_dir

    def get_xml_files(self):
        xml_filenames = []
        for xml_filename in os.listdir(self.xml_dir):
            if xml_filename.endswith(".xml"):
                xml_filenames.append(os.path.join(self.xml_dir, xml_filename))
        return xml_filenames
