from setuptools import setup, find_packages

setup(
    name="shiro",
    version="0.1.1",  # Replace with your current version
    author="Duncan Miller",
    author_email="python@openshiro.com",
    description="Wrapper for the Shiro API",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/OpenShiro/shiro-python",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.1",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    # Include any package data in MANIFEST.in or specify package_data here
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        "": ["*.txt", "*.rst"],
    },
    # If your package will have a CLI, you can specify entry points here
    entry_points={
        "console_scripts": [
            # Define any executables here
            # "shiro-cli=shiro.cli:main",
        ],
    },
)
