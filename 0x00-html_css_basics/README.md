## 0x00. HTML/CSS Basics

![CSSBASICS](https://cdn-images-1.medium.com/max/792/1*lJ32Bl-lHWmNMUSiSq17gQ.png)

## ENVIRONMENT
All code is tested to be W3C compliant and validated with `W3C-Validator`.

## 0. HTML base and default
An HTML page that displays a header.

Layout:

Body:

no margin
no padding
all texts must be:
color: #333333
size: 14px
font family: Helvetica Neue, Helvetica, Aria, sans-serif
Header:

background color #FF0000 (red)
height: 60px
width: 100%

Files: `0-index.html`, `styles/0-common.css`, `styles/0-header.css`

## 1. Header container
Improves on 0-index.html and adds `UL` container in the header.

Layout:

Header:

padding top of 10px
Header -> UL container:

class: container
background color #00FF00 (green)
height: 50px
max-width: 1000px
align center (horizontally and vertically)
no list type
no padding
position relative

Files: `1-index.html`, `styles/0-common.css`, `styles/1-header.css`

## 2. Header logo
Improves on 1-index.html and adds logo in the header

Layout: 

Header -> UL container:

new LI tag:
class: logo
background color #0000FF (blue)
height: 100%
width: 120px
align to the left
Header -> UL container -> LI:

new A tag:
taking 100% of the same (width and height)
source: /

Files: `styles/0-common.css`, `styles/2-header.css`

## 3. Search and User blocks
Improve on 2-index.html by adding a search bar

Layout: 

Header -> UL container:

new LI tag:
class: search
background color #550000
position absolute
height: 40px
left: 140px
right: 220px
margin:
5px on top and bottom
0px on the right and left
new LI tag:
class: user
background color #005500
height: 100%
width: 200px
align to the right
Header -> UL container -> LI.search:

new DIV tag:
class: find
background color: #005555
height: 100%
width: 45%
new DIV tag:
class: location
background color: #009999
height: 100%
width: 45%
new DIV tag:
class: action
background color: #119911
height: 100%
width: 10%
All DIV must be align in the same line

Files: `3-index.html`, `styles/0-common.css`, `styles/3-header.css`

## AUTHOR
Spencer Cheng: [github account](https://github.com/spencerhcheng), [twitter](https://twitter.com/spencerhcheng)
