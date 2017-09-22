from setuptools import setup

setup(
    name='spotifycontroller',
    version='0.0.2',
    description='My skill for Snips',
    url='https://github.com/tbluche/spotify-controller',
    download_url='',
    license='MIT',
    install_requires=['requests==2.6.0', 'spotipy==2.4.4'],
    test_suite="tests",
    keywords=['snips'],
    packages=['spotifycontroller'],
    package_data={'spotifycontroller': ['Snipsspec']},
    include_package_data=True,
)
