clean:
	@find . -iname "*.log" -exec rm {} \;
	@rm -rf ./logoutput/ad/shows/*