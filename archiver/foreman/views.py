from flask import request, jsonify, Blueprint

from archiver.backend import store
from archiver.datatypes import Container
from archiver.exceptions import ValidationError

from utils import push_task


rest = Blueprint('archiver', __name__)


@rest.route('/', methods=['POST', 'PUT'])
def begin_register():
    json = request.get_json(force=True)
    if json:
        container = Container.from_json(json)
        # Container should always be defined otherwise a
        # validation error will be raised by from_json
        if container:
            return push_task(container)
    raise ValidationError('no data')


@rest.route('/', methods=['GET'])
def list_projects():

    return jsonify({'projects': store.list_containers()})


@rest.route('/callback', methods=['POST', 'PUT'])
def callback():
    json = request.get_json(force=True)
    if json:
        print json
        return ''
    print "No data in callback"
    raise ValidationError('no data')


@rest.route('/<string(maxlength=60):cid>')
def get_metadata_route(cid):
    service = request.args.get('service')
    if service:
        return store.get_container_service(cid, service)
    return store.get_container(cid)


@rest.route('/<string(length=64):fid>')
def get_file_route(fid):
    #TODO Move constants to settings
    try:
        request.args['metadata']
        return store.get_file('File Metadata/{}.json'.format(fid))
    except KeyError:
        return store.get_file('Files/{}'.format(fid))
