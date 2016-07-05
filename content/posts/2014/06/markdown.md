Title: Last try of the day
Author:      Yu Cheng  
Date:        2014-06-04 23:40
Tags: reStructuredText, css, pelican, markdown
Category: Blog

A long day with Pelican and reStructuredText, to achieve my goals of embedding iPython notebook and Youtube videos, I feel like I'd better try Markdown, which I am more familiar with, below are some results:


####Image

{% img http://ycheng1.files.wordpress.com/2013/10/trac_anim.gif 500 400 Equatorial Waves%}


####Code

    :::python
    print("Hello world!")


####iPython notebook

{% notebook power_spectrum.ipynb cells[4:6] %}
