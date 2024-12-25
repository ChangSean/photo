import os
import requests 

data = []
with open('photos.csv','r', encoding='utf8') as f:
    for row in f:
        data.append(row.strip())

cats = []
dogs = []
for d in data:
    s = d.split(',')

    id = s[0]
    download_count = int(s[1])
    url = s[2]
    tags = s[3:]

    if 'cat' in tags:
        cats.append([url,download_count,id])
    if 'dog' in tags:
        dogs.append(url)

print('Number of cats:',len(cats))
print('Number of dogs:',len(dogs))

if not os.path.exists('cats'):
    os.makedirs('cats')

count = 0
for url,download_count,id in cats:
    count += 1
    print('downloading',count,url)
    filename = f'{download_count}_{id}.jpg' #str(download_count)+'_'+ id + '.jpg'
    response = requests.get(url)
    with open(os.path.join('cats',filename),'wb') as f:
        f.write(response.content)