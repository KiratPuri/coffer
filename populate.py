import os, random
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')

import django

django.setup()

from dashboard.models import data

import json

with open("static/jsondata.json", encoding='utf-8') as file:
    date_format = "%B, %d %Y %H:%M:%S"  #January, 20 2017 03:51:24 
    date_string = "January, 20 2017 03:51:24"
    data_list = json.load(file)
    for each in data_list:
        intensity = None if each["intensity"] == "" else each["intensity"]
        relevance = None if each["relevance"] == "" else each["relevance"]
        likelihood = None if each["likelihood"] == "" else each["likelihood"]
        added = None if each["added"] == "" else datetime.strptime(each["added"], date_format) 
        published = None if each["published"] == "" else datetime.strptime(each["published"], date_format)

        field = data.objects.get_or_create(end_year = str(each["end_year"]), intensity = intensity, sector= each["sector"], topic = each['topic'], insight = each['insight'], url = each['url'], region = each['region'], start_year = each["start_year"], impact = each['impact'], added = added,  published = published, country = each['country'], relevance = relevance, pestle = each['pestle'], source = each['source'], title = each['title'], likelihood = likelihood)
