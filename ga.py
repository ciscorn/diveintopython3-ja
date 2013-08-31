#!/usr/bin/env python

import glob

code = """<script type="text/javascript"> var _gaq = _gaq || []; _gaq.push(['_setAccount', 'UA-27293420-1']); _gaq.push(['_trackPageview']); (function() { var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true; ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js'; var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s); })(); </script>\n"""

for filename in glob.glob("output/*.html"):
    with open(filename, encoding="utf-8") as f:
        data = f.read()
        try:
            i = data.index("<form")
        except ValueError:
            pass
        else:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(data[:i] + code + data[i:])
