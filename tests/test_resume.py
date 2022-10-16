from base.resume_p import ResumeParser
def test_first_case():
    obj = ResumeParser('C:\\Users\\AVITA\\Desktop\\naresh07\\naresh.docx')
    data = obj.get_data()
    mobile = data["mobile"]
    email = data["email"]
    education = data["education"]
    name = data["Name"]
    skills = data["skills"]
    assert mobile == "8297783525"
    assert email == "gantenapatinaresh@gmail.com"
    assert education == "B-Tech"
    assert name == ''
    assert skills == ["python", "sql"]
