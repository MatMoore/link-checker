from persistence import put_urls
import fileinput
from urllib.parse import urlparse

def parse_input():
    for line in fileinput.input():
        line = line.strip()
        if not line:
            continue

        parsed = urlparse(line, scheme='https')
        if not parsed.netloc:
            raise ValueError(f'Invalid URL [{url}]')

        yield line


if __name__ == '__main__':
    urls = list(parse_input())
    print(f'Storing URLs {urls}')
    put_urls(urls)