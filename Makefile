CC = g++

CPP = $(wildcard *.cpp)

OBJ = $(addprefix bin/,$(notdir $(CPP:.cpp=.o)))

CFLAGS = -Wall -ansi -pedantic

DEBUG = -g

LIBS = -lboost_regex


bin/main: $(OBJ)
	$(CC) -o $@ $^ $(LIBS)


bin/%.o: %.cpp
	$(CC) $(CLFAGS) $(DEBUG) -c -o $@ $<


run: clean bin/main
	chmod +x bin/main
	./bin/main


clean:
	rm -rf bin/*
	mkdir -p bin
