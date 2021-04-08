#Import dependencies
import os
from ScraperModules.httpscrape import httpscrape
# from ScraperModules.socks4scrape import socks4scrape
# from ScraperModules.socks5scrape import socks5scrape

httpscrape()

#User input options
# while True:
    # try:
        # choice = int(input("\n[1] Scrape HTTP Proxies\n\n[2] Scrape SOCKS4 Proxies\n\n[3] Scrape SOCKS5 Proxies\n\n"))
        # if choice not in (1, 2 ,3):
            # print("\nPlease pick one of the choices above")
        # else:
            # break

    # except ValueError:
        # print("\nPlease pick one of the choices above")

# if choice == 1:
    # httpscrape()
# elif choice == 2:
    # socks4scrape()
# elif choice == 3:
    # socks5scrape()