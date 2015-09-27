#!/bin/sh

echo "*********** test help:"
./help 2>&1 > /dev/null
if [ "$?" -eq 0 ]
then
    echo "falco help command line logic test succeeded"
else
    echo "falco help command line logic test FAILED"
    exit 1
fi

echo "*********** test format:"
./format 2>&1 > /dev/null
if [ "$?" -eq 0 ]
then
    echo "falco -t format test succeeded"
else
    echo "falco -t format test FAILED"
    exit 1
fi

echo "********** database:"
./database 2>&1 > /dev/null
if [ "$?" -eq 0 ]
then
    echo "falco database argument command line logic test succeeded"
else
    echo "falco database argument command line logic test FAILED"
    exit 1
fi

echo "********** workfile:"
./workfile 2>&1 > /dev/null
if [ "$?" -eq 0 ]
then
    echo "falco workfile logic test succeeded"
else
    echo "falco workfile logic test FAILED"
    exit 1
fi

echo "********* items:"
./items  2>&1 > /dev/null
if [ "$?" -eq 0 ]
then
    echo "falco number of items test logic succeeded"
else
    echo "falco number of items test logic test FAILED"
    exit 1
fi

./packagename 2>&1 > /dev/null
echo "********* packagename:"
if [ "$?" -eq 0 ]
then
    echo "falco packagename logic test succeeded"
else
    echo "falco packagename logic test FAILED"
    exit 1
fi

echo "********* version:"
./version 2>&1 > /dev/null
if [ "$?" -eq 0 ]
then
    echo "falco package version logic test succeeded"
else
    echo "falco package version logic test FAILED"
    exit 1
fi

echo "********* cve:"
./cve 2>&1 > /dev/null
if [ "$?" -eq 0 ]
then
    echo "falco cve logic test succeeded"
else
    echo "falco cvec test FAILED"
    exit 1
fi

echo "********* build:"
./build  2>&1 > /dev/null
if [ "$?" -eq 0 ]
then
    echo "all tests succeeded"
else
    echo "failed build test"
    exit 1
fi
