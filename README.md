#flask-handson

##About

Implementation of flask-handson (http://methane.github.com/flask-handson/) by Naoki Inada

##Start Up

###Python3.3じゃなくてPython2.7にした

FlaskがPython3.3に対応してない説とかがあって、  
とりあえずMacにデフォルトでインストールされているPython2.7を使うことにした。  
ただ、システムでふんだんに使われていると思われるので、  
仮想化ために`virtualenv`と`source /bin/activate`で挑戦する。  

###distributeをインストールする

    curl -O http://python-distribute.org/distribute_setup.py
    
    python ./distribute_setup.py
    
    easy_install --help