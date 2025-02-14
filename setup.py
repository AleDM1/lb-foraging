from setuptools import setup, find_packages

setup(
    name="lbforaging",
    version="1.1.1",
    description="Level Based Foraging Environment",
    author="Filippos Christianos",
    url="https://github.com/AleDM1/lb-foraging",
    packages=find_packages(exclude=["contrib", "docs", "tests"]),
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    install_requires=["numpy", "gym==0.21", "pyglet"],
    extras_require={"test": ["pytest"]},
    include_package_data=True,
)
