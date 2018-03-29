from flask import Flask, make_response, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/hello')
def templated_svg():
    width = request.args.get('width', '800')
    height = request.args.get('height', '600')
    svg = render_template('Seoul_districts.svg', width=width, height=height)
    response = make_response(svg)
    response.content_type = 'image/svg+xml'
    return response


if __name__ == '__main__':
    app.run()
