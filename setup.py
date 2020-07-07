import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="meta_envs", 
    version="0.0.1",
    author="Ray",
    author_email="2199192959@qq.com",
    description="An environment package for meta reinforcement learning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/YangRui2015/Meta-Envs",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
)
