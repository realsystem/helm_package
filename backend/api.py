import logging
from flask import jsonify, request, Blueprint
from backend import aws


DEFAULT_TIMEOUT = 60
BUCKET_NAME = 'rs-uploader-bucket'

bp = Blueprint('storage', __name__, url_prefix='/')
my_site = aws.MyTerra('us-east-2')


@bp.route('/health', methods=['GET'])
def health():
    return jsonify({})


@bp.route('/', methods=['GET', 'POST', 'PUT'])
def index():
    if request.method == 'POST':
        logging.debug('object_name:', request.form['object_name'])
        response = my_site.create_upload_url(BUCKET_NAME, request.form['object_name'])
        logging.debug('response:', response)
        response = jsonify(
            {
                'url': response['url'],
                'fields': response['fields'],
            }
        )
        return response

    if request.method == 'PUT':
        logging.debug('object_name:', request.form['object_name'])
        flag = request.form['flag']
        logging.debug('flag:', flag)
        if flag == 'status':
            status = my_site.check_status(BUCKET_NAME, request.form['object_name'])
            logging.debug('status:', status)
            if status == 'uploaded':
                response = jsonify({'status': status})
            else:
                response = jsonify({'error': status}), 501
        else:
            response = jsonify({'error': 'flag is not supported'}), 501
        return response

    if request.method == 'GET':
        object_name = request.form['object_name']
        logging.debug('object_name:', object_name)
        if 'timeout' in request.form:
            timeout = request.form['timeout']
        else:
            timeout = DEFAULT_TIMEOUT
        logging.debug('timeout:', timeout)
        url = my_site.create_download_url(
            BUCKET_NAME, object_name, expiration=timeout
        )
        logging.debug('url:', url)
        response = jsonify({'url': url})
        return response
