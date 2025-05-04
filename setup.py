from setuptools import setup, find_packages

setup(
    name='talemai',
    version='0.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'aiofiles',     
        'PyPDF2',       
        'pypdf',
        'pyfiglet',
        'langchain',
        'langchain-community',
        'langchain-astradb',
        'langchain-huggingface',
    ],
    entry_points={
        'console_scripts': [
            'yourscript = yourpackage.scripts.yourscript:cli',  # Update with your actual script and function
        ],
    },
)
