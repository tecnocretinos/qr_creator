# app.py

from flask import Flask, request, render_template, request
from os import listdir
import qrcode, os, logging, uuid
from os.path import isfile, join

app = Flask(__name__, template_folder='views', static_url_path='/static')

@app.route("/")
def home():
    mypath = "static"
    onlyfiles = [os.remove(join(mypath, f)) for f in listdir(mypath) if isfile(join(mypath, f))]
    return render_template('index.html')

@app.route("/createqr", methods=["POST"])
def create_qr_code():
    try:
        content = request.form['text']
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(content)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        uuid_id = str(uuid.uuid1())
        img_name = f"./static/{uuid_id}.png"
        img.save(img_name)
        return render_template("show_image.html", qr_code = img_name)
        

    except Exception as err:
        logging.exception("Exception creating qr code")
        return "error while creating qr"