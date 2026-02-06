"""XDTS File Format Handling

Functions for creating and writing Toei Digital Time Sheet (.xdts) files.
"""

import json
from ..config import XDTS_VERSION, SYMBOL_NULL_CELL


def create_xdts_document(duration: int, scene: str = "1", cut: str = "1") -> dict:
    """Create a new XDTS document structure.
    
    The XDTS format is JSON-based and used by OpenToonz and other
    animation software for timing/exposure sheets.
    
    Args:
        duration: Total number of frames in the animation.
        scene: Scene identifier (default "1").
        cut: Cut/shot identifier (default "1").
        
    Returns:
        Dictionary representing the XDTS document structure.
    """
    return {
        "header": {
            "cut": cut,
            "scene": scene
        },
        "timeTables": [{
            "fields": [{
                "fieldId": 0,
                "tracks": []
            }],
            "duration": duration,
            "name": "Timeline 1",
            "timeTableHeaders": [{
                "fieldId": 0,
                "names": []
            }]
        }],
        "version": XDTS_VERSION
    }


def add_track(xdts_doc: dict, track_name: str, track_number: int) -> dict:
    """Add a new track to the XDTS document.
    
    Each track corresponds to an animated layer from Krita.
    
    Args:
        xdts_doc: The XDTS document to modify.
        track_name: Name of the track (layer name).
        track_number: Track index (0-based).
        
    Returns:
        The track dictionary that was added (for adding frames to).
    """
    track = {
        "frames": [],
        "trackNo": track_number
    }
    
    xdts_doc["timeTables"][0]["fields"][0]["tracks"].append(track)
    xdts_doc["timeTables"][0]["timeTableHeaders"][0]["names"].append(track_name)
    
    return track


def add_frame_to_track(track: dict, frame_number: int, label: str) -> None:
    """Add a frame entry to a track.
    
    Args:
        track: The track dictionary to add to.
        frame_number: The frame number (relative to animation start).
        label: The frame label (cell number or SYMBOL_NULL_CELL).
    """
    track["frames"].append({
        "data": [{"id": 0, "values": [label]}],
        "frame": frame_number
    })


def add_track_terminator(track: dict, duration: int) -> None:
    """Add the null cell terminator at the end of a track.
    
    XDTS tracks should end with a SYMBOL_NULL_CELL entry at the
    duration frame to mark the end of the animation.
    
    Args:
        track: The track to terminate.
        duration: Total animation duration (frame to place terminator).
    """
    add_frame_to_track(track, duration, SYMBOL_NULL_CELL)


def write_xdts_file(xdts_doc: dict, filepath: str) -> str:
    """Write the XDTS document to a file.
    
    The XDTS format requires a specific header line before the JSON content.
    
    Args:
        xdts_doc: The XDTS document to write.
        filepath: Path to the output file (should end in .xdts).
        
    Returns:
        The filepath that was written.
    """
    # Ensure the file has .xdts extension
    if not filepath.lower().endswith('.xdts'):
        filepath = filepath + '.xdts'
    
    with open(filepath, 'w', encoding='utf-8') as f:
        # XDTS files require this header line
        f.write("exchangeDigitalTimeSheet Save Data\n")
        json.dump(xdts_doc, f, indent=4)
    
    return filepath
