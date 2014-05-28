empty = {}

bad_structure = {
    'metadata': {
        'id': '12345',
        'title': 'example project',
        'description': '',
        'contributors': [
            'john smith'
        ]
    },
    'services': [
        {
            'github': {
                'access_token': 'some secret key',
                'repo': 'archiver',
                'user': 'chrisseto'
            }
        }
    ],
    'children': []
}

bad_children = {}

bad_service = {
    'node':
    {
        'metadata': {
            'id': '12345',
            'title': 'example project',
            'description': '',
            'contributors': [
                'john smith'
            ]
        },
        'services': [
            {
                'github': {
                    'user': 'chrisseto'
                }
            }
        ],
        'children': []
    }
}

unimplemented_service = {

}

good = {
    'node':
    {
        'metadata': {
            'id': '12345',
            'title': 'example project',
            'description': '',
            'contributors': [
                'john smith'
            ]
        },
        'services': [
            {
                'github': {
                    'access_token': 'some secret key',
                    'repo': 'archiver',
                    'user': 'chrisseto'
                }
            }
        ],
        'children': []
    }
}


good_with_children = {
    'node':
    {
        'metadata': {
            'id': '12345',
            'title': 'example project',
            'description': '',
            'contributors': [
                'john smith'
            ]
        },
        'services': [
            {
                'github': {
                    'access_token': 'some secret key',
                    'repo': 'archiver',
                    'user': 'chrisseto'
                }
            }
        ],
        'children': [
            {
                'node': {
                    'metadata': {
                        'id': '12345',
                        'title': 'example project',
                        'description': '',
                        'contributors': [
                            'john smith'
                        ]
                    },
                    'services': [
                        {
                            'github': {
                                'access_token': 'some secret key',
                                'repo': 'archiver',
                                'user': 'chrisseto'
                            }
                        }
                    ],
                    'children': []
                }
            }
        ]
    }
}


good_multi_service = {
    'node':
    {
        'metadata': {
            'id': '12345',
            'title': 'example project',
            'description': '',
            'contributors': [
                'john smith'
            ]
        },
        'services': [
            {
                'github': {
                    'access_token': 'some secret key',
                    'repo': 'archiver',
                    'user': 'chrisseto'
                },
            },
            {
                's3': {
                    'access_key': 'Some key',
                    'secret_key': 'Another Key',
                    'bucket': 'a bucket name'
                }
            }
        ],
        'children': []
    }
}
