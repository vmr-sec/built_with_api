#!/usr/bin/env python
#most recent backup is in bkup.py

import httplib
import urllib
import json
from os.path import exists

def webrequest(line):
#define a function that accepts the input from the for loop in main()
    url = "https://api.builtwith.com/v11/api.json?KEY=213e029b-e519-48c1-9a35-cb5f2ed2de35&LOOKUP=%s" % line
    response = urllib.urlopen(url)
    r = response.read()
    # Create a request to the URL and read the response
    filename = '/Users/vrajkumar/Desktop/Python/Project/files/%s.json' % line
    if exists(filename) == False:
    #Function used to check for the existance of a file
        with open(filename, 'w') as directory:
            directory.write(r)
            directory.close()
            #Write the output into a json file with the hostname as the filename
    return;

def search(line, component):

    search_file = '/Users/vrajkumar/Desktop/Python/Project/files/%s.json' % line
    with open(search_file, 'r') as data_file:
    #opens the file in the read mode, file name is sent by function dnl_search()
        data = json.load(data_file)
        #load the json file
        x = 0
    for elem in data['Results'][0]['Result']['Paths'][0]['Technologies']:
        #loop to match all elements
        name = elem['Name']
        if name == component:
            print "Found in %s" %line
            x = 1
        else:
            x = x + 0
        #Returning these values to print appropriate statements
    return x;

def disp_all(all_comp):

    url = "https://api.builtwith.com/v11/api.json?KEY=213e029b-e519-48c1-9a35-cb5f2ed2de35&LOOKUP=%s" % all_comp
    response = urllib.urlopen(url)
    r = response.read()
    filename = "temp.json"
    with open(filename, 'w') as temp_file:
        temp_file.write(r)
        temp_file.close()

    with open(filename, 'r') as temp_read:
        data = json.load(temp_read)
    count = 0
    for elem in data['Results'][0]['Result']['Paths'][0]['Technologies']:
        #print elem['Description']
        print elem['Name']
        print elem['Link']
        print elem['FirstDetected']
        print elem['LastDetected']
        print elem['Tag']
        print '\n\n'
        count = count + 1

    print "This site has a total of %i components" %count
    return;

def view_all():
    print """Do you want to view all components of a particular domain ?
If yes enter the domain name, if no enter N."""
    all_comp=raw_input(">").lower()

    if all_comp != "n":
        disp_all(all_comp)

    Main()
    return;

def download():

    print "Enter file name that has the domain list"
    fname = raw_input('>')
    domains = open(fname)
    print "\n"

    print "Working on your request\n"
    for line in domains:
        webrequest(line)
        #reads the domains iteratively from file and sends to the function
    print "Write completed to respective files\n"

    Main()
    return;

def dnl_search():

    print "Enter file name that has the domain list"
    fname = raw_input('>')
    domains = open(fname)
    print "\n"

    print "\nEnter the name of the vulnerable component"
    component = raw_input('>')
    #should be used in search after getting the components
    print "\n"

    print "Searching data from domains with component: %s\n" %component
    domains = open(fname)
    #Reopening the file so the for loop can read the domains interatively
    z = 0
    #Using this variable to print appropriate results
    for line in domains:
    #loop to search
        y = search(line, component)
        if y == 1:
            z = z + y

    if z == 0:
        print "Component not found in any domain\n"

    Main()
    return;


def Main():

    print """\nThis program lets you view or download a technology stack from individual
domains or a list of domains belonging to Intuit."""

    print """\nWhat would you like to do ?
1. View all components runnign on one domain.
2. Download all components of multiple domains into files.
3. Search several domains for any component.
4. Exit program"""

    choice = int(raw_input('>'))

    print "\n"

    if choice == 1:
        view_all()
    elif choice == 2:
        download()
    elif choice == 3:
        dnl_search()
    elif choice == 4:
        print "Exiting program."

Main()


