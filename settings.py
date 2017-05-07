
global gdSettings

gdSettings = {
    'sTasksDir': 'tasks',
    'sTemplatesDir': 'templates',
    'sAssetsDir': 'assets',
    'sTemporaryDir': 'temporary',
    'dTemplates': {
        "index": "index.html",
        "error": "error.html",
        "*": "error.html"
    },
    'dControlers': {
        "/": "index.py",
        "test.html": "test.py",
        "*": "error.py"
    },
    'dRouter': {
        "/index.html": "/"
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