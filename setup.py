import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pycon-routable", 
    version="0.0.1",
    author="Steven Bucholtz",
    author_email="steven_bucholtz@hotmail.com",
    description="A simple Python server template for receiving and sending socket-level data.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Routable/pycon",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)