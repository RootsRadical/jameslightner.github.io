from flask import Flask
import hashlib

app = Flask(__name__)

def get_hash(input_string):
    # Compute SHA-256 hash of the input string
    sha256_hash = hashlib.sha256(input_string.encode()).hexdigest().upper()
    return sha256_hash

@app.route('/hash')
def my_hash():
    data = "Hello World Check Sum!!"
    hash_value = get_hash(data)
    return f"<p>data: {data}</p><p> Name of Cipher Used: SHA-256 Value: {hash_value}</p>"

if __name__ == '__main__':
    app.run(ssl_context='adhoc')  # Optional: enables SSL with a self-signed cert
