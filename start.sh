#!/bin/bash
echo " "
echo " "
echo "***************************************************"
echo "**                                               **"
echo "**  Edit base.py and set the string connection.  **"
echo "**                                               **"
echo "***************************************************"
echo " "
echo " Starting containers..."
echo " "
echo " "
read -t 5
pipenv shell
docker-compose up --build
