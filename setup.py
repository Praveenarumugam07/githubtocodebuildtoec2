from setuptools import setup, find_packages

setup(
    name='my-python-app',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],  # Add dependencies if needed
    entry_points={
        'console_scripts': [
            'myapp = my_app.main:main'
        ]
    }
)
