web: gunicorn --chdir ./reward_chart reward_chart.wsgi:application
release: cd reward_chart && python manage.py migrate
