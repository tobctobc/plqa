import requests
try:
    file_url = "http://ospank.com/get_file/1/dc08ca1c3d124fd24dcfe638244c7b60/10000/10559/10559.mp4"
    r = requests.get(file_url, stream=True)
    with open("1.mp4", "wb") as pdf:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                pdf.write(chunk)
except:
    print('1.mp4失败')
try:
    file_url = "http://ospank.com/get_file/1/dc08ca1c3d124fd24dcfe638244c7b60/10000/10559/10559.mp4/?embed=true"
    r = requests.get(file_url, stream=True)
    with open("2.mp4", "wb") as pdf:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                pdf.write(chunk)
except:                
    print('2.mp4失败')
