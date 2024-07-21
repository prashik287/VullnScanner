import socket
import platform
from flask import Flask, render_template,request,url_for,redirect
import os
# Importing modules and classes from your application
from modules.portscan import PortScanner
from modules.recon import Reconnaissance
from modules.domaincheck import is_domain_name, is_ip_address
from modules.cvem import cvemitre
from firebase import firebase

# Initialize Firebase connection
firebase = firebase.FirebaseApplication('https://vulnscanner-72253-default-rtdb.firebaseio.com/', None)

# Static image directory
img = os.path.join('static', 'Image')

# Initialize Flask application
app = Flask(__name__)

# Route to render hello.html with user parameter
@app.route('/hello/<user>')
def hello_name(user):
    return render_template('hello.html', name=user)

# Route for home page
@app.route('/')
def home_name():
    return render_template('index.html')

# Route for handling target setting
@app.route('/sethost', methods=['POST', 'GET'])
def sethost():
    if request.method == 'POST':
        target = request.form.get('target')
        action = request.form.get('action')

        if action == 'reconnaissance':
            return redirect(url_for('recon', target=target))
        elif action == 'port_scanning':
            return redirect(url_for('ports', target=target))
        elif action == 'reconpriv':
            return redirect(url_for('privaterecon', target=target))
        else:
            return "Invalid action", 400

    else:
        image_url = url_for('static', filename='Image/coding-background.jpg')
        return render_template('gethost.html', image_url=image_url)

# Route for handling port scanning
@app.route('/ports', methods=['GET','POST'])
def ports():
    target = request.args.get('target')
    if request.method == "POST":
        return f"Portscan Result for : {target}"
    
    scanner = PortScanner()
    open_ports1 = scanner.main(target)
    
    if open_ports1 == "No open Ports found":
        return render_template('port.html', result=open_ports1, vul="" )
    else:
        banner = open_ports1.split("  ")[1]
        cv = cvemitre()
        vuln = cv.getvuln(banner)
        return render_template('port.html', result=open_ports1, vul=vuln )

# Route for contact page
@app.route('/contact', methods=["GET"])
def contact():
    return render_template("contact.html")

# Route for handling form submission
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST' and len(dict(request.form)) > 0:
        userdata = dict(request.form)
        name = userdata["name"]
        email = userdata["email"]
        Subject = userdata["Subject"]
        Message = userdata["Message"]
        new_data = {"name": name, "email": email,"Subject":Subject,"Message":Message}
        firebase.post("/users", new_data)
        return "Thank you!"
    else:
        return "Sorry, there was an error."

# Route for handling reconnaissance
@app.route('/recon', methods=['GET', 'POST'])
def recon():
    target = request.args.get('target')
    if request.method == 'POST':
        # Process further actions here if needed
        return f"Reconnaissance results for: {target}"

    def check_input(input_string):
        if is_ip_address(input_string):
            return input_string
        elif is_domain_name(input_string):
            return socket.gethostbyname(input_string)
        else:
            return "Invalid input"
    
    ip = check_input(target)
    whois_lookup = Reconnaissance.whoislookup(target)
    reverse_dns = Reconnaissance.reverse_dns(target)
    dns_lookup = Reconnaissance.dnslookup(target)
    host_search = Reconnaissance.hostsearch(target)
    zonetransfer = Reconnaissance.zonetransfer(target)
    reverse_lookup = Reconnaissance.reverselookupip(target)

    return render_template('recon.html', target=target, reverse_dns=reverse_dns, dns_lookup=dns_lookup, host_search=host_search, zonetransfer=zonetransfer, reverse_lookup=reverse_lookup, ip=ip, whois_lookup=whois_lookup)



if __name__ == '__main__':
    app.run(debug=True)

