import base64

def get_base64_string(path):
    try:
        with open(path,"rb") as img:
            return base64.b64encode(img.read()).decode('utf-8')
    except Exception as e:
        raise Exception('Image unable to detect')