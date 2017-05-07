
global gdSettings

gdSettings = {
    'sTasksDir': 'tasks',
    'sTemplatesDir': ,
    'assets': ,
    'dTemplates': {
        "index": "index.html",
        "error": "error.html",
        "*": "error.html",
    },
    'dControlers': {
        "/": "index.py",
        "test.html": "test.py",
        "*": "error.py",
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