#!/bin/sh

echo "*********** test help:"
./help 2>&1 > /dev/null
if [ "$?" -eq 0 ]
then
    echo "falco help command line logic test succeeded"
else
    echo "falco help command line logic test FAILED"
    exit
fi
echo "********** database:"
./database 2>&1 > /dev/null
if [ "$?" -eq 0 ]
then
    echo "falco database argument command line logic test succeeded"
else
    echo "falco database argument command line logic test FAILED"
    exit
fi
echo "********** workfile:"
./workfile 2>&1 > /dev/null
if [ "$?" -eq 0 ]
then
    echo "falco workfile logic test succeeded"
else
    echo "falco workfile logic test FAILED"
    exit
fi
echo "********* items:"
./items  2>&1 > /dev/null
if [ "$?" -eq 0 ]
then
    echo "falco number of items test logic succeeded"
else
    echo "falco number of items test logic test FAILED"
    exit
fi
./packagename 2>&1 > /dev/null
echo "********* packagename:"
if [ "$?" -eq 0 ]
then
    echo "falco packagename logic test succeeded"
else
    echo "falco packagename logic test FAILED"
    exit
fi
echo "********* version:"
./version 2>&1 > /dev/null
if [ "$?" -eq 0 ]
then
    echo "falco package version logic test succeeded"
else
    echo "falco package version logic test FAILED"
    exit
fi
echo "********* build:"
./build  2>&1 > /dev/null
if [ "$?" -eq 0 ]
then
    echo "all tests succeeded"
fi
