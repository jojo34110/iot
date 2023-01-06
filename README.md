# iot
Apres l'instalation d'influxdb et de grafana.

Creer un repertoire puis ouvrez app.py .

Installer l'environement virtuelle avec la commande :
- python -m venv venv

Puis activez l'environement virtuelle:
- déplacez vous dans le repertoire venv/script
- lancez l'environement virtuelle avec la commande activate

installer les librairies flask et influxdb-client la ou se trouve l'api app.py
- pip3 install flask
- pip3 influxdb-client
Ou utiliser les requirements.txt

Lancer l'api a l'aide de la commande flask --app app run

Puis lancer les capteurs humidity et temperature a l'aide la commande npm run sensors


Remerciement a Hugo.D pour m'avoir aider sur le projet n'etant pas orienté dev se fut compliqué pour moi ...
