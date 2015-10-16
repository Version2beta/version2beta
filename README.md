# version2beta's blog #

This project is just my [blog][], created with [Metalsmith].

[blog]: http://www.version2beta.com "version2beta blog"
[Metalsmith]: http://www.metalsmith.io "Metalsmith static site generator"

## Deployment

QA: `s3cmd --recursive sync build-content/* s3://new.version2beta.com`

Prod: `s3cmd --recursive sync build-content/* s3://version2beta.com`
