import requests
import time
from worker_threadpool import Worker, ThreadPool

start_time = time.time()
lines = [open("test_taylor.txt", "r").readlines()][0]
pool = ThreadPool(45)

def post(line):
    r = requests.post("http://127.0.0.1:8000/", json=line)
    print(r.text)

pool.map(post, lines)
pool.wait_completion()

print("--- %s seconds ---" % (time.time() - start_time))