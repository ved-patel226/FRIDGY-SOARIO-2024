import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

from flask import Flask, redirect, url_for, render_template, request, session, abort
from flask_dance.contrib.github import make_github_blueprint, github
from werkzeug.utils import secure_filename
from flask_wtf.csrf import CSRFProtect, validate_csrf
import requests
from datetime import datetime

from py_tools.week_refresh import *
from py_tools.calander import *
from py_tools.json_editor import *
from py_tools.env_translator import env_to_var
from py_tools.wtforms_upload import *
from py_tools.ai import *
from py_tools.weather import *
from py_tools.calander import *

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/Fridge-IMGS/'
app.config['CONFIG_KEY'] = env_to_var("CONFIG_KEY")
app.config['SESSION_COOKIE_SECURE'] = False
app.secret_key = env_to_var("APP_SECRET")
csrfp = CSRFProtect(app)
csrfp.init_app(app)

github_blueprint = make_github_blueprint(client_id=env_to_var("GITHUB_CLIENT_ID"),
                                         client_secret=env_to_var("GITHUB_CLIENT_SECRET"))

app.register_blueprint(github_blueprint, url_prefix="/login")


def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]

def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name")
    }
    return location_data

def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

def find_y_for_x(x_target, x1, y1, x2, y2):
    slope = calculate_slope(x1, y1, x2, y2)

    y = slope * (x_target - x1) + y1
    
    return y



@app.route('/', methods=["GET", "POST"])
def index():
    if not github.authorized:
        return render_template("index.html")
    
    if request.method == "POST":
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        if file:
            file.filename = f"{datetime.now().strftime("%d_%m_%Y")}.jpg"
            cprint(f"{app.config['UPLOAD_FOLDER']}", "yellow", attrs=["bold"])
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            file.save(filepath)
            
            gai_vision(os.environ.get("USER"))
            
            return redirect(url_for("index"))

    
    resp = github.get("user")
    if resp.ok:
        user_info = resp.json()
        email = user_info.get("email")
        user = user_info.get("login")
        
        os.environ["USER"] = user
        os.environ["EMAIL"] = email
        
        sunday_check(os.environ.get("USER"))
        
        app.config['UPLOAD_FOLDER'] = f'static/Fridge-IMGS/{os.environ["USER"]}/'
        
        labels, values = dict_to_list(user)
        foods = all_foods(os.environ["USER"])
        city = get_location()
        lat_long_tuple = get_lat_long(city["city"])
        perfect_day = perfect_errand_day(lat_long_tuple[0], lat_long_tuple[1])
        
        recent_file = get_most_recent_file(app.config['UPLOAD_FOLDER'])
        
        if recent_file == None:
            show_upload = True
        else:
            recent_files = recent_file.split("/")[-1].strip(".jpg")        
            
            if str(datetime.strptime(recent_files, "%d_%m_%Y").date()) == str(datetime.now().strftime("%Y-%m-%d")):
                show_upload = False
            else:
                show_upload = True


        try:
            
            if values[0] == values[-1]:
                back_to_back_predict = None
            
            back_to_back_predict = find_y_for_x(30, values[0], values.index(values[0]), values[-1], values.index(values[-1]))
        except:
            back_to_back_predict = 0
        
        values = list(reversed(values))
        
        if back_to_back_predict == None:
            pass
        elif back_to_back_predict - len(values) <= 0:
            back_to_back_predict = 0
        else:
            back_to_back_predict = back_to_back_predict - len(values)
        
        cprint(f"Day Prediction: {back_to_back_predict}", "blue", attrs=["bold"])
        
        return render_template("dashboard.html", user=os.environ["USER"], email=email, labels=labels, values=values, foods=foods, city=city, days=perfect_day, file=recent_file, show=show_upload, predict=back_to_back_predict)

@app.route('/create/<date>')
def create(date):
    create_all_day_event(date)
    return redirect(url_for("index"))

@app.route('/google-auth')
def google_auth():
    check_auth()
    google_redirect()
    return redirect(url_for("index"))

def check_auth():
    if not github.authorized:
        return redirect(url_for("index"))
    elif not os.environ.get("USER"):
        return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)