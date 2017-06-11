def crawl_web(seed):
	tocrawl = [seed]
	crawled = []
	index={}
	while tocrawl:
		page = tocrawl.pop()
		if page not in crawled:
			content=get_page(page)
			add_page_to_index(index,page,content)
			union(tocrawl, get_all_links(get_page(content))
			crawled.append(page)  


def add_page_to_index(index, url, content):
	words = content.split()
	for word in words:
		add_to_index(index,word,url)


def add_to_index(index, keyword, url):
	if keyword in index:
    index[keyword].append(url)
  else:
	  # not found, add a new keyword to index
	  index[keyword] = [url]

def lookup(index, keyword):
  if keyword in index:
    return index[keyword]
return None
