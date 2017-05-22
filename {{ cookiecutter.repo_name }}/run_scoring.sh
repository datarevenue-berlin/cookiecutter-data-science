#!/usr/bin/env bash

git fetch --tags
export VERSION=${VERSION-$(git describe --tags)}
git checkout ${VERSION}

docker pull drtools/{{cookiecutter.repo_name}}-worker:${VERSION}
docker-compose \
    -f deploy/docker-compose.yml \
    -f deploy/docker-compose.prod.yml \
    up \
        --no-build \
        --exit-code-from worker

DATE=`date +%Y-%m-%d`
path="s3://{{cookiecutter.s3_bucket}}/data/predictions/${DATE}.csv.zip"
count=`aws s3 ls $path | wc -l`

if [[ $count -gt 0 ]]; then
    exit 0
else
    exit 1
fi
