#Makefile by Nicolas Mavromatis, nima6629

#compiler defined
CC = gcc
#variable entered in as OPTS= on cmd line, set to -Wall by default
OPTS ?= -Wall
#needed to include math.h
LDFLAGS = -lm
#all the obj files that will be created
OBJFILES= app.o soar.o vouched.o marine.o
#executable file to be created
TARGET= app

#Test files:
TESTTARGET= run_test
TESTOBJFILES= test.o vouched.o soar.o marine.o

#Not completely sure what this does/why it is necessary...
all: $(TARGET)

#Create an executable file.
#First, it compiles code into object code, or machine code (.o files)
#These are linked to create executable. 
$(TARGET): $(OBJFILES)
	$(CC) $(OPTS) -o $(TARGET) $(OBJFILES) $(LDFLAGS)
    

#compile test code into exe and run
test:$(TESTOBJFILES)
	$(CC) $(OPTS) -o $(TESTTARGET) $(TESTOBJFILES) $(LDFLAGS)
	./run_test
    
#Clean deletes all the .o files so they can be made fresh. I elected not to remove the executables, though not a bad idea.
clean:
	rm -f $(OBJFILES) $(TESTOBJFILES) *~
