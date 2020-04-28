import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django_run_command",
    version="1.0.3",
    author="Shahid Tariq",
    author_email="shahidzoonimar@gmail.com",
    description="A Python Django library which helps you to run management commands from admin dashboard",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ShahidTariq/DjangoRunCommands.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
