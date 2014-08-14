# -*- coding: utf-8 -*-

import json

class DpPipeline(object):

    def __init__(self):
        self.file = open('dp.json', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item
