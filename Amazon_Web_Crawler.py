# -*- coding: utf-8 -*-
import requests
import csv
from bs4 import BeautifulSoup
num=1
list_column_name  = [ 'Phone_Name','Date','Rating_Out_of_5', 'Review_Title', 'Review_Text']
with open ('E:\Rise Spring 2017\Advance Business Intelligence\Project\Amazon_Phone_Reviews.csv','a',newline='',encoding='utf-8') as fp:
        a = csv.writer(fp, delimiter=',')
      
        while(num<65):   #Number of Amazon Pages that have reviews
            if (num==0):
                num = num + 1
            else:
                url = 'https://www.amazon.com/Samsung-Galaxy-S7-Smartphone-International/product-reviews/B01CJSF8IO/ref=cm_cr_arp_d_show_all?ie=UTF8&reviewerType=all_reviews&pageNumber='+str(num)
                r = requests.get(url)
                soup = BeautifulSoup(r.content)
                reviews_text = []
                review_text_counter = 0
                for tag in soup.findAll('span',{"class":"a-size-base review-text"}):
                    reviews_text.append(tag.get_text())
                    review_text_counter = review_text_counter + 1
                print(review_text_counter)
                print(reviews_text)
                if (review_text_counter == 0):
                    continue
                reviews_date = []
                review_date_counter = 0
                for tag in soup.findAll('div',{"class":"a-section a-spacing-none reviews-content a-size-base"}):
                    for t in soup.findAll('span',{"class":"a-size-base a-color-secondary review-date"}):
                        x = t.get_text()
                        y = x[3:]
                        review_date_counter = review_date_counter + 1
                        if (review_date_counter == 1 or review_date_counter ==2):
                            pass
                        else:
                            reviews_date.append(y)
                print(reviews_date)
                print(review_date_counter)
        
                review_rating_counter = 0
                reviews_rating= []    
                for tag in soup.findAll('i',{"data-hook": "review-star-rating"}):
                    for t in tag.findAll('span',{"class":"a-icon-alt"}):
                        rating = tag.get_text()
                        reviews_rating.append(rating[0:3])
                        review_rating_counter = review_rating_counter + 1
                print(review_rating_counter)
                print(reviews_rating)
    
   
                review_titile_counter = 0
                review_title= []    
                for tag in soup.findAll('a',{"data-hook": "review-title"}):
                    review_title.append(tag.get_text())
                    review_titile_counter = review_titile_counter + 1
                print(review_title)
                print(review_titile_counter)
                
                phone_name_counter = 0
                phone_name=[]
                phone_nm = 'Samsung Galaxy S7 G930F'
                for tag in soup.findAll('a',{"data-hook": "review-title"}):
                    phone_name.append(phone_nm)
                    phone_name_counter = phone_name_counter + 1
                print(phone_name)
        
                rows = zip(phone_name,reviews_date,reviews_rating,review_title,reviews_text)
                for row in rows:
                    a.writerow(row)
                num = num + 1
    
    
