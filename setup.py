import setuptools

install_requires = [
    'PyMuPDF==1.24.7',
]

setuptools.setup(
    name=             'pdfcrop',
    version=          '0.1',
    author=           'Zhiqi Lin',
    description=      'python commandline tools with similar functionality with `pdfcrop` in linux command',
    packages=         ['pdfcrop'],
    python_requires=  '>=3.8',
    install_requires = install_requires,
)
