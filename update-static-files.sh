echo "~(^^)~ Compiling LESS into CSS"
cd home/static/main/styles
lessc styles.less styles.css


echo "~(^^)~ Beginning upload of new static files"
cd ../..
aws s3 sync . s3://setsuhi-tokyo/static    --acl public-read
