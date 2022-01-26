from flask import Flask, render_template , request, redirect , url_for
app = Flask(__name__)

@app.route('/')
def api_root():
    return render_template('index.html')

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route("/test", methods=["POST"])
def test():
    user = request.form['fname']
    return redirect(url_for('success',name = user))


if __name__ == '__main__':
    app.run(debug = True)