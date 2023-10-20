from setuptools import find_packages, setup

setup(
    name="fakecli",
    version="1.0.0",
    author="FxGen31",
    description="An example of CLI app built with Python Click library.",
    py_modules=["fakecli"],
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "click",
        "requests"
    ],
    entry_points={
        "console_scripts": [
            "fakecli = fake_store_cli_app.cli:safe_entry_point"
        ]
    }
)