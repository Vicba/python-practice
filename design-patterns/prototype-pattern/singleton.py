import urllib.parse
import urllib.request

# Define a metaclass 'SingletonType' for creating singleton instances
class SingletonType(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


# Define the URLFetcher class using the SingletonType metaclass
class URLFetcher(metaclass=SingletonType):
    def __init__(self):
        self.urls = []
    
    def fetch(self, url):
        req = urllib.request.Request(url)
        
        with urllib.request.urlopen(req) as response:
            if response.code == 200:
                the_page = response.read()
                print(the_page)
                
                urls = self.urls
                urls.append(url)
                self.urls = urls
            
    def dump_url_registry(self):
        # Return a string representation of the list of fetched URLs
        return ', '.join(self.urls)


def main():
    MY_URLS = ['http://www.voidspace.org.uk', 
               'http://google.com', 
               'http://python.org',
               'https://www.python.org/error',
               ]

    print(URLFetcher() is URLFetcher())

    fetcher = URLFetcher()

    # Iterate through the sample URLs and fetch them using the URLFetcher instance
    for url in MY_URLS:
        try:
            fetcher.fetch(url)
        except Exception as e:
            print(e)
    
    print('-------')
    
    done_urls = fetcher.dump_url_registry()
    
    print(f'Done URLs: {done_urls}')


if __name__ == '__main__':
    main()
