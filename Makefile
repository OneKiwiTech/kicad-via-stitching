test:
	@echo "Run test"
	python3 dialog.py

release: release.sh
	@echo "Create release"
	./release.sh

install:
	@echo "Install Plugin"
	mkdir via-stitching
	cp __init__.py via-stitching/
	cp -r onekiwi/ via-stitching/
	rm -rf ~/.local/share/kicad/7.0/scripting/plugins/via-stitching/
	mv via-stitching/ ~/.local/share/kicad/7.0/scripting/plugins

uninstall:
	@echo "Uninstall Plugin"
	rm -rf ~/.local/share/kicad/7.0/scripting/plugins/via-stitching/