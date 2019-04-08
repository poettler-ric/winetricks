.PHONY: sources

sources:
	spectool -g winetricks.spec

srpm:
	rpmbuild -bs winetricks.spec \
	    -D "_sourcedir ${PWD}" \
	    -D "_srcrpmdir ${PWD}"
