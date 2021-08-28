import setuptools

setuptools.setup(
    name="dicioinformal",
    version="0.5.2",
    packages=setuptools.find_packages(),
    extras_require={
        "dev": ["httpx", "bs4"],
    },
    url="https://github.com/renatohribeiro/dicioinformal",
    author="OLixao",
    author_email="contact@olixao.ml",
    maintainer="RuizLenato",
    maintainer_email="renatohribeh@outlook.com",
    description="Search on dicionario informal",
    long_description="No description for now",
    long_description_content_type="text/markdown",
)
