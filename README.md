# Smart Security Systems
<p>By Ganesh Sankaran</p>
<p>Tested on macOS Mojave and Ubuntu 18.04 LTS</p>
<hr />
<h3>The Challenge</h3>
<p>Your business stores an extraordinary amount of raw security footage which must be searched and analyzed manually. This not only results in a loss in your productivity, but also poses a threat to your business' security.</p>
<h3>The Solution</h3>
<p>Smart Security Systems generates metadata from several security footage streams by passing it through an extremely efficient computer vision algorithm. The metadata is much easier to store, search, and analyze compared to raw video.</p>
<strong>Storage</strong>
<p>Smart Security Systems automatically generates and stores feature-rich metadata from your videos. The memory-efficient nature of metadata means that your data can be stored securely for a long period of time.</p>
<strong>Search</strong>
<p>Smart Security Systems allows you to choose from a variety of filters and tags to find the exact moment you are looking for. Searches are faster and more flexible thanks to the capabilities of Elasticsearch.</p>
<strong>Analysis</strong>
<p>Smart Security Systems employs an extremely quick, accurate, and customizable computer vision algorithm that can notify you of incidents. By harnessing the power of AI, our algorithm surpasses humans in sight and memory.</p>
<h3>Deploying the Django Web Application (macOS)</h3>
<strong>1. Obtaining the Source Code</strong>
<p>a. Clone the repository</p>
<pre>cd ~</pre>
<i><code>~</code> will be the parent directory for the repository</i>
<pre>git clone https://github.com/ganeshsankaran/smart-security-systems.git</pre>
<p>b. Obtain the pre-trained YOLOv3 model</p>
<pre>cd ~/smart-security-systems/SmartSecuritySystems/sss_v1/yolov3-coco/</pre>
<pre>wget --no-check-certificate https://pjreddie.com/media/files/yolov3.weights</pre>
<br />
<strong>2. Setting Up the PostgreSQL Server</strong>
<p>a. Install the necessary packages</p>
<i>Download and install PostgreSQL at <code>https://www.enterprisedb.com/downloads/postgres-postgresql-downloads</code></i>
<i>Then install the command line utilities for PostgreSQL</i>
<pre>brew install postgresql</pre>
<p>b. Create the database</p>
<pre>sudo su - postgres</pre>
<pre>createdb sss</pre>
<pre>exit</pre>
<br />
<strong>3. Setting up the Python Environment</strong>
<p>a. Install the necessary packages</p>
<pre>sudo pip3 install -r ~/smart-security-systems/SmartSecuritySystems/requirements.txt</pre>
<p>b. Configure <code>matplotlib</code></p>
<pre>sudo mkdir ~/.matplotlib/</pre>
<pre>sudo vim matplotlibrc</pre>
<i>Write <code>backend: TkAgg</code> to the file and save changes</i>
<br />
<br />
<strong>4. Deploying the Django Web Application</strong>
<p>a. Configure the database</p>
<pre>sudo python3 ~/smart-security-systems/SmartSecuritySystems/manage.py makemigrations</pre>
<pre>sudo python3 ~/smart-security-systems/SmartSecuritySystems/manage.py migrate</pre>
<p>b. Start the server</p>
<pre>sudo python3 ~/smart-security-systems/SmartSecuritySystems/manage.py runserver 0.0.0.0:80</pre>
<hr />
<h3>Deploying the Django Web Application (Ubuntu)</h3>
<strong>1. Obtaining the Source Code</strong>
<p>a. Clone the repository</p>
<pre>cd ~</pre>
<i><code>~</code> will be the parent directory for the repository</i>
<pre>git clone https://github.com/ganeshsankaran/smart-security-systems.git</pre>
<p>b. Obtain the pre-trained YOLOv3 model</p>
<pre>cd ~/smart-security-systems/SmartSecuritySystems/sss_v1/yolov3-coco/</pre>
<pre>wget --no-check-certificate https://pjreddie.com/media/files/yolov3.weights</pre>
<br />
<strong>2. Setting Up the PostgreSQL Server</strong>
<p>a. Install the necessary packages</p>
<pre>sudo apt install postgresql postgresql-contrib postgresql-server-dev-all</pre>
<p>b. Configure the <code>postgres</code> account</p>
<pre>sudo su - postgres</pre>
<pre>psql</pre>
<i>Set the password to <code>password</code></i>
<pre>\password</pre>
<pre>\q</pre>
<p>c. Create the database</p>
<pre>createdb sss</pre>
<pre>exit</pre>
<br />
<strong>3. Setting up the Python Environment</strong>
<p>a. Install the necessary packages</p>
<pre>sudo pip3 install -r ~/smart-security-systems/SmartSecuritySystems/requirements.txt</pre>
<br />
<strong>4. Deploying the Django Web Application</strong>
<p>a. Configure the database</p>
<pre>sudo python3 ~/smart-security-systems/SmartSecuritySystems/manage.py makemigrations</pre>
<pre>sudo python3 ~/smart-security-systems/SmartSecuritySystems/manage.py migrate</pre>
<p>b. Start the server</p>
<pre>sudo python3 ~/smart-security-systems/SmartSecuritySystems/manage.py runserver 0.0.0.0:80</pre>

