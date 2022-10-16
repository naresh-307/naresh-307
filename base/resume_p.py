from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
import docx2txt
import re
from database.dbfile import conn
from ex_handle import handle_error
class ResumeParser:
    def __init__(self, filename):
        self.doc = docx2txt.process(filename)
        self.education = {'B.tech'}
        self.skills = {'python', 'sql'}
        self.cur = conn.cursor()

    def get_data(self):
        try:
            mobile = re.search(r'\d{10}', self.doc)
            gmail = re.search(r'\S+@\S+', self.doc)
            education = re.search(r'%s' % '|'.join(self.education), self.doc, re.IGNORECASE)
            skills = re.findall(r'%s' % '|'.join(self.skills), self.doc, re.IGNORECASE)
            name = ''

            nltk_results = ne_chunk(pos_tag(word_tokenize(self.doc)))
            # print('%%%%%%%%%%%%%%')
            # print(nltk_results)
            for nltk_result in nltk_results:
                if (nltk_result) == Tree:

                    for nltk_result_leaf in nltk_result.leaves():
                        name += nltk_result_leaf [0]+ ''

            # print('Type:', nltk_result, 'Name:', name)


            print({'mobile': mobile.group(), 'gmail': gmail.group(), 'education': education.group(),
                  'skills': set(skills), 'Name': name})
            values = (name, mobile.group(), gmail.group(), education.group(), ','.join(skills))

            print("insert into  reduce values('%s','%s','%s','%s','%s')"%(values))

            insert_query = "insert into  reduce values(%s,%s,%s,%s,%s)"
            self.cur.execute(insert_query, values)
            print('Data inserted successfully.....')
            conn. commit()
            return {'mobile': mobile.group(), 'email': gmail.group(), 'education': education.group(), 'skills' : skills, 'Name': name}

        except Exception as e:
            return e
