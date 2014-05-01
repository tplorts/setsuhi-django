echo "~(^^)~ Compiling LESS into CSS"
cd home/static/main/styles
lessc -x styles.less styles.compiled.css


echo "~(^^)~ Beginning upload of new static files"
cd ../..
aws s3 sync . s3://setsuhi-tokyo/static   --exclude "node_modules/*"    --acl public-read
