import csv
import json
import urllib2
import sys
import constants
from time import sleep


reload(sys)
sys.setdefaultencoding('utf-8')

with open('fb_page_id_list.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    with open('page_info.csv', 'wb') as csvfile:
        while True:
            try:
                fieldnames = ['page_id', 'page_name', 'fan_count', 'category']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for row in reader:
                    page_id = row['page_id']
                    access_token = "<FILL IN>"
                    api = "https://graph.facebook.com/v2.10/{0}?fields=name%2Ccategory%2Cfan_count%2Cis_community_page&access_token={1}".format(
                        page_id, access_token)
                    try:
                        fb_likes = urllib2.urlopen(api)

                    except urllib2.URLError, e:
                        if hasattr(e, 'code'):
                            if e.code == 408:
                                print 'Timeout ', e.code
                            if e.code == 404:
                                print 'File Not Found ', e.code

                    fb_json = fb_likes.read()
                    fb_data = json.loads(fb_json)
                    print  fb_data["name"]
                    #sleep(1) 

                    writer.writerow(
                        {'page_id': fb_data["id"], 'page_name': fb_data["name"], 'fan_count': fb_data["fan_count"],
                         'category': fb_data["category"]})
                sys.exit()
            except ValueError:
                sleep(1) 
