from setuptools import setup, find_packages
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="babygame",
    version="1.0.0",
    author="SLPstream",
    description="A simple fullscreen color cycling game for babies",
    long_description=read("README.md") if os.path.exists("README.md") else "",
    long_description_content_type="text/markdown",
    license="MIT",
    keywords="baby game educational interactive color",
    url="https://github.com/slpstream/babygame",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: MacOS X",
        "Environment :: Win32 (MS Windows)",
        "Environment :: X11 Applications",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Education",
        "Topic :: Games/Entertainment",
    ],
    python_requires=">=3.7",
    install_requires=[
        "pygame>=2.0.0",
        "numpy>=1.20.0",
    ],
    entry_points={
        "console_scripts": [
            "babygame=babygame.python.babycolor:main",
        ],
    },
    include_package_data=True,
)