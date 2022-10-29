from re import L
from assets.controller import * 



def check_file_extension (path) : 
    response = requests.get(path)
    content_type = response.headers['content-type']
    extension = mimetypes.guess_extension(content_type)
    return extension

def iterate_over_a_the_first_case_of_a_double_list(_list) :
    _return = ""
    for l in _list: 
        if l[0] == "/hello" : 
            break
        _return += ""+l[0]+"\n"
    return _return
    