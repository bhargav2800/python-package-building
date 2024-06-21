from setuptools import setup, find_packages

setup(
    name='aws_airflow_sdk',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'click',
        'requests',
        'boto3',
        'keyring',
    ],
    entry_points={
        'console_scripts': [
            'aws-airflow-sdk=src.cli:cli',
        ],
    },
)
