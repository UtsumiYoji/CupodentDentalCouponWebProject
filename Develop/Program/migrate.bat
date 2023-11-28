python ./manage.py makemigrations common
python ./manage.py makemigrations custom_user
python ./manage.py makemigrations company
python ./manage.py makemigrations coupon
python ./manage.py makemigrations
python ./manage.py migrate
python ./manage.py loaddata fixture.json
