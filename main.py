from flask import Flask, render_template, request
import os
import ai

app = Flask(__name__)


@app.route('/', methods=('GET', 'POST'))
@app.route('/index', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        if 'file1' in request.files:
            file = request.files['file1']
        if 'file2' in request.files:
            file = request.files['file2']
        if 'file3' in request.files:
            file = request.files['file3']
        if file:
            xfile = os.path.join('static', 'upl_' + file.name + '.jpg')
            print(xfile)
            file.save(xfile)
    return render_template('index.html', res1=brain.res1, res2=brain.res2, res3=brain.res3)

@app.route('/analyze_images/', methods=['POST'])
def analyze():
    print('analyze_images()')
    brain.analyze_uploaded_images()
    return render_template('index.html', res1=brain.res1, res2=brain.res2, res3=brain.res3)

@app.route('/aiabout/')
def aiabout():
    return render_template('ai.html')

@app.route('/web/')
def web():
    return render_template('web.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    brain = ai.MyAI()
    app.run(debug=True)
