# app.py

from flask import Flask, request
import qrcode
import logging, uuid

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
    return "Hola cretino!!"


@app.route("/createqr", methods=["POST"])
def create_qr_code():
    try:
        content = request.json
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(content["text"])
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        uuid_id = str(uuid.uuid1())
        img.save(f"{uuid_id}.png")
        return uuid_id
    except Exception as err:
        logging.exception("Exception creating qr code")
        return "error while creating qr"