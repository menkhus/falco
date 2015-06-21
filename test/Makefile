# test falco as if used in a software build

all:	nonexist.build.out bash.build.out multi.build.out

# this should pass since sdjahf is not found
nonexist.build.out:
	../falco -b -d ../vfeed.db -n nonexistant -o nonexist.build.out


# this will FAIL make because bash is found:
bash.build.out:
	../falco -b -d ../vfeed.db -n bash -o bash.build.out

# this will FAIL make because several packages are found:
multi.build.out:
	../falco -b -d ../vfeed.db -f testlist.txt -o multi.build.out
clean:
	rm nonexist.build.out > /dev/null
	rm bash.build.out > /dev/null
	rm multi.build.out > /dev/null

