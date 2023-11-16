# connection_between_2_notebooks
## Way to connect 2 notebooks in Google Colab using ngrok and flask. 
### I was sending some .txt file from 2.ipynb to 1.ipynb. Upload method in upload.py

 How to do it point by point

1. Need to install ngrok and flask using:
  
 ```!pip install pyngrok```

Screenshot of successful result:

 ![Screenshot of successful result](https://github.com/ceba11/connection_between_2_notebooks/assets/107613374/d8be2d65-6b98-4b0c-a02c-4beea9643aad)

 ```!pip install flask```

 Screenshot of successful result:

![Screenshot of successful result](https://github.com/ceba11/connection_between_2_notebooks/assets/107613374/6a38cea1-93ca-4e4d-a13c-a3119f17c013)


2. Need to connect to your ngork account

```
from pyngrok import ngrok

ngrok.set_auth_token("Your auth token from ngrok")


```

 Can do it from here:

 https://dashboard.ngrok.com/get-started/your-authtoken

4. Creating public url with port, result should show you your link.

```
from pyngrok import ngrok

public_url = ngrok.connect(8888)
print(public_url)
```

 Screenshot of successful result:

![image](https://github.com/ceba11/connection_between_2_notebooks/assets/107613374/af082ae7-2748-44b2-bda3-319869002d17)


Result should look like: https://2b57-45-67-21-5.ngrok-free.app

Copy it!

5. Need to create our flask app somewhere on disk space

```
from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    filename = file.filename  # Получение имени файла

    save_path = f'/filefromsecond/{filename}'  
    file.save(save_path)

    return 'Файл загружен успешно', 200

if __name__ == "__main__":
    app.run(debug=True)
```

In save_path we enter path,where our file should be saved with {filename} on the end.

6. Launch our flask app for future server

```
%env FLASK_APP=/upload.py
```
Screenshot of successful result:

![image](https://github.com/ceba11/connection_between_2_notebooks/assets/107613374/d511d14f-3b78-4f9e-83f3-c1a6d5df8aa3)

/upload.py - path to our app

7. Launch it

```
!flask run --port 8888
```

Screenshot of successful result:
![image](https://github.com/ceba11/connection_between_2_notebooks/assets/107613374/5788c76e-82fb-447b-8ae6-2e57a09449e5)


8.Create second notebook and paste this code

```
import requests

url = 'https://1a57-34-91-72-5.ngrok-free.app/upload'  # URL от ngrok
files = {'file': open('/content/random.txt', 'rb')}

r = requests.post(url, files=files)
print(r.text)
```

After public link from ngork (https://1a57-34-91-72-5.ngrok-free.app/) need to past our method name (it is 'upload' here)

In files we should paste a path to file you want to upload

Screenshots of successful result:

![image](https://github.com/ceba11/connection_between_2_notebooks/assets/107613374/362d54f2-3c6e-41b4-a25d-5b56e3283529)

![image](https://github.com/ceba11/connection_between_2_notebooks/assets/107613374/a16e2412-9713-42cd-9b6d-ed5963da3fca)

