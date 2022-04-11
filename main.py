from scrapping import Crawling

if __name__ == "__main__":
    # 0~100
    # for i in range(1, 100):
    #     url = f"https://1xbet.whoscored.com/Players/{91909+i}/History"
    #     Crawling(url).setting()
    #     scrapped = Crawling(url)
    #     scrapped.run()

    url = "https://1xbet.whoscored.com/Players/91908/History"
    Crawling(url).setting()
    scrapped = Crawling(url)
    scrapped.run()

    # url = "https://1xbet.whoscored.com/Players/3203/History"
    # Crawling(url).setting()
    # scrapped = Crawling(url)
    # scrapped.run()

    # url = "https://1xbet.whoscored.com/Players/91910/history"
    # Crawling(url).setting()
    # scrapped = Crawling(url)
    # scrapped.run()
