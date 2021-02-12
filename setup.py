from setuptools import setup


with open("README.md") as f:
    readme = f.read()

setup(
    name="vpype-vectrace",
    version="0.1.0",
    description="vpype polygon tracer plugin",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Tatarize",
    author_email="tatarize@gmail.com",
    url="https://github.com/tatarize/vpype-vectrace/",
    packages=["vpype_vectrace"],
    classifiers=(
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ),
    install_requires=[
        "click",
        "vpype",
        "Pillow",
        "svgelements",
    ],
    entry_points="""
            [vpype.plugins]
            iread=vpype_vectrace.iread:iread
        """,
)