from PIL import Image
import requests
import numpy as np

def download_img(url):
    img = Image.open(requests.get(url, stream=True).raw)
    img = np.array(img.getdata())
    img = np.resize(img, (40, int(len(img)/40), 3))
    return img

def img_to_code(url):
    img = download_img(url)
    length = len(img[0])
    column = 20
    array = []
    while column < length:
        for i in img[5][column]:
            array.append(i)
        column = column + 40
    return array

flag_url = "https://cryptoengine.stillhackinganyway.nl/flag"
flag = img_to_code(flag_url)
print(flag)

url = "https://cryptoengine.stillhackinganyway.nl/encrypt?text="
text = "fla"

enc_text = img_to_code(url+text)
possible = "abcdefABCDEF0123456789"

while len(enc_text) < len(flag):
    len_enc = len(enc_text)
    cur_three = ""
    start = 0
    if(text == "fla"):
        cur_three = "g{"
        start = 2
    for i in range(start, 3):
        for x in possible:
            temp = cur_three + x #guess next letter
            temp = temp + "a"*(3-len(temp)) #fill to three letters
            temp_url = url+text+temp #concatenate url
            print(temp_url)
            attempt = img_to_code(temp_url)
            if attempt[len_enc+i] == flag[len_enc+i]: #if guess is correct
                cur_three = cur_three + x
                break
    text = text + cur_three
    enc_text = img_to_code(url+text)