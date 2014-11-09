# test falco as if used in a software build

all:	sdjahf.build.out bash.build.out

# this should pass since sdjahf is not found
sdjahf.build.out:
	../falco -b -d ../vfeed.db -n sdjahf -o sdjahf.build.out


# this will FAIL make because bash is found:
bash.build.out:
	../falco -b -d ../vfeed.db -n bash -o bash.build.out
clean:
	rm sdjahf.build.out
	rm bash.build.out
