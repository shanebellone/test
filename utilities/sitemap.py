import os


def generate_sitemap():
    domain = "https://shanebellone.com/"
    path = "templates/posts/"
    urls = [(domain + file[:-5]) for file in os.listdir(path)]
    with open(r'static/sitemap.txt', 'w') as sitemap:
        for url in urls:
            sitemap.write("%s\n" % str(url))
    sitemap.close()
