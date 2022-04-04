from scrapping import Crawling

if __name__ == "__main__":

    for i in range(1):
        url = f"https://1xbet.whoscored.com/Players/{91909+i}/History"

        scrapped = Crawling(url)
        scrapped.run()
