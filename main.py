from flask import Flask, render_template

from app import server
import graphs

@server.route('/')
def home():
    return render_template('index.html')

@server.route('/genre_bar_redirect')
def genre_bar_redirect():
    return '', 302, {'Location': '/dash/genre-bar-graph/'}

@server.route('/classification_bar_redirect')
def class_bar_redirect():
    return '', 302, {'Location': '/dash/classification-bar-graph/'}

@server.route('/heatmap_redirect')
def heatmap_redirect():
    return '', 302, {'Location': '/dash/heatmap'}

if __name__ == '__main__':
    server.run(debug=True)
