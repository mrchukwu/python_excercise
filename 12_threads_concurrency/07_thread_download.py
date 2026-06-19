import threading
import requests
import time

def download(url):
  print(f"Starting download  {url}")
  resp = requests.get(url)
  print(f"Finish downloading from {url}, size: {len(resp.content)} bytes")

urls = [
  "http://httpbin.org/image/jpeg",
  "http://httpbin.org/image/png",
  "http://httpbin.org/image/svg",
]

start = time.time()
threads = []

for url in urls:
  t = threading.Thread(target=download, args=(url,  ))
  t.start()
  threads.append(t)

for t in threads:
  t.join()

end = time.time()
print(f"Total time: {end - start:.2f} seconds")