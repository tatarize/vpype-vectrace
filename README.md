# vpype-vectrace
Vpype plugin for vector tracing.
See: https://github.com/abey79/vpype

vpype plugin. Reads image files and traces them for the vpype pipeline.

* `iread` load an image for vector tracing


# Vectrace

Pronounced "Vect-Race", Vectrace is a Pure Python Polygon Production Program. Basically the hooks for polygon tracing programs in python are really kinda annoying. And I didn't want to port code that isn't licensed in a maximally useful way, so I wrote my own.

This is especially useful because vpype does not need a bunch of preprocessing. The main goal of Vectrace is to create perfect vectors from images. The optimizations and modifications can be done elsewhere in the pipeline. Or not at all, I don't really mind/care.


# Installing
`$ pip install vpype-vectrace`


# Supported Formats.

Vectrace supports all image formats that are supported by Pillow.

# Example

`vpype iread github.png write github.svg`

* Original.
    * ![github](https://user-images.githubusercontent.com/3302478/107616468-fe78dc00-6c02-11eb-8de0-593b20c646a4.png)
* Vector.
    * ![github-vector](https://user-images.githubusercontent.com/3302478/107616476-00db3600-6c03-11eb-820e-ef56898c9157.png)
* Filled With Black.
    * ![github-vector-filled](https://user-images.githubusercontent.com/3302478/107616478-02a4f980-6c03-11eb-972d-cc629c013335.png)

---

`vpype iread github.png linemerge efill -d 0.3 ewrite github.pes`
(Using vpype-embroidery https://github.com/EmbroidePy/vpype-embroidery )

* ![github-embroidery](https://user-images.githubusercontent.com/3302478/107616955-da69ca80-6c03-11eb-81bb-4150f2f4fb5d.png)
