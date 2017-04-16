from everything import *
import pprint

@app.route("/", methods=["GET"])
def home():
  return render_template("home.html")


@app.route("/api/post", methods=["POST"])
def get_message():
  data = request.data
  data = json.loads(data)
  return data['message']


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS