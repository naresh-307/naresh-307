import logging

logging.basicConfig(filename='logger/app.log', filemode='w', format='%(level name)s:%(name)s: % %(message)s')
logger = logging.getLogger('Resume-Logger')
