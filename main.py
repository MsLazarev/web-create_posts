from flask import Flask, request, render_template, redirect, url_for, session
from db_scripts import *
import os

def make_database():
    main()

def main_page():
    post_list = get_post()
    
    post_list[-1][-1].replace("\r\n", "<br>")
    print(post_list[-1][-1])
    #print()
    return render_template('main.html', post_list=post_list)

def index():
    if request.method == "GET":
        return main_page()
    
    if request.method == "POST":
        return redirect(url_for('create'))
    

def create_page():
    return render_template('create.html')

def create():
    if request.method == 'POST':
        head_post = request.form.get('headshot')
        describe_post = request.form.get('describeshot')
        put_post(head_post, describe_post)
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