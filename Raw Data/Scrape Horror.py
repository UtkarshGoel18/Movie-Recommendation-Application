from bs4 import BeautifulSoup
import requests
source = requests.get('https://www.imdb.com/search/title?genres=horror&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=17d3863a-3e07-4c9b-a09a-f643edc8e914&pf_rd_r=WFJXJRT0XK3G83FGRHF1&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_13').text
soup = BeautifulSoup(source,'lxml')
i=0
print('Genere : HORROR')
while(i<5):
  movie = soup.find_all('div', class_='lister-item-content')[i]
  name= movie.h3.a.text
  try:
    rating= movie.div.div['data-value']
  except Exception as e:
    rating= 'N/A'
  description=movie.find_all('p', class_='text-muted')[1].text
  i=i+1
  print(i,'-',name)
  print('  Rating :',rating)
  print('  About :',description)
  print()
  


