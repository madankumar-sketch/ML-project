from setuptools import setup, find_packages

setup(
    name='your_package_name',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'ipykernel', 'pandas', 'numpy', 'matplotlib', 'plotly', 'seaborn', 'scipy', 'scikit-learn', 
        'imblearn', 'xgboost', 'catboost', 'pymongo', 'evidently', 'dill', 'PyYAML', 'neuro_mf', 
        'boto3', 'mypy-boto3-s3', 'botocore', 'fastapi', 'uvicorn', 'jinja2', 'python-multipart'
    ],
)
