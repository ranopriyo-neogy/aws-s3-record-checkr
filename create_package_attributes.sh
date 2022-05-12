#!/bin/bash

set -e
PACKAGE_NAME="lambda_function.zip"

if [ -f ${PACKAGE_NAME} ]; then
    rm -f ${PACKAGE_NAME}
fi

pip install -r requirements.txt --target ./package
cd package
zip -r ../${PACKAGE_NAME} .
cd ..
zip -g ${PACKAGE_NAME} lambda_function.py attributes.py