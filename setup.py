from setuptools import setup, find_packages

setup(
    name="strutils",
    version="0.1.0",
    description="Простая Python-библиотека для выполнения стандартных задач",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Vladislav Strogonov",
    author_email="your_email@example.com",
    url="https://github.com/strogs/strutils",
    packages=find_packages(),
    install_requires=[
        "requests>=2.31.0",
    ],
    python_requires=">=3.7",
)
