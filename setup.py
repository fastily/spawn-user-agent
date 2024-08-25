import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="spawn-user-agent",
    version="0.0.2",
    author="Fastily",
    author_email="fastily@users.noreply.github.com",
    description="Super simple user agent generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fastily/spawn-user-agent",
    project_urls={
        "Bug Tracker": "https://github.com/fastily/spawn-user-agent/issues",
    },
    include_package_data=True,
    packages=setuptools.find_packages(include=["spawn_user_agent"]),
    install_requires=[],
    classifiers=[
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)
