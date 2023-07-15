from flask_cors import CORS
import connexion

config = {
    ## Code to get config from a property store
    ## This config cannot come from commandline
}

app = connexion.App(__name__, specification_dir="./")
app.add_api("swagger.yml")
CORS(app.app)