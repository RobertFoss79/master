CC = gcc
CFLAGS = -std=c11 -Wall
LIBS = cs50.c

# Rule for compiling all C files in the directory
all: $(patsubst %.c,%,$(wildcard *.c))

# Rule to compile each .c file into an executable
%: %.c $(LIBS)
	$(CC) $(CFLAGS) $< $(LIBS) -o $@

# Clean up generated executables
clean:
	rm -f *.exe
