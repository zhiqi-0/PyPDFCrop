# PyPDFCrop 

This is a pdfcrop tool with similar functionality with `pdfcrop` in linux commandline.
This tool can crop white margins of all pdf pages.

## Install

Install remotely:

```sh
pip install git+https://github.com/zhiqi-0/PyPDFCrop.git
```

Or locally:

```sh
pip install -e .
```

## Usage

```sh
python -m pdfcrop.pdfcrop filename.pdf -o outfile.pdf
```
