from assets.controller import * 



def check_file_extension (path) : 
    response = requests.get(path)
    content_type = response.headers['content-type']
    extension = mimetypes.guess_extension(content_type)
    return extension