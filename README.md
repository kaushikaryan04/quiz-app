Gives 10 Random Questions that are stored in database fetched from api ( https://the-trivia-api.com/v2/questions ).  
Made a custom command to fetch question from api and store in database ( python manage.py modelscript )  
Authentication so only registered and logged in users can use app.  
After quiz is over a page shows incorrect and correct options with scores.    
  
## Steps to run  
```


pip install -r requirements.txt

python manage.py migrate

python manage.py modelscript ( if want to add more questions for api )

python manage.py runserver 


```
