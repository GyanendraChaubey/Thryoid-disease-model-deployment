# Thryoid-disease-model-deployment
This is deployment of thyroid disease prediction model

```
commands requiored for installation on ubuntu on AWS

```

```
sudo apt install python3

sudo apt-get update 

sudo apt-get install python3-venv

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

screen -R deploy python app.py

```

To detach the from the screen run below command and then ctrl+C
```
screen -R deploy 
```



