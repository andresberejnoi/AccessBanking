from everything import *
import pprint

@app.route("/", methods=["GET"])
def home():
  return render_template("home.html")


@app.route("/api/post", methods=["POST"])
def get_message():
  data = request.data
  data = json.loads(data)
  print data['message']
  ai_data_response = aiInstance.sendQuery(data['message'])
  if ai_data_response['status']['code'] == 200:
      response = aiInstance.methodChoice(ai_data_response)
  else:
      print "Failed to complete query request with error: {0}"\
            .format(ai_data_response['status']['errorType'])
  print response
  return response


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
