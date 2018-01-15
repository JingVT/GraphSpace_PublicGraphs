# GrapphSpaces_PublicGraphs

Please open index.html on IE internet browser to see the result.

Purpose:
Uses the GraphSpace REST APIs, documented at http://manual.graphspace.org/en/latest/Programmers_Guide.html#graphspace-rest-api to perform the following tasks.
(i) Compute the number of public graphs stored in GraphSpace.
(ii) For each user who has uploaded at least one public graph, count the number of public graphs uploaded by that user. Sort this information (the user-count pairs) in decreasing order of this number and print it in a well-formatted table.
(iii) For each public graph, download the JSON file for that graph. Parse the file to count the number of nodes and edges in this graph.
(iv) Compute a histogram of the number of nodes in public graphs and another histogram of the number of edges in public graphs. Display both histograms nicely.
(v) Diaplay the result of (ii) and (iv) on an HTML page.

Programming Language:
Python (version Python 2.7.14)
JavaScript
HTML, CSS

JavaScript library: D3

There are two ways to update the data:
(1)	Run “dataFilte.py” manually.
(2)	Run “timer.py” which update the data in every 200 second automatically. 

Total number of public graphs in GraphSpace can be found in “TotalNumberOfPublicGraphs.csv”.

