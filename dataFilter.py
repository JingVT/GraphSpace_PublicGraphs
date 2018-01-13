import urllib2, base64
#import urllib.request
import base64
import json
import collections
import operator
import csv
import os.path

#all urls referenced in this file have the following base:
urlBase = "http://www.graphspace.org/api/v1/graphs"

def getData( param ):
    url_key = urlBase;
    url = url_key + param
    #request = urllib.request.Request(url)
    request = urllib2.Request(url)
    base64string = base64.b64encode('%s:%s' % ("jcui85@vt.edu", "Cjing_1185426"))
    request.add_header("Authorization", "Basic %s" % base64string)
    #credentials = ('%s:%s' % ("jcui85@vt.edu", "Cjing_1185426"))
    #encoded_credentials = base64.b64encode(credentials.encode('ascii'))
    #request.add_header('Authorization', 'Basic %s' % encoded_credentials.decode("ascii"))
    request.add_header("Content-Type", "application/json") 
    request.add_header("Accept","application/json")
    result = urllib2.urlopen(request)
    #result = urllib.request.urlopen(request)

    return json.load(result)

#data for all public graphs stored in GraphSpace
publicTotal = getData( "?is_public=1&limit=1000" )


#TotalNumber of public graphs stored in GraphSpace
totalNumberOfPublicGraphs = len(publicTotal["graphs"]) #alternative way: publicTotal["total"]


#sort users by the number of ownered public graphs in decreasing order
count = {};
for element in publicTotal["graphs"]:
    if element["owner_email"] in count:
       count[element["owner_email"] ] += 1
    else:
       count[element["owner_email"] ] = 1

orderedCount = sorted(count.items(), key = lambda t: t[1], reverse = True)


#count the number of nodes and edges in each public graph
publicNodes = {};
publicEdges = {};
for element in publicTotal["graphs"]:
    id = element["id"]
    publicEach = getData( "/" + str(id) )
    publicNodes[element["name"]] = len(publicEach["graph_json"]["elements"]["nodes"])
    publicEdges[element["name"]] = len(publicEach["graph_json"]["elements"]["edges"])


#write result to .csv file
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


with open(os.path.join(__location__, "TotalNumberOfPublicGraphs.csv"), "wb") as f:
   writer = csv.writer(f)
   writer.writerow(['TotalNumberOfPublicGraphs', totalNumberOfPublicGraphs])

with open(os.path.join(__location__, "TotalPublicGraphs.csv"), "wb") as f:
   writer = csv.writer(f)
   writer.writerow(['Graph Owner', 'Number of Public Graphs'])
   writer.writerows(orderedCount)


with open(os.path.join(__location__, "TotalPublicNodes.csv"), "wb") as f:
   writer = csv.writer(f)
   writer.writerow(['Name', 'Nodes'])
   for key, value in publicNodes.items():
      writer.writerow([key, value])


with open(os.path.join(__location__, "TotalPublicEdges.csv"), "wb") as f:
   writer = csv.writer(f)
   writer.writerow(['Name', 'Edges'])
   for key, value in publicEdges.items():
      writer.writerow([key, value])


