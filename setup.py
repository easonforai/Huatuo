import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ehuatuo",
    version="0.1",
    author="Xuming Hua",
    author_email="",
    description="Provide medical NER function",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/easonforai/huatuo",
    packages=setuptools.find_packages(),
    install_requires=['tqdm==4.62.3', 'numpy==1.21.5', 'keras==2.3.1', 'tensorflow==2.1.0',
                      'bert4keras==0.10.9', 'paddlepaddle==2.2.2', 'paddlenlp==2.2.4', 'pyahocorasick==1.4.4'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)