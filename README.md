Tabloid
=======

Makes pretty table in console.


Requirements and dependencies
----------
 - `python 3.*`.

 - [Colorama](https://pypi.python.org/pypi/colorama) needs to color header.

Example
-------
If you run [`example.py`](https://raw.githubusercontent.com/shoonoise/Tabloid/master/example.py) as is, you should see something like (depends on terminal's color scheme):

![Example output](https://github.com/shoonoise/tabloid/raw/master/screenshots/tabloid_demo.png "Demo 1")

Example tolerance to long lines (`example2.py`):

![Example output](https://github.com/shoonoise/tabloid/raw/master/screenshots/tabloid_demo_2.png "Demo 2")


Example using with [pygments](http://pygments.org/) (`example3.py`):

![Example output](https://github.com/shoonoise/tabloid/raw/master/screenshots/tabloid_demo_3.png "Demo 3")

Why not ${YOUR_FAV_LIB}?
-------

Well, at first, existing libs does not tolerant to ~~big data~~ long lines. And it's enough for me.
But, as I've started to write my own lib, I try to add something more.
So, you can define formatting rules for each cell based on column, row or moon size.


