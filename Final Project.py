from tkinter import *
from bs4 import BeautifulSoup
import requests
def Comedy():
  root1 = Tk()
  label = Label(root1,text="Genre : COMEDY",fg="black",font=("Courier", 20))
  label.pack(side= TOP)
  source = requests.get('https://www.imdb.com/search/title?genres=comedy&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=17d3863a-3e07-4c9b-a09a-f643edc8e914&pf_rd_r=WFJXJRT0XK3G83FGRHF1&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_5').text
  soup = BeautifulSoup(source,'lxml')
  i=0  
  while(i<5):
    movie = soup.find_all('div', class_='lister-item-content')[i]
    name= movie.h3.a.text
    try:
      rating= movie.div.div['data-value']
    except Exception as e:
      rating= 'N/A'
    description=movie.find_all('p', class_='text-muted')[1].text
    i=i+1
    name=f"{i} -{name}"
    rating=f"Ratings : {rating}"
    description=f"Description : {description}"
    Title= Label(root1,text=name,font=("Times New Roman", 20))
    Title.pack()
    Rate= Label(root1,text=rating)
    Rate.pack()
    Desc= Label(root1,text=description)
    Desc.pack()
  
  root1.mainloop()

def Horror():
  root1 = Tk()
  label = Label(root1,text="Genre : HORROR",fg="black",font=("Courier", 20))
  label.pack(side= TOP)
  source = requests.get('https://www.imdb.com/search/title?genres=horror&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=17d3863a-3e07-4c9b-a09a-f643edc8e914&pf_rd_r=WFJXJRT0XK3G83FGRHF1&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_13').text
  soup = BeautifulSoup(source,'lxml')
  i=0  
  while(i<5):
    movie = soup.find_all('div', class_='lister-item-content')[i]
    name= movie.h3.a.text
    try:
      rating= movie.div.div['data-value']
    except Exception as e:
      rating= 'N/A'
    description=movie.find_all('p', class_='text-muted')[1].text
    i=i+1
    name=f"{i} -{name}"
    rating=f"Ratings : {rating}"
    description=f"Description : {description}"
    Title= Label(root1,text=name,font=("Times New Roman", 20))
    Title.pack()
    Rate= Label(root1,text=rating)
    Rate.pack()
    Desc= Label(root1,text=description)
    Desc.pack()
  
  root1.mainloop()

def Action():
  root1 = Tk()
  label = Label(root1,text="Genre : ACTION",fg="black",font=("Courier", 20))
  label.pack(side= TOP)
  source = requests.get('https://www.imdb.com/search/title?genres=action&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=17d3863a-3e07-4c9b-a09a-f643edc8e914&pf_rd_r=WFJXJRT0XK3G83FGRHF1&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_1').text
  soup = BeautifulSoup(source,'lxml')
  i=0  
  while(i<5):
    movie = soup.find_all('div', class_='lister-item-content')[i]
    name= movie.h3.a.text
    try:
      rating= movie.div.div['data-value']
    except Exception as e:
      rating= 'N/A'
    description=movie.find_all('p', class_='text-muted')[1].text
    i=i+1
    name=f"{i} -{name}"
    rating=f"Ratings : {rating}"
    description=f"Description : {description}"
    Title= Label(root1,text=name,font=("Times New Roman", 20))
    Title.pack()
    Rate= Label(root1,text=rating)
    Rate.pack()
    Desc= Label(root1,text=description)
    Desc.pack()
  
  root1.mainloop()

def SciFi():
  root1 = Tk()
  label = Label(root1,text="Genre : Sci-Fi",fg="black",font=("Courier", 20))
  label.pack(side= TOP)
  source = requests.get('https://www.imdb.com/search/title?genres=sci-fi&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=17d3863a-3e07-4c9b-a09a-f643edc8e914&pf_rd_r=WFJXJRT0XK3G83FGRHF1&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_18').text
  soup = BeautifulSoup(source,'lxml')
  i=0  
  while(i<5):
    movie = soup.find_all('div', class_='lister-item-content')[i]
    name= movie.h3.a.text
    try:
      rating= movie.div.div['data-value']
    except Exception as e:
      rating= 'N/A'
    description=movie.find_all('p', class_='text-muted')[1].text
    i=i+1
    name=f"{i} -{name}"
    rating=f"Ratings : {rating}"
    description=f"Description : {description}"
    Title= Label(root1,text=name,font=("Times New Roman", 20))
    Title.pack()
    Rate= Label(root1,text=rating)
    Rate.pack()
    Desc= Label(root1,text=description)
    Desc.pack()
  
  root1.mainloop()
  
def Romantic():
  root1 = Tk()
  label = Label(root1,text="Genre : ROMANTIC",fg="black",font=("Courier", 20))
  label.pack(side= TOP)
  source = requests.get('https://www.imdb.com/search/title?genres=romance&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=17d3863a-3e07-4c9b-a09a-f643edc8e914&pf_rd_r=WFJXJRT0XK3G83FGRHF1&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_17').text
  soup = BeautifulSoup(source,'lxml')
  i=0  
  while(i<5):
    movie = soup.find_all('div', class_='lister-item-content')[i]
    name= movie.h3.a.text
    try:
      rating= movie.div.div['data-value']
    except Exception as e:
      rating= 'N/A'
    description=movie.find_all('p', class_='text-muted')[1].text
    i=i+1
    name=f"{i} -{name}"
    rating=f"Ratings : {rating}"
    description=f"Description : {description}"
    Title= Label(root1,text=name,font=("Times New Roman", 20))
    Title.pack()
    Rate= Label(root1,text=rating)
    Rate.pack()
    Desc= Label(root1,text=description)
    Desc.pack()
  
  root1.mainloop()

