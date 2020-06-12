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
	python3 setup.py
	
install:
	source venv/bin/activate; \
	pip3 install -r requirements.txt; \