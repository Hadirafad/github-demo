@app.route("/", methods=['GET'])
def home():
    return "Welcome to Library Management Server"