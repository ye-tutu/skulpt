class NotImplementedImportError(ImportError, NotImplementedError): pass

def _(name):
    msg = f"{name} is not yet implemented in Skulpt"
    raise NotImplementedImportError(msg, name=name)
