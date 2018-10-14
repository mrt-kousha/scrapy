# -*- coding: utf-8 -*-
import json
import os

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ganjoorPipeline(object):

    def process_item(self, item, spider):
        if item['output_dir'] != '':
            os.system('mkdir -p {}'.format(item['output_dir']))
        else:
            item['output_dir'] = 'data'
            os.system('mkdir -p {}'.format(item['output_dir']))
        with open(item['output_dir']+'/'+item['author']+'.json', 'a+') as file:
            del item['output_dir']
            line = json.dumps(dict(item)) + "\n"
            file.write(line)
            return item