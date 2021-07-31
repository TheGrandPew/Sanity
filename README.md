# Sanity The MXSS Fuzzer
--------------------------

## About
  This Fuzzer was orignaly used to find the DOMPurify 2.2.3 bypass, It uses a really bad (but it will work) mutation engine in python to generate html using the tags supplied in gentags.py. The main part of this fuzzer is done in the client side, utilizing iframes as workers that get the html from the backend sanitize it put it in a divs shadow dom then diff the santized output with the div's innerHTML. If the santized and divs innerHTML differers then it will log it as a potential mxss!!

## Running 
  1) python3 server.py
  2) open http://localhost:3333/ui in the browser of choice
  3) click start fuzzer and fuzz away
