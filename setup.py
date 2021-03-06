import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mplcamera",
    version="0.0.2",
    author="znstrider",
    author_email="mindfulstrider@gmail.com",
    description="Camera Class to make snapshots of a figure and save a gif from stored images",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/znstrider/mplcamera",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Matplotlib",
        "Topic :: Scientific/Engineering :: Visualization"
    ],
    python_requires='>=3.6',
)
