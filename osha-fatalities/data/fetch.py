from lxml import html as htmlparser
from pathlib import Path
from urllib.parse import urljoin
import requests

LANDING_PAGE_URL = 'https://www.osha.gov/dep/fatcat/dep_fatcat_archive.html'
DATA_DIR = Path(__file__).parent.joinpath('raw')


def fetch_all():
    print("Downloading", LANDING_PAGE_URL)
    hdoc = htmlparser.fromstring(requests.get(LANDING_PAGE_URL).text)
    for href in hdoc.xpath('//a[contains(@href, "csv")]/@href'):
        url = urljoin(LANDING_PAGE_URL, href)
        print("Downloading", url)
        resp = requests.get(url)
        fname = DATA_DIR.joinpath(Path(href).name)
        print("Saving to", fname)
        fname.write_text(resp.text)



if __name__ == '__main__':
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    fetch_all()
