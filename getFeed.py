#!/usr/bin/python
#
#   https://pythonhosted.org/feedparser/introduction.html
#
#   2020-11-12 - v0.8.0 - Change name (now getFeed.py) and purpose
#
import sys
import feedparser

# 
##################################
# specific to this program, but not used
#
def write2file(name, data):
    f = open(name,'a')
    f.write(data)
    f.close()

##################################

theFeed = ''

if len(sys.argv) > 1:
    theFeed = sys.argv[1]

if len(theFeed) == 0:
    print "\n\tPlease give a URL\n"
    exit(1)
else:
    print theFeed
    #exit(0)

#
#
#theFeed = './bongino'

d = feedparser.parse(theFeed)
#
#
#

print 

if 'title' in d.feed:
    print "Feed Title: ", d['feed']['title'].encode('utf-8', 'ignore')
if 'language' in d.feed:
    print "Feed Language: ", d['feed']['language']
if 'link' in d.feed:
    print "Feed Link: ", d['feed']['link']

print 'number of entries ' + str(len(d['entries']))

no_entries = len(d['entries']) - 1

print ""

for i in range(0, no_entries):
    print "Title: " + d['entries'][i]['title'].encode('utf-8', errors='ignore')
    print "RSS Link: " + d['entries'][i]['link'].encode('utf-8', errors='ignore') 

    if 'guid' in d['entries'][i]:
        print "Perma Link: " + d['entries'][i]['guid']
    #print "Google Search for title: " + 'https://www.google.com/search?q=' + d.entries[i].title.encode('utf-8', errors='ignore').replace(' ', '+') + '&tbs=qdr:d'
    #if 'published' in d.entries[i]:
    #    print "Publish date: " + d.entries[i].published
    #print "Description: " + d['entries'][i]['description'].encode('utf-8')
    print ""

print ""
