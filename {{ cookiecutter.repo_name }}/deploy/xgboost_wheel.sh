#!/usr/bin/env bash
set -e

python -c \
"print(' {wrap}\n{message:^60}\n {wrap}'.format(wrap='='*60, message='BUILDING XGBOOST WHEEL'))"

cd /tmp
git clone --recursive https://github.com/dmlc/xgboost xgboost-wheel-build
cd xgboost-wheel-build

python -c \
"print(' {wrap}\n{message:^60}\n {wrap}'.format(wrap='.'*60, message='BUILDING XGBOOST'))"

make -j4
cd python-package
cp ../lib/libxgboost.so xgboost/
mv setup.py backup.setup.py && mv setup_pip.py setup.py
pip wheel . --no-deps --wheel-dir $1
rm -rf /tmp/xgboost-wheel-build

python -c \
"print(' {wrap}\n{message:^60}\n {wrap}'.format(wrap='-'*60, message='OK'))"