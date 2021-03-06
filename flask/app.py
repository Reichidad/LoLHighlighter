from flask import Flask, render_template, request, url_for, jsonify
from run_extraction import run_extraction
import datetime

# config
DEBUG = True

# instantiate the app
app = Flask(__name__, static_url_path='/static')
app.config.from_object(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/highlight')
def highlight(youtube_url=None):
    if request.method == 'POST':
        pass

    elif request.method == 'GET':
        url = request.args.get('youtube_url')
        url = str(url)

        try:
            cat_offsets, cat_dict = run_extraction(url)
        except Exception as ex:
            print(ex)

        return render_template('index.html', youtube_url=url, offsets=cat_offsets, category=cat_dict)


@app.route('/about')
def about():
    return render_template('about.html')


@app.template_filter('time_format')
def time_format(t):
    if t is None:
        return ''

    return str(datetime.timedelta(seconds=t))


app.jinja_env.filters['time_format'] = time_format

if __name__ == '__main__':
    app.run()
