import setuptools

__version__ = "0.0.0"

REPO_NAME = "end-to-end-ml-project-with-mlflow"
SRC_REPO = "mlproject"
AUTHOR_USERNAME = "Vedansh1857"
AUTHOR_EMAIL = "vedanshgupta606@gmail.com"

with open("README.md", 'r', encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USERNAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ML app",
    long_description=long_description,
    url=f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)