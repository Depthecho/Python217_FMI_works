from flask import Flask, render_template, request
from dictionary import load_dictionary, save_dictionary

app = Flask(__name__)
dictionary = load_dictionary()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    english_word = request.form['english_word']
    russian_word = request.form['russian_word']
    transcription = request.form['transcription']
    dictionary[english_word] = {'russian': russian_word, 'transcription': transcription}
    save_dictionary(dictionary)
    message = f'Слово "{english_word}" добавлено в словарь и сохранено в файл'
    return render_template('index.html', message=message)

@app.route('/search', methods=['POST'])
def search():
    search_word = request.form['search_word']
    if search_word in dictionary:
        russian_word = dictionary[search_word]['russian']
        transcription = dictionary[search_word]['transcription']
        message = f'{search_word} - перевод на русский: {russian_word}, транскрипция: {transcription}'
    else:
        message = 'Слово не найдено в словаре'
    return render_template('index.html', message=message)

@app.route('/dictionary')
def dictionary_page():
    return render_template('dictionary.html', dictionary=dictionary)

if __name__ == '__main__':
    app.run()