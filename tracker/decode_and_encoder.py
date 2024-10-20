import json
import base64

def encode_data(data):
    json_data = json.dumps(data)
    encoded = base64.b64encode(json_data.encode('utf-8')).decode('utf-8')
    return encoded
    
def decode_data(encoded):
    decoded_bytes = base64.b64decode(encoded)
    data = json.loads(decoded_bytes)
    return data