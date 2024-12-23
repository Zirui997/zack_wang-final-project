from setuptools import setup, find_packages

setup(
    name="custom_api_client",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["requests"],
    license="MIT",
    description="A Python client for interacting with OpenWeatherMap API.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Zirui997/zack_wang-final-project", 
    author="Zirui-Wang",
    author_email="zw3055@columbia.edu",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
