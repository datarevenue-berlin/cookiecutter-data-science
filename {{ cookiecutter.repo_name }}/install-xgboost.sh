#!/usr/bin/env bash

cd ..
git clone --recursive https://github.com/dmlc/xgboost
cd xgboost
sudo make -j4
cd python-package
python3 setup.py install
cd ../../{{cookiecutter.repo_name}}
