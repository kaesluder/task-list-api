import app
from flask_cors import CORS

app = app.create_app()


CORS(app)
app.run()
