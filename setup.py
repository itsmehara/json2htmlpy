from setuptools import setup, find_packages

setup(
    name="json2htmlpy",  # Package name
    version="1.0.0",  # Version number
    description="A simple script to convert JSON to HTML tables.",  # Short description
    long_description=open('README.md').read(),  # Long description from README
    long_description_content_type="text/markdown",  # Type of long description
    author="Haranadh",  # My name
    author_email="hara2help@gmail.com",  # My email
    url="https://github.com/itsmehara/json2htmlpy",  # My project’s GitHub URL
    packages=find_packages(),  # Automatically find packages in My repository
    include_package_data=True,  # Include other files as defined in MANIFEST.in
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "beautifulsoup4",  # Add your dependencies here
        "bs4",
        "build"
    ],
    entry_points={
        "console_scripts": [
            "json2html=json2htmlpy.jsontohtml:main",  # Replace with your command and function
        ],
    },
)
