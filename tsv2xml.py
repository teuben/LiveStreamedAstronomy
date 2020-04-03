#! /usr/bin/env python
#
#  convert a | separated CSV/TSV file into an RSS feed.xml file
#
#  Example taken for the corona induces AAS listing of live-streamed events
#
#  Another example is the CADC meeting RSS feed,which seems to be using
#  http://www1.cadc-ccda.hia-iha.nrc-cnrc.gc.ca/cadcbin/meetings/rss-meetings.py
#
# https://docs.google.com/feeds/download/spreadsheets/Export?key<FILE_ID>&exportFormat=csv&gid=0

from astropy.io import ascii
import numpy as np

def html(text):
    """ surely must be a better way
    """
    if type(text) == np.str_:
        return text.replace('&','&amp;')
    return text

comment = "<! -- %s -->"

header = """<?xml version="1.0" encoding="utf-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
<channel>
  <atom:link href="https://teuben.github.io/ACOM/rss.xml" rel="self" type="application/rss+xml" />

  <title>
    Live-Streamed Astronomy Presentations &amp; Events V4
  </title>
  <description>

    As a service to the community, the AAS is compiling a list of
    live-streamed astronomy presentations and events --
    both those intended for professional astronomers and those intended for a wider audience.


  </description>
  <link>
    https://aas.org/posts/news/2020/03/live-streamed-astronomy-presentations-events
  </link>
"""

footer = """
</channel>
</rss>
"""


csvfile = 'Live-Streamed Astronomy Presentations & Events (Responses).csv'
tsvfile = 'Live-Streamed Astronomy Presentations & Events (Responses) - Form Responses 1.tsv'

#data = ascii.read(csvfile, format='csv', delimiter='|')
data = ascii.read(tsvfile, format='csv', delimiter='\t')
n = len(data)
#print(data.colnames)

# 0: data entered>
# 1: Presentation/Event Topic or Title
# 2: Presentation/Event Sponsor
# 3: Intended Audience
# 4: Presenter Name(s) & Affiliation(s)        <author> ???
# 5: Date
# 6: Start Time
# 7: Time Zone
# 8: URL for Live-Stream and/or More Information
# 9: Notes/Comments

print(header)    

for i in range(n,0,-1):
    # print(i,data[i][0],data[i][1])
    title = html(data[i-1][1])

    print(" <item>")
    print("  <title> %s </title>" % html(data[i-1][1]))
    print("  <description>")
    print("     Presentation/Event Sponsor: %s&lt;br&gt;"  % html(data[i-1][2]))
    print("     Intended Audience: %s&lt;br&gt;" % html(data[i-1][3]))
    print("     Presenter Name(s)  &amp; Affiliation(s): %s&lt;br&gt;" % html(data[i-1][4]))
    print("     Date: %s&lt;br&gt;" % html(data[i-1][5]))
    print("     Start Time: %s&lt;br&gt;" % html(data[i-1][6]))
    print("     Time Zone: %s&lt;br&gt;" % html(data[i-1][7]))
    print("     Notes: %s&lt;br&gt;" %  html(data[i-1][9]))
    print("     &lt;br&gt;")
    print("     URL: %s&lt;br&gt;" %  html(data[i-1][8]))
    print("  </description>")
    print("  <link> %s </link>" % html(data[i-1][8]))
    print(" </item>\n")
    

print(footer)
