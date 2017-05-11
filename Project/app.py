from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        capshape = request.form['capshape']
        return render_template('capshape.html', capshape=capshape)
    return render_template('test_index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
