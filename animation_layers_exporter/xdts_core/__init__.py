"""XDTS Core Library

Core functionality for XDTS export operations.
"""

from .utils import (
    mkdir,
    int_to_str,
    sanitize_filename,
    compute_content_hash,
    make_unique_name,
)
from .document import get_document_info
from .layer import (
    get_animated_layers,
    get_static_layers,
    get_layer_keyframes,
    count_total_keyframes,
)
from .frame_export import FrameExporter
from .xdts_file import (
    create_xdts_document,
    add_track,
    write_xdts_file,
)
from .exporter import XDTSExportEngine, ExportOptions, ExportResult

__all__ = [
    'mkdir',
    'int_to_str', 
    'sanitize_filename',
    'compute_content_hash',
    'make_unique_name',
    'get_document_info',
    'get_animated_layers',
    'get_static_layers',
    'get_layer_keyframes',
    'count_total_keyframes',
    'FrameExporter',
    'create_xdts_document',
    'add_track',
    'write_xdts_file',
    'XDTSExportEngine',
    'ExportOptions',
    'ExportResult',
]
