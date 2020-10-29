from bitlyshortener import Shortener
# get access toke from bitly
tokens_pool = ['f3afbf82e53c51c95dab8944bddecab753a833cb']
shortener = Shortener(tokens=tokens_pool, max_cache_size=128)
# get url into list
url = []
get_url = input("Enter url: ")
url.append(get_url)

# sort using bitly
sort_url = shortener.shorten_urls_to_dict(url, domain="bit.ly")
print("sort url: ", sort_url)
