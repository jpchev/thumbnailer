from flask import Flask, request, send_from_directory
from thumbnailerapp.services.main import thumbnail
from werkzeug.utils import secure_filename
from thumbnailerapp.services.tasks import thumbnail_task
import os
import uuid

webapp = Flask(__name__)
webapp.config.from_pyfile(os.path.join('..', 'config.py'))

@webapp.route('/thumbnail', methods=["POST"])
def thumbnail_route():
    if 'file' not in request.files:
        return "No file part", 400
    
    params = request.form.to_dict()
    width = params['width']
    height = params['height']
    
    file = request.files['file']
    filename = secure_filename(file.filename)
    
    # save file with a uuid
    id = str(uuid.uuid1())
    uploaded_filename = os.path.join(webapp.config['UPLOAD_FOLDER'], id)
    file.save(uploaded_filename)
    
    thumbnail_filename = id + '.' + 'jpeg'
    thumbnail_full_filename = os.path.join(webapp.config['UPLOAD_FOLDER'], thumbnail_filename)

    # calling async task
    task = thumbnail_task.s(uploaded_filename, thumbnail_full_filename, width, height)
    task.delay()
    return "ok"
    
    # sync call to thumbnail, no task involved
    #thumbnail(uploaded_filename, thumbnail_full_filename, width, height)
    #try:
    #    # send file to client
    #    return send_from_directory(
    #        UPLOAD_FOLDER,
    #        thumbnail_filename)
    #finally:
    #    os.remove(uploaded_filename)
    #    os.remove(thumbnail_full_filename)

if __name__ == "__main__":
    app.run()