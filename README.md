<strong><h1> VullnScanner </h1></strong>
Simple Vulnerability Scanner
<hr>

<div style="display: flex; justify-content: space-between;">
  <img src="https://github.com/prashik287/VullnScanner/blob/main/screenshots/home.PNG" style="width: 49%;">
  <img src="https://github.com/prashik287/VullnScanner/blob/main/screenshots/portscan.PNG" style="width: 49%;">
</div>
  <img src="https://github.com/prashik287/VullnScanner/blob/main/screenshots/recon.png" style="width: 100%; height:50%">


<!-- ![alt text](https://github.com/prashik287/VullnScanner/blob/main/screenshots/home.PNG)
![alt text](https://github.com/prashik287/VullnScanner/blob/main/screenshots/portscan.PNG)
![alt text](https://github.com/prashik287/VullnScanner/blob/main/screenshots/recon.png) -->

<h2>Descriptiom</h2>
<ul>
<p>A vulnerability scanner is a specialized tool designed to identify security weaknesses in systems, networks, and applications. The proposed scanner focuses on three primary tasks:

<li>Reconnaissance of Target:</li>

The scanner initiates the process by gathering detailed information about the target system or network. This includes discovering IP addresses, domain names, network infrastructure, and publicly available services. The reconnaissance phase provides a comprehensive overview of the target, laying the groundwork for more in-depth analysis.

<li>Port Scanning of Target:</li>

After reconnaissance, the scanner performs a thorough port scan on the target to identify open and accessible ports. This step reveals which services and applications are running on the target system, such as web servers, databases, and email servers. By mapping the open ports, the scanner gains insights into potential entry points that could be exploited.

<li>Displaying Vulnerable Services and Their Vulnerabilities:</li>

The final phase involves analyzing the services discovered during the port scan for known vulnerabilities. The scanner cross-references identified services against a database of common vulnerabilities and exposures (CVEs). It then provides a detailed report to the user, highlighting any vulnerable services and their specific vulnerabilities, along with recommended remediation steps.</p>
</ul>


<h2>Installation</h2>


<pre>git clone https://github.com/prashik287/VullnScanner
      cd VullnScanner
      pip install -r requirements.txt
</pre>

