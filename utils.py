import os

def list_dirs(path):
    """
    Returns a sorted list of directories in the given path.
    Ignores hidden files and specific system directories.
    """
    if not os.path.exists(path):
        return []
        
    imgore_dirs = {"scripts", ".git", "__pycache__", ".streamlit", "venv", "env"}
    
    return sorted(
        d for d in os.listdir(path)
        if os.path.isdir(os.path.join(path, d)) and d not in imgore_dirs
    )

def list_files(path):
    """
    Returns a sorted list of files in the given path.
    """
    if not os.path.exists(path):
        return []
        
    return sorted(
        f for f in os.listdir(path)
        if os.path.isfile(os.path.join(path, f))
    )
