import base64


def get_base64_string(path):
    with open(path,"rb") as img:
        return base64.b64encode(img.read()).decode('utf-8')