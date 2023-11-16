# connection_between_2_notebooks
## Way to connect 2 notebooks in Google Colab using ngrok and flask. 
### I was sending some .txt file from 2.ipynb to 1.ipynb. Upload method in upload.py

 How to do it point by point

1. Need to install ngrok and flask using:
  
 ```!pip install pyngrok```

 ```!pip install flask```
 
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

/upload.py - path to our app

7. Launch it

```
!flask run --port 8888
```

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

