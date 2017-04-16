from everything import *
import pprint

@app.route("/", methods=["GET"])
def home():
  return render_template("home.html")


@app.route("/api/post", methods=["POST"])
def get_message():
  data = request.data
  data = json.loads(data)
  #balance_msg = bankInstance.getBalance(cfg['bank']['bank_id'], cfg['bank']['account'])
  most_recent_msg = bankInstance.getMostRecentTransaction(cfg['bank']['bank_id'], cfg['bank']['account'])
  return most_recent_msg


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
