from base.resume_p import ResumeParser
from exception import error_handler
import os
cwd = os.getcwd()
# @error_handler
def data(filename):
    parser = ResumeParser(filename)

    return parser.get_data()

if __name__ == '__main__':
    print(data('C:\\Users\\AVITA\\Desktop\\naresh07\\naresh.docx'))


