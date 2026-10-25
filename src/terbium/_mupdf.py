"""PyMuPDF, imported under its current module name.

PyMuPDF 1.24.3 added the ``pymupdf`` module name, and from PyMuPDF 2.0 the old
``fitz`` name prints a FutureWarning on import. terbium imports ``pymupdf`` and
falls back to ``fitz`` only on PyMuPDF 1.24.0 to 1.24.2, which
``PyMuPDF>=1.24`` still allows and which have no ``pymupdf`` module.
"""
try:
    import pymupdf
except ImportError:  # PyMuPDF 1.24.0 to 1.24.2
    import fitz as pymupdf

__all__ = ["pymupdf"]
