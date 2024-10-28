from flask import Flask
from flask import session, request, url_for, render_template

app = Flask("Flask recap app")


@app.route("/", methods=["GET", "POST"]) # can also do @app.get or @app.post
def root():
    if request.method == "GET":
        return "Hello World", 200
    else:
        return render_template("tempaltes/home.html", person="jean")

@app.route("/name/<name>/<int:user_id>")
def name(name, user_id):
    # there is also <path:subpath> it is like string but accept path
    return f"Your name is {name} and user_id is {user_id} and the path to query is {url_for("query_param", q='')}"

@app.route("/query")
def query_param():
    param = request.args.get("q")
    print(param)
    if param ==  None:
        return "Please provide arg", 400
    return f"param: {param}"


from werkzeug.utils import secure_filename #if you want to keep the fileanem from client to store on serv. pass it in here
from flask import make_response

@app.route("/data", methods=["POST"])
def data():
    username = request.form['username']
    password = request.form["password"]
    # this is html form data
    file = request.files["filename"] # can access .filename attribute on each request.files 
    file.save(f"/files/{secure_filename(file.filename)}")
    # this is to get a file from html request

    cookie = request.cookies.get("cookie_name")
    resp = make_response(render_template("home.html", person="cookie example"))
    resp.set_cookie("chocolat_chips", "best", max_age=60, ) # max age is seconds




if __name__ == "__main__":
    app.run(debug=True)