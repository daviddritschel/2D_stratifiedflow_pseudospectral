all:
	cd straka/src && make all
	cd robert/src && make all

install:
	cd straka/src && make install
	cd robert/src && make install

clean:
	cd straka/src && make clean
	cd robert/src && make clean
