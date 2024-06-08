Freelancer Jekyll theme  [![Build Status](https://api.travis-ci.org/jeromelachaud/freelancer-theme.svg?branch=master)](https://travis-ci.org/jeromelachaud/freelancer-theme/) 
=========================

Jekyll theme based on [Freelancer bootstrap theme ](http://startbootstrap.com/template-overviews/freelancer/)

For more details, read the [documentation](http://jekyllrb.com/)


### How to update publications

1. open the [link](https://scholar.google.com/citations?hl=en&user=KNZTJ40AAAAJ&view_op=list_works&sortby=pubdate&cstart=0&pagesize=100)
2. go to the bottom, and click `SHOW MORE` until all publications are shown.
3. save the webpage to `update_publications/tmp` directory
4. go to `update_publications`
5. execute `python parse_google_scholar.py tmp/_Fritz\ J\ Sedlazeck_\ -\ _Google\ Scholar_.html` (the html file that was saved at step 3).
6. check the _include directory. If the timestamp of publications.html is now, the update is succeed.
 

#  **********
