import setuptools

VERSION = "0.0.6"

NAME = "prisoners-dilemma-sdk"

INSTALL_REQUIRES = []


setuptools.setup(
    name=NAME,
    version=VERSION,
    description="",
    url=f"https://github.com/youssef-attai/{NAME}",
    project_urls={
        "Source Code": f"https://github.com/youssef-attai/{NAME}"
    },
    author="Youssef Atta'i",
    author_email="youssefjattai@gmail.com",
    license="MIT",
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.10",
    ],
    # Snowpark requires Python 3.8
    python_requires=">=3.8",
    # Requirements
    install_requires=INSTALL_REQUIRES,
    packages=["prisoners_dilemma_sdk"],
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
