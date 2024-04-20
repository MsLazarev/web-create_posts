from flask import Flask, request, render_template, redirect, url_for, session
from db_scripts import *
import os

categories_memory = [] #Память с последними нажатыми кнопками(категории для фильтров)

def make_database():
    main()

def main_page(post_list):
    global cnt
    
    #post_list[-1][-1].replace("\r\n", "<br>")
    #print(post_list[-1][-1])
    #print()
    return render_template('main.html', post_list=post_list, cnt=cnt)

def topic_page():
    post_list = []
    if 'all_topic' in request.form:
        categories_memory.append("Все_категории")
        post_list = filter_all()
    if 'crypto_topic' in request.form:
        categories_memory.append("Криптовалюта")
        post_list = filter_crypto()
    if 'sport_topic' in request.form:
        categories_memory.append("Спорт")
        post_list = filter_sport()
    if 'strimes_topic' in request.form:
        categories_memory.append("Стримеры")
        post_list = filter_streamers()
    if 'music_topic' in request.form:
        categories_memory.append("Музыка")
        post_list = filter_music()
    if 'cybersport_topic' in request.form:
        categories_memory.append("Киберспорт")
        post_list = filter_cybersport()
    if 'politic_topic' in request.form:
        categories_memory.append("Политика")
        post_list = filter_politic()
    return main_page(post_list)

cnt = 0
def index():
    global cnt
    if request.method == "GET":
        post_list = get_post()
        return main_page(post_list)
    
    if request.method == "POST":
        if 'create' in request.form:
            return redirect(url_for('create'))
        
        if 'topic' in request.form:
            if cnt == 0:
                cnt = 1
            else:
                cnt = 0

            # if categories_memory[-1] == 'Все_категории':
            #     post_list = filter_all()
            # elif categories_memory[-1] == 'Криптовалюта':
            #     post_list = filter_crypto()
            # elif categories_memory[-1] == 'Спорт':
            #     post_list = filter_sport()
            # elif categories_memory[-1] == 'Стримеры':
            #     post_list = filter_streamers()
            # elif categories_memory[-1] == 'Музыка':
            #     post_list = filter_music()
            # elif categories_memory[-1] == 'Политика':
            #     post_list = filter_politic()
            # elif categories_memory[-1] == 'Киберспорт':
            #     post_list = filter_cybersport()
            post_list = get_post()
            return main_page(post_list)

        
        if 'create' not in request.form and 'topic' not in request.form:
            return topic_page()
    



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