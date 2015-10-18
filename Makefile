all:
	node build.js

dev: all
	s3cmd --recursive sync build-content/* s3://new.version2beta.com

prod: all
	s3cmd --recursive sync build-content/* s3://version2beta.com

.PHONY: all dev prod
