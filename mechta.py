import bs4
import urllib.request
import json
name = []
price = []
image_url = []
disc=[]
url = 'www.mechta.kz'
source = urllib.request.urlopen('https://www.mechta.kz/section/noutbuki-7n9/')
soup = bs4.BeautifulSoup(source,'lxml')
nout_web = soup.findAll("a", {"class": "aa_st_imglink j_product_link"})
info_nout_web = soup.findAll("div", {"class": "aa_std_props ifont12"})
for i in range(len(nout_web)):
    temp = json.loads(nout_web[i]['data-seo'])
    temp_url = str(nout_web[i]['style']).replace("background-image: url('", '').replace("'); height: 100%;", '')
    price.append(temp['price'])
    name.append(temp['name'])
    image_url.append(str(url+temp_url))
for i in range(len(info_nout_web)):
    temp = ''
    for j in info_nout_web[i]:
        if not j.string:
            pass
        else:
            temp = temp +j.string
    disc.append(temp)
