ansible = ansible-playbook --ask-vault-pass -i ansible/hosts

pip-install:
	pip install -r requirements.txt

ansible-pkg:
	$(ansible) ansible/packages.yml

ansible-deploy:
	$(ansible) ansible/deploy-django.yml
