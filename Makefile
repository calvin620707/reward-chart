pip-install:
	pip install -r requirements.txt

ansible-pkg:
	ansible-playbook -i ansible/hosts ansible/packages.yml

ansible-deploy:
	ansible-playbook -i ansible/hosts ansible/deploy.yml
