import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()
with open("requirements.txt", "r") as fh:
    requirements = [line.strip() for line in fh]

setuptools.setup(
    name="E2EAF-auth-automation",
    version="0.0.2",
    author="Sumit",
    author_email="sumit@email",
    description="A Python library which implements auth tests and helpers",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    packages=setuptools.find_packages(exclude=["test"]),
    include_package_data=True,
    package_data={
        '': ['*.yaml']
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=requirements,
)
