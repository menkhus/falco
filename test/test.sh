#!/bin/sh

echo "*********** test help:"
./help > /dev/null
if [ "$?" -eq 0 ]
then
    echo "falco help command line logic test succeeded"
else
    echo "falco help command line logic test FAILED"
    exit
fi
echo "********** database:"
./database > /dev/null
if [ "$?" -eq 0 ]
then
    echo "falco database argument command line logic test succeeded"
else
    echo "falco database argument command line logic test FAILED"
    exit
fi
echo "********** workfile:"
./workfile > /dev/null
if [ "$?" -eq 0 ]
then
    echo "falco workfile logic test succeeded"
else
    echo "falco workfile logic test FAILED"
    exit
fi
echo "********* items:"
./items > /dev/null
if [ "$?" -eq 0 ]
then
    echo "falco number of items test logic succeeded"
else
    echo "falco number of items test logic test FAILED"
    exit
fi
./packagename > /dev/null
echo "********* packagename:"
if [ "$?" -eq 0 ]
then
    echo "falco packagename logic test succeeded"
else
    echo "falco packagename logic test FAILED"
    exit
fi
echo "********* version:"
./version > /dev/null
if [ "$?" -eq 0 ]
then
    echo "falco package version logic test succeeded"
else
    echo "falco package version logic test FAILED"
    exit
fi
echo "********* build:"
./build  > /dev/null
if [ "$?" -eq 0 ]
then
    echo "all tests succeeded"
fi
