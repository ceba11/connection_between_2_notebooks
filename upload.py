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
