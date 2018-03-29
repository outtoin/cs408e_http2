import os
from lxml import etree as ET

class Map(object):
    def __init__(self, map):
        self.map_dir = map
        self.new_map = self._get_new_filename(map)
        self.tree = ET.parse(map)
        self.root = self.tree.getroot()
        self.id = self._get_ids()

    def change_color(self, change_dict):
        for child in self.root:
            for key in change_dict.keys():
                if 'path' in child.tag and child.attrib['id'] == key:
                    print('find')
                    child.attrib['fill'] = change_dict[key]
                    break
        self.tree.write(self.new_map)


    def _get_ids(self):
        ret = []
        for child in self.root:
            if 'path' in child.tag:
                ret.append(child.attrib['id'])
        return ret

    def _get_new_filename(self, map):
        base = os.path.basename(map)
        dir = os.path.dirname(map)
        return os.path.join(dir, 'new_' + base)

    def get_id(self):
        return self.id