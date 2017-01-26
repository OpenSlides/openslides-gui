from setuptools import setup, find_packages

with open('README.rst') as readme:
    long_description = readme.read()

setup(
    name="openslides-gui",
    version="1.1.1",
    description="GUI frontend for managing OpenSlides server",
    long_description=long_description,
    url='https://github.com/OpenSlides/openslides-gui',
    author='OpenSlides-Team, see README',
    author_email='support@openslides.org',
    license='MIT',
    keywords='OpenSlides',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
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
