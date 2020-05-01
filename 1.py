import requests
import os
print('hello')
def size_format(size):
    if size < 1000:
        return '%i' % size + 'B'
    elif 1000 <= size < 1000000:
        return '%.1f' % float(size/1000) + 'KB'
    elif 1000000 <= size < 1000000000:
        return '%.1f' % float(size/1000000) + 'MB'
    elif 1000000000 <= size < 1000000000000:
        return '%.1f' % float(size/1000000000) + 'GB'
    elif 1000000000000 <= size:
        return '%.1f' % float(size/1000000000000) + 'TB'

try:
    file_url = "http://ospank.com/get_file/1/dc08ca1c3d124fd24dcfe638244c7b60/10000/10559/10559.mp4"
    r = requests.get(file_url, stream=True)
    with open("1.txt", "wb") as pdf:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                pdf.write(chunk)
    print(size_format(os.path.getsize("1.txt")))
except:
    print('1.mp4失败')
try:
    file_url = "http://ospank.com/get_file/1/dc08ca1c3d124fd24dcfe638244c7b60/10000/10559/10559.mp4/?embed=true"
    r = requests.get(file_url, stream=True)
    with open("2", "wb") as pdf:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                pdf.write(chunk)

    print(size_format(os.path.getsize("2")))                
except:                
    print('2.mp4失败')
