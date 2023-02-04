# External function visibility
__all__ = ['append_extension']


# Module functions

def append_extension(filename: str, extension: str) -> str:
    """
    Function which constructs the filename
    and extension so the user doesn't have to.
    """
    filename = filename.replace(' ', '_')
    match extension:
        case "txt" | "json" | "csv" | "xml":
            return filename + "." + extension
        case other:
            raise RuntimeError(f"This filetype ({other}) is unrecognized and will not be supported in the near future.")