from distutils.core import setup

setup(
    name='hdmi-matrix-api',
    version='1.0.0',
    packages=['app', 'app.utils', 'app.models', 'app.routers'],
    url='https://github.com/mintopia/hdmi-matrix-api',
    license='MIT',
    author='Mintopia',
    author_email='jess@mintopia.net',
    description='REST API for HDMI Matrix Control'
)
