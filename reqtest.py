import requests
import concurrent.futures
import time

t1 = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = []
    for i in range(0, 100, 1):
        print(f"Sending Request {i}")
        x = executor.submit(requests.get, "https://google.com")
        results.append(x)
    for resX in results:
        print(resX.result())
# for i in range(0, 100, 1):
#     print(f"Sending Request {i}")
#     r = requests.get("https://google.com")
#     print(r)
t2 = time.perf_counter()


print(t2-t1)
