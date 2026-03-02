import requests

url = "https://BaseURLHere"
filetype = ".mp3"
downloadRange = range(1, 114)

# Change writing mode accordingly
# "w"   write (text mode), ex: txt, json
# "wb"  write (binary mode), ex: mp3, png, pdf
writingMode = "wb"

for i in downloadRange:
    urlfullPath = url + str(i).zfill(3) + filetype
    response = requests.get(urlfullPath)
    with open("./download/" + str(i).zfill(3) + filetype, writingMode) as f:
        f.write(response.content)