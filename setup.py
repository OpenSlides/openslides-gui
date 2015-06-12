from setuptools import setup, find_packages

setup(
    name="openslides-gui",
    version="1.0.0dev1",
    description="GUI frontend for openslides",
    long_description="", # TODO
    url='http://openslides.org',
    author='OpenSlides-Team, see AUTHORS',
    author_email='support@openslides.org',
    license='MIT',
    keywords='OpenSlides',
    classifiers=[
        # TODO: fill those
    ],
    packages=find_packages(),
    install_requires=[
        "openslides",
        "wxPython-Phoenix",
        "psutil",
    ],
    package_data={
        "openslides_gui": [
            "data/openslides.ico",
            "data/openslides-logo_wide.png",
        ],
    },
    entry_points={
        "gui_scripts": [
            "openslides-gui=openslides_gui.gui:main",
        ],
    }
)
