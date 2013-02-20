#flask-handson

##About

Implementation of [flask-handson](http://methane.github.com/flask-handson/) by [Naoki Inada](http://github.com/methane)

##Introduction

###Python3.3じゃなくてPython2.7にした

FlaskがPython3.3に対応してない説とかがあって、  
とりあえずMacにデフォルトでインストールされているPython2.7を使うことにした。  
ただ、システムでふんだんに使われていると思われるので、  
仮想化ために`virtualenv`と`source /bin/activate`で挑戦する。  

##Preference

###distributeをインストールする

+ [python-distribute.org](http://python-distribute.org/)

    curl -O http://python-distribute.org/distribute_setup.py
    
    python ./distribute_setup.py
    
    easy_install --help

###virtualenvをインストールする

+ [virtualenv.org](http://www.virtualenv.org/)

    easy_install virtualenv

###pipをインストールする

+ [pip](http://www.pip-installer.org/)

pipはPythonのパッケージをインストールしてくれる。  

>The easiest way to install and use pip is with virtualenv, since every virtualenv has pip (and it’s dependencies) installed into it automatically.
>When used in this manner, pip will only affect the active virtual environment.

ということで、virtualenvで環境を別途用意して、アクティベートし、  
パッケージがその環境だけに影響するよう、pipを使ってFlaskをインストール。  

pipがなかったらインストールする。

    easy_install pip

###virtualenvを使ってpythonの環境を作成する

デフォルトでインストールされているpythonを使うけど、  
ハンズオンをやる中でシステムに影響しないように。  

    mkdir pythonenv
    
    virtualenv --distribute pythonenv --python python2.7
    
    source ./pythonenv/bin/activate

###Flaskをインストールする

+ [Flask](http://flask.pocoo.org/)

Flaskはpythonで実行されるマイクロフレームワーク。  
システムにインストールされたpython環境にではなく  
別途用意した環境をアクティベートし、インストールする。  

    (pythonenv) pip install Flask

##Implementation

###hello.py




