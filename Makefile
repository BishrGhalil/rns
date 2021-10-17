all: install

install:
	cp subman /usr/bin/subman
	cp lists_header.py /usr/bin/lists_header.py
	cp c_colors.py /usr/bin/c_colors.py

uninstall:
	rm -rf /usr/bin/subman
	rm -rf /usr/bin/lists_header.py
	rm -rf /usr/bin/c_colors.py
