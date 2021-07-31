from flask import Flask, send_from_directory, render_template
import HTMLMut

app = Flask(__name__)
mut = HTMLMut.HtmlBuilder()

# ROUTING CODE

@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

@app.route('/ui')
def uiIndex():
    return send_from_directory('./ui','index.html')

@app.route('/ui/<path:path>')
def uiStatic(path):
    return send_from_directory('./ui',path)

@app.route('/api/html')
def apiHTML():
    return {'html':mut.generate()}

# END OF ROUTING CODE


if __name__ == '__main__':
    app.run(port=3333)
