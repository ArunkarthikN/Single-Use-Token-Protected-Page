from flask import Flask, render_template, url_for
import uuid

app = Flask(__name__)

# Dictionary to store tokens and their validity
tokens = {}

# Generate a unique token and add it to the tokens dictionary
def generate_token():
    token = str(uuid.uuid4())
    tokens[token] = True
    return token

# Route to generate the link with the token
@app.route('/generate_link')
def generate_link():
    token = generate_token()
    link = url_for('protected_page', token=token, _external=True)
    return f"Share this link: {link}"

# Route for the protected page
@app.route('/protected_page/<token>')
def protected_page(token):
    if token in tokens and tokens[token]:
        tokens[token] = False  # Invalidate the token after use
        return render_template('protected.html')
    else:
        return render_template('invalid.html')

if __name__ == '__main__':
    app.run(debug=True)
