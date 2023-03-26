from flask import Flask, render_template, request, send_file, Response
from PIL import Image
import io
from io import BytesIO


app = Flask(__name__)

# frontend

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/jpgtopng")
def jpgtopng():
    return render_template("jpgtopng.html")

@app.route("/pngtojpg")
def pngtojpg():
    return render_template("pngtojpg.html")

@app.route("/webptopng")
def webptopng():
    return render_template("webptopng.html")

@app.route("/bmptopng")
def bmptopng():
    return render_template("bmptopng.html")

@app.route("/pngtopdf")
def pngtopdf():
    return render_template("pngtopdf.html")


##### APIs. CONVERSIONS. BACKEND

@app.route('/api/jpgtopng', methods=['POST'])
def jpg_to_png():
        image_file = request.files['image']
        image = Image.open(image_file)
        image = image.convert('RGBA')
        file_bytes = io.BytesIO()
        image.save(file_bytes, format='PNG')
        file_bytes.seek(0)
        return send_file(file_bytes, attachment_filename='converted.PNG', as_attachment=True)
        

@app.route('/api/pngtojpg', methods=['POST'])
def png_to_jpg():
        image_file = request.files['image']
        image = Image.open(image_file)
        image = image.convert('RGB')
        file_bytes = io.BytesIO()
        image.save(file_bytes, format='JPEG')
        file_bytes.seek(0)
        return send_file(file_bytes, attachment_filename='converted.jpg', as_attachment=True)


@app.route('/api/webptopng', methods=['POST'])
def webp_to_png():
    image = request.files["image"]
    img = Image.open(image)
    byte_io = io.BytesIO()
    img.save(byte_io,'PNG')
    byte_io.seek(0)
    response = Response(byte_io,content_type='image/png')
    response.headers.set("Content-Disposition","attachment", filename='converted.png')
    return response

@app.route('/api/bmptopng', methods=['POST'])
def bmp_to_png():
    image = request.files["image"]
    img = Image.open(image)
    byte_io = io.BytesIO()
    img.save(byte_io,'PNG')
    byte_io.seek(0)
    response = Response(byte_io,content_type='image/png')
    response.headers.set("Content-Disposition","attachment", filename='converted.png')
    return response

@app.route('/api/pngtopdf', methods=['POST'])
def png_to_pdf():
    image = request.files["image"]
    img = Image.open(image)
    byte_io = io.BytesIO()
    img.save(byte_io,'PDF')
    byte_io.seek(0)
    response = Response(byte_io,content_type='application/pdf')
    response.headers.set("Content-Disposition","attachment", filename='converted.pdf')
    return response



if __name__ == "__main__":
    app.run(debug=True)
