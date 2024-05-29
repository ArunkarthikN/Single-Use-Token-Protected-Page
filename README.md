# Single-Use-Token-Protected-Page
This project is a simple Flask application that generates a unique, single-use token for accessing a protected page. The token becomes invalid after one use, ensuring the link cannot be reused or shared.

**Features**

* Generate a unique token for accessing a protected page.
* Invalidate the token after it has been used once.
* Serve different pages for valid and invalid tokens.

**Prerequisites**
* Python 3.x
* Flask

**Installation**

**1. Clone the repository:**

```sh
git clone https://github.com/ArunkarthikN/Single-Use-Token-Protected-Page.git
cd single-use-token-protected-page

```

**2. Create and activate a virtual environment:**

```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`


```

**For Linux:**

```sh
apt install python3.12-venv
python3 -m venv /path/to/venv
source /path/to/venv/bin/activate
```

**3. Install the required packages:**

```sh
pip install Flask
```

# Project Structure

single-use-token-protected-page/
│
├── app.py
└── templates/
├── protected.html
└── invalid.html


