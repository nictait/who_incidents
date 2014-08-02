# This is a template for a Python scraper on Morph (https://morph.io)
# including some code snippets below that you should find helpful

# import scraperwiki
# import lxml.html
#
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries. You can use whatever libraries are installed
# on Morph for Python (https://github.com/openaustralia/morph-docker-python/blob/master/pip_requirements.txt) and all that matters
# is that your final data is written to an Sqlite database called data.sqlite in the current working directory which
# has at least a table called data.
#!/usr/bin/env python

import scraperwiki
import requests
import lxml.html

scraperwiki.sqlite.execute("drop table if exists swdata")

#html = requests.get("http://www.who.int/csr/don/archive/disease/ebola/en/")
#print html.content

url = "http://www.who.int/csr/don/archive/disease/ebola/en/"
root = lxml.html.parse(url).getroot()
print root

div = root.xpath( '//div[@id="main"]' )
print div

for row in div:
#    rownum = rownum + 1
    
#    #print row
#    cellnum = 0
#    datacell = 0
    for cell in row.xpath('//td'):
        #if rownum == 1:
        print cell.text_content()
        
      
        #print colnum
        #print cell.text_content()

#url = "http://www.who.int/csr/don/2014_07_31_ebola/en/"

#root = lxml.html.parse(url).getroot()
#print root

#docstr = lxml.html.tostring(root)
##print docstr
#recno = 0


#div = root.xpath( '//div[@id="main"]' )


#print div

#colnum = 0
#rownum = 0

#for row in div:
#    rownum = rownum + 1
    
#    #print row
#    cellnum = 0
#    datacell = 0
#    for cell in row.xpath('//td'):
#        #if rownum == 1:
#            #print cell.text_content()
#        
#        cellnum = cellnum + 1
#        colnum = colnum + 1
#        #print colnum
#        #print cell.text_content()
#        #print cell.attrib['class']
#        print str(cellnum % 6)
#        #print str(cellnum) + " " + cell.text_content()
#        
#        #scraperwiki.sqlite.save(unique_keys=['recno'],data={"recno":cellnum,"country":"","new":""})
#        if cellnum > 6:
#            datacell = datacell + 1
#            if (datacell % 18) == 1:
#                country = cell.text_content()
#            if (datacell % 18) == 8:
#                new = cell.text_content()
#            if (datacell % 18) == 9:
#                confirmed = cell.text_content()
#            if (datacell % 18) == 10:
#                probable = cell.text_content()
#            if (datacell % 18) == 11:
#                suspect = cell.text_content()
#            if (datacell % 18) == 12:
#                total = cell.text_content()    
#            if (datacell % 18) == 0:
#                scraperwiki.sqlite.save(unique_keys=['recno'],data={"recno":cellnum,"country":country,"new":new,"confirmed":confirmed,"probable":probable,"suspect":suspect,"total":total})
                

#print "rows = " + str(rownum)
#print "cells = " + str(cellnum)

#//*[@id="primary"]/table/tbody/tr[2]/td[1]
# Saving data:
# unique_keys = [ 'id' ]
# data = { 'id':12, 'name':'violet', 'age':7 }
# scraperwiki.sql.save(unique_keys, data)
