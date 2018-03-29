from flask import Flask, make_response, render_template, request, redirect, url_for
from pathlib import Path
from os.path import join
from map import Map
import json
from settings import MAIN_PATH
from Settings.default_settings import clear_all_olds

app = Flask(__name__)


@app.route('/')
def hello_world():
    clear_all_olds('Seoul_districts.svg')
    return redirect('/map')

@app.route('/map')
def templated_svg():
    new_map = Path(join(MAIN_PATH, "templates", "new_Seoul_districts.svg"))
    width = request.args.get('width', '800')
    height = request.args.get('height', '600')
    if (new_map.exists()):
        svg = render_template('new_Seoul_districts.svg', width=width, height=height)
    else:
        svg = render_template('Seoul_districts.svg', width=width, height=height)
    response = make_response(svg)
    response.content_type = 'image/svg+xml'
    return response

@app.route('/map/change', methods=['POST'])
def new_map():
    map = Map(join(MAIN_PATH, 'templates', 'Seoul_districts.svg'))
    if request.method == 'POST':
        req_dict = json.loads(request.data)
        print(req_dict)
        map.change_color(req_dict)
        return redirect('/map')


if __name__ == '__main__':
    app.run()
