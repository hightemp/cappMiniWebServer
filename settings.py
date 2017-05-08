
global gdSettings

gdSettings = {
    'sTasksDir': 'tasks',
    'sTemplatesDir': 'templates',
    'sAssetsDir': 'assets',
    'sTemporaryDir': 'temporary',

    'dRoutes': {
        "/": {
            'sTemplate': 'index.html',
            'sControler': 'index.py'
        },
        "*": {
            'sRedirect': '/'
        }
    },

    'aDefaultHeaders': [
        ('Content-Type', 'text/html')
    ],
    'aAccessDirectories': [
        'templates',
        'assets',
        'temporary'
    ],
    'dTemplateVariables': {
        'sTitle': 'test'
    }
}