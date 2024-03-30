from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        search_query = request.form['search']
        return redirect(url_for('search_results', search=search_query))
    return render_template('index.html')

@app.route('/search_results')
def search_results():
    search_query = request.args.get('search')
    return render_template('search_results.html', search_query=search_query)

if __name__ == '__main__':
    app.run(debug=True)