def Animation():
  root1 = Tk()
  label = Label(root1,text="Genre : ANIMATION",fg="black",font=("Courier", 20))
  label.pack(side= TOP)
  source = requests.get('https://www.imdb.com/search/title?genres=animation&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=17d3863a-3e07-4c9b-a09a-f643edc8e914&pf_rd_r=WFJXJRT0XK3G83FGRHF1&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_3').text
  soup = BeautifulSoup(source,'lxml')
  i=0  
  while(i<5):
    movie = soup.find_all('div', class_='lister-item-content')[i]
    name= movie.h3.a.text
    try:
      rating= movie.div.div['data-value']
    except Exception as e:
      rating= 'N/A'
    description=movie.find_all('p', class_='text-muted')[1].text
    i=i+1
    name=f"{i} -{name}"
    rating=f"Ratings : {rating}"
    description=f"Description : {description}"
    Title= Label(root1,text=name,font=("Times New Roman", 20))
    Title.pack()
    Rate= Label(root1,text=rating)
    Rate.pack()
    Desc= Label(root1,text=description)
    Desc.pack()
  
  root1.mainloop()

def Drama():
  root1 = Tk()
  label = Label(root1,text="Genre : DRAMA",fg="black",font=("Courier", 20))
  label.pack(side= TOP)
  source = requests.get('https://www.imdb.com/search/title?genres=drama&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=17d3863a-3e07-4c9b-a09a-f643edc8e914&pf_rd_r=WFJXJRT0XK3G83FGRHF1&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_8').text
  soup = BeautifulSoup(source,'lxml')
  i=0  
  while(i<5):
    movie = soup.find_all('div', class_='lister-item-content')[i]
    name= movie.h3.a.text
    try:
      rating= movie.div.div['data-value']
    except Exception as e:
      rating= 'N/A'
    description=movie.find_all('p', class_='text-muted')[1].text
    i=i+1
    name=f"{i} -{name}"
    rating=f"Ratings : {rating}"
    description=f"Description : {description}"
    Title= Label(root1,text=name,font=("Times New Roman", 20))
    Title.pack()
    Rate= Label(root1,text=rating)
    Rate.pack()
    Desc= Label(root1,text=description)
    Desc.pack()
  
  root1.mainloop()

def Thriller():
  root1 = Tk()
  label = Label(root1,text="Genre : THRILLER",fg="black",font=("Courier", 20))
  label.pack(side= TOP)
  source = requests.get('https://www.imdb.com/search/title?genres=thriller&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=17d3863a-3e07-4c9b-a09a-f643edc8e914&pf_rd_r=WFJXJRT0XK3G83FGRHF1&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_22').text
  soup = BeautifulSoup(source,'lxml')
  i=0  
  while(i<5):
    movie = soup.find_all('div', class_='lister-item-content')[i]
    name= movie.h3.a.text
    try:
      rating= movie.div.div['data-value']
    except Exception as e:
      rating= 'N/A'
    description=movie.find_all('p', class_='text-muted')[1].text
    i=i+1
    name=f"{i} -{name}"
    rating=f"Ratings : {rating}"
    description=f"Description : {description}"
    Title= Label(root1,text=name,font=("Times New Roman", 20))
    Title.pack()
    Rate= Label(root1,text=rating)
    Rate.pack()
    Desc= Label(root1,text=description)
    Desc.pack()
  
  root1.mainloop()


root = Tk()
label = Label(root,text="WELCOME TO MOVIE RECOMMENDATION PROGRAM \n Choose your genre ",bg="black",fg="white")
label.grid(columnspan=4)
button1 = Button(text="Comedy",fg="white",bg="black",width=15,command=Comedy)
button2 = Button(text="Horror",fg="white",bg="black",width=15,command=Horror)
button3 = Button(text="Action",fg="white",bg="black",width=15,command=Action)
button4 = Button(text="Sci-Fi",fg="white",bg="black",width=15,command=SciFi)
button5 = Button(text="Romantic",fg="white",bg="black",width=15,command=Romantic)
button6 = Button(text="Animation",fg="white",bg="black",width=15,command=Animation)
button7 = Button(text="Drama",fg="white",bg="black",width=15,command=Drama)
button8 = Button(text="Thriller",fg="white",bg="black",width=15,command=Thriller)
button1.grid(row=1,column =1)
button2.grid(row=1,column =2)
button3.grid(row=2,column =1)

button4.grid(row=2,column =2)
button5.grid(row=3,column =1)
button6.grid(row=3,column =2)
button7.grid(row=4,column =1)
button8.grid(row=4,column =2)
Credits= Label(root,text="Credits : \nProject By:- Utkarsh Goel\nGmail: utkarsh.sky99@gmail.com\n Rating and data scraped from : www.IMDb.com" ,font=("Times New Roman", 14))
Credits.grid(columnspan=4)

root.mainloop()
