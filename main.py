from flask import Flask, request, render_template, redirect, url_for, session
from db_scripts import *
import os

def make_database():
    main()

def main_page():
    global cnt
    post_list = get_post()
    
    #post_list[-1][-1].replace("\r\n", "<br>")
    #print(post_list[-1][-1])
    #print()
    return render_template('main.html', post_list=post_list, cnt=cnt)
cnt = 0
def index():
    global cnt
    if request.method == "GET":
        return main_page()
    
    if request.method == "POST":
        if 'create' in request.form:
            return redirect(url_for('create'))
        if 'topic' in request.form:
            if cnt == 0:
                cnt = 1
            else:
                cnt = 0
            return main_page()
    

def create_page():
    topic_list = [(1, "Криптовалюта"), (2, "Спорт"), (3, "Стримеры"), (4, "Музыка"), (5, "Киберспорт"), (6, "Политика")]
    return render_template('create.html', topic_list = topic_list)

def create():
    if request.method == 'POST':
        head_post = request.form.get('headshot')
        describe_post = request.form.get('describeshot')
        topic_post = request.form.get('topicshot')
        put_post(head_post, describe_post, topic_post)
        post_list = get_post()
        print(post_list)
        return redirect(url_for('index'))

    return create_page()


folder = os.getcwd()
app = Flask(__name__, static_folder="folder", template_folder=folder)
app.json.ensure_ascii = False

app.add_url_rule('/', 'index', index, methods = ['POST', 'GET'])
app.add_url_rule('/create', 'create', create, methods = ['POST', 'GET'])

if __name__ == '__main__':
    make_database()
    app.run()