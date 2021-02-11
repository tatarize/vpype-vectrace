# vpype-vectrace
Vpype plugin for vector tracing.
See: https://github.com/abey79/vpype

vpype plugin. Reads image files and traces them for the vpype pipeline.

* `iread` load an for vector tracing


# Vectrace

Pronounced "Vect-Race", Vectrace is a Pure Python Polygon Production Program. Basically the hooks for polygon tracing programs in python are really kinda annoying. And I didn't want to port code that isn't licensed in a maximally useful way, so I wrote my own. This is especially useful because vpype does not need a bunch of preprocessing. The main goal of Vectrace is to create perfect vectors from images. The optimizations and modifications can be done elsewhere in the pipeline. Or not at all, I don't really mind/care.



# Installing
`$ pip install vpype-vectrace` (Contingent on pypi upload.)


# Supported Formats.

Vectrace supports all formats that are supported by Pillow.