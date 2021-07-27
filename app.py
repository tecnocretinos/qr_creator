# app.py

from flask import Flask, request, render_template, request, send_from_directory
from os import listdir
import qrcode, os, logging, uuid
from os.path import isfile, join

app = Flask(__name__,
            template_folder='views', 
            static_folder=os.path.abspath('./tmp/images/') #. removed
    )
            # static_url_path='/tmp/images/', 

@app.route("/")
@app.route("/dev")
def home():
    try:
        #TODO: delete only my images generated not all in the folder
        # mypath = "/tmp/images"
        # os.mkdir(mypath)
        # onlyfiles = [os.remove(join(mypath, f)) for f in listdir(mypath) if isfile(join(mypath, f))]
        #TODO: add css to index.html
        return render_template('index.html')
    except FileExistsError:
        # onlyfiles = [os.remove(join(mypath, f)) for f in listdir(mypath) if isfile(join(mypath, f))]
        return render_template('index.html')
    except Exception as err:
        logging.exception("Error accessing index.html page")

@app.route("/createqr", methods=["GET","POST"])
@app.route("/dev/createqr", methods=["GET","POST"])
def create_qr_code():
    try:
        #TODO: Limit the text input size
        # content = request.form['text']
        # qr = qrcode.QRCode(
        #     version=1,
        #     error_correction=qrcode.constants.ERROR_CORRECT_L,
        #     box_size=10,
        #     border=4,
        # )
        # qr.add_data(content)
        # qr.make(fit=True)

        # img = qr.make_image(fill_color="black", back_color="white")
        # uuid_id = str(uuid.uuid1())
        logging.exception(os.listdir())
        logging.warning("testing warning logging")
        logging.exception(os.listdir("./tmp/images"))
        uuid_id = '7d7c11a6-ee7c-11eb-a6a2-38f9d341619d'
        img_name = f"https://kb6y3koqql.execute-api.us-east-1.amazonaws.com/dev/tmp/images/?filename={uuid_id}.png" #. removed
        # img.save(img_name)
        return render_template("show_image.html", qr_code = img_name)

    except Exception as err:
        logging.exception("Exception creating qr code")
        return "error while creating qr"


@app.route("/tmp/images/")
@app.route("/dev/tmp/images/")
def testing_send_file_from_directory():
    filename = request.args.get("filename")
    logging.exception(filename)
    return send_from_directory("./tmp/images/",
                                filename,
                                mimetype="image/png",
                                )