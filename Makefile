define HEADER
  _ __  _   _  ___ ___  _ __  _ __   ___  _ __| |_ 
 | '_ \\| | | |/ __/ _ \\| '_ \\| '_ \\ / _ \\/ __| __|
 | |_) | |_| | (_| (_) | | | | | | |  __/ (__| |_ 
 | .__/ \\__, |\\___\\___/|_| |_|_| |_|\\___|\\___|\\__|
 | |     __/ |                                    
 |_|    |___/     
--------------------------------------------------------
endef
export HEADER


header:
	clear
	@echo "$$HEADER"

run: 
	python3 pycon/__main__.py

install:
	pip3 install -r requirements.txt
	
venv: 
	test -d venv || virtualenv -p python3 --no-site-packages venv
	
test:
	python3 -m unittest discover

clean:
	rm -rf venv
	find -iname "*.pyc" -delete
	