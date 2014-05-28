from archiver.exceptions import ValidationError


def validate_project(data):
    try:
        if data['node']:
            return _validate_project(data['node'])
    except KeyError:
        pass
    raise ValidationError('missing node segment')


def _validate_project(node):
    try:
        if _validate_metadata(node['metadata']):
            for child in node['children']:
                if not _validate_project(child['node']):
                    raise ValidationError('bad child')
            for service in node['services']:
                if not _validate_service(service):
                    raise ValidationError('bad service')
            return True
    except (KeyError, TypeError):
        raise ValidationError('malformed data')
    raise ValidationError('improperly formatted data')


def _validate_metadata(data):
    try:
        valid = data is not None
        valid = valid and bool(data['id'])
        valid = valid and bool(data['title'])
        # description can be ''
        # valid = valid and data['description'] is not None
        valid = valid and bool(data['contributors'])
        return valid
    except KeyError:
        return False


#TODO
def _validate_service(data):
    return True
