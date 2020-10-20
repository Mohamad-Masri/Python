import random
import urllib.request


def dl(url):
    imgName = str(random.randrange(0, 1000)) + '.jpg'
    urllib.request.urlretrieve(url, imgName)

dl(https://www.google.com/webhp?hl=en&ictx=2&sa=X&ved=0ahUKEwis5JqrstLcAhVlK8AKHbKJCSAQPQgD)