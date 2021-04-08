# Import dependencies
import requests
import re
from ScraperModules import variables

#Create the socks5scrape function
def socks5scrape():

    #Clear contents of the output file
    file = open('proxylistsocks5.txt', 'w')
    file.write("")
    file.close()

    #Send the HTTP requests
    for urlno, url in enumerate (variables.socks5urls):
        print("Scraping SOCKS5 source " + str(urlno) + "...\n")
        data = requests.get(url, headers=variables.headers)
        proxiesdata = str(data.text)

        #Look for regex matches in the html body of the websites
        matches = re.finditer(variables.regex, proxiesdata)

        #List the proxy matches
        for matchnumber, match in enumerate(matches, start=1):
            matchnumber = 1
            #Save the proxies in ip:port format
            proxies = "{ip}:{port}".format(ip = match.group(matchnumber), port = match.group(matchnumber + 1))
            saveproxies = "\n" + proxies
            file = open('proxylistsocks5.txt', 'a')
            file.write(saveproxies)
            file.close()
    #Verify that all lines are real proxies
    print("\nVerifying that all lines are proxies...\n")
    textfile = open('proxylistsocks5.txt', 'r')
    vf = textfile.read()
    textfile.close()
    matches = re.findall(r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b:\d{2,5}', vf)
    verify = open('proxylistsocks5.txt', 'w')
    verify.writelines("\n".join(matches))

    #Remove duplicate proxies
    print("\nRemoving duplicate proxies...\n")
    uniquelines = set(open('proxylistsocks5.txt').readlines())
    rm = open('proxylistsocks5.txt', 'w')
    rm.writelines(set(uniquelines))
    rm.close()

    #Count number of proxies scraped
    with open('proxylistsocks5.txt') as f:
        number = sum(1 for _ in f)
    print("\nFinished scraping! " + (str(number)) + " SOCKS5 proxies have been saved to proxylistsocks5.txt.")

    #Exit the function
    return
