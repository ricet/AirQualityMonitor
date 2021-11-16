sudo apt-get install -y adduser libfontconfig1
wget https://dl.grafana.com/oss/release/grafana_8.2.4_armhf.deb
sudo dpkg -i grafana_8.2.4_armhf.deb

sudo systemctl daemon-reload
sudo systemctl enable grafana-server.service
sudo systemctl start grafana-server

grafana-cli plugins install frser-sqlite-datasource
sudo systemctl restart grafana-server