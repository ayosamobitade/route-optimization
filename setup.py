# setup.py

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="route_optimization",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A delivery route optimization system using OR-Tools and Folium",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/route-optimization",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "pandas>=1.3.0",
        "folium>=0.12.1",
        "streamlit>=1.20.0",
        "streamlit-folium>=0.11.0",
        "ortools>=9.5.2237",
        "requests>=2.28.0",
    ],
    entry_points={
        "console_scripts": [
            # Optional CLI entry points can be added here, e.g.:
            # "route-optimize=src.route_optimizer:main",
        ],
    },
)
