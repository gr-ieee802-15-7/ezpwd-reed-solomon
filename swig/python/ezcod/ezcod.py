# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.5
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_ezcod', [dirname(__file__)])
        except ImportError:
            import _ezcod
            return _ezcod
        if fp is not None:
            try:
                _mod = imp.load_module('_ezcod', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _ezcod = swig_import_helper()
    del swig_import_helper
else:
    import _ezcod
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0


class ezcod_base(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ezcod_base, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ezcod_base, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_setmethods__["latitude"] = _ezcod.ezcod_base_latitude_set
    __swig_getmethods__["latitude"] = _ezcod.ezcod_base_latitude_get
    if _newclass:
        latitude = _swig_property(_ezcod.ezcod_base_latitude_get, _ezcod.ezcod_base_latitude_set)
    __swig_setmethods__["latitude_error"] = _ezcod.ezcod_base_latitude_error_set
    __swig_getmethods__["latitude_error"] = _ezcod.ezcod_base_latitude_error_get
    if _newclass:
        latitude_error = _swig_property(_ezcod.ezcod_base_latitude_error_get, _ezcod.ezcod_base_latitude_error_set)
    __swig_setmethods__["longitude"] = _ezcod.ezcod_base_longitude_set
    __swig_getmethods__["longitude"] = _ezcod.ezcod_base_longitude_get
    if _newclass:
        longitude = _swig_property(_ezcod.ezcod_base_longitude_get, _ezcod.ezcod_base_longitude_set)
    __swig_setmethods__["longitude_error"] = _ezcod.ezcod_base_longitude_error_set
    __swig_getmethods__["longitude_error"] = _ezcod.ezcod_base_longitude_error_get
    if _newclass:
        longitude_error = _swig_property(_ezcod.ezcod_base_longitude_error_get, _ezcod.ezcod_base_longitude_error_set)
    __swig_setmethods__["accuracy"] = _ezcod.ezcod_base_accuracy_set
    __swig_getmethods__["accuracy"] = _ezcod.ezcod_base_accuracy_get
    if _newclass:
        accuracy = _swig_property(_ezcod.ezcod_base_accuracy_get, _ezcod.ezcod_base_accuracy_set)
    __swig_setmethods__["confidence"] = _ezcod.ezcod_base_confidence_set
    __swig_getmethods__["confidence"] = _ezcod.ezcod_base_confidence_get
    if _newclass:
        confidence = _swig_property(_ezcod.ezcod_base_confidence_get, _ezcod.ezcod_base_confidence_set)
    __swig_setmethods__["certainty"] = _ezcod.ezcod_base_certainty_set
    __swig_getmethods__["certainty"] = _ezcod.ezcod_base_certainty_get
    if _newclass:
        certainty = _swig_property(_ezcod.ezcod_base_certainty_get, _ezcod.ezcod_base_certainty_set)
    __swig_destroy__ = _ezcod.delete_ezcod_base
    __del__ = lambda self: None

    def encode(self, _preci=0):
        return _ezcod.ezcod_base_encode(self, _preci)

    def decode(self, _ezcod):
        return _ezcod.ezcod_base_decode(self, _ezcod)
ezcod_base_swigregister = _ezcod.ezcod_base_swigregister
ezcod_base_swigregister(ezcod_base)

class ezcod_3_10(ezcod_base):
    __swig_setmethods__ = {}
    for _s in [ezcod_base]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ezcod_3_10, name, value)
    __swig_getmethods__ = {}
    for _s in [ezcod_base]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ezcod_3_10, name)
    PARITY = _ezcod.ezcod_3_10_PARITY
    PRECISION = _ezcod.ezcod_3_10_PRECISION
    CHUNK = _ezcod.ezcod_3_10_CHUNK
    SEP_NONE = _ezcod.ezcod_3_10_SEP_NONE
    SEP_DEFAULT = _ezcod.ezcod_3_10_SEP_DEFAULT
    SEP_DOT = _ezcod.ezcod_3_10_SEP_DOT
    SEP_BANG = _ezcod.ezcod_3_10_SEP_BANG
    SEP_SPACE = _ezcod.ezcod_3_10_SEP_SPACE
    CHK_NONE = _ezcod.ezcod_3_10_CHK_NONE
    CHK_DEFAULT = _ezcod.ezcod_3_10_CHK_DEFAULT
    CHK_DASH = _ezcod.ezcod_3_10_CHK_DASH
    CHK_SPACE = _ezcod.ezcod_3_10_CHK_SPACE
    __swig_setmethods__["precision"] = _ezcod.ezcod_3_10_precision_set
    __swig_getmethods__["precision"] = _ezcod.ezcod_3_10_precision_get
    if _newclass:
        precision = _swig_property(_ezcod.ezcod_3_10_precision_get, _ezcod.ezcod_3_10_precision_set)
    __swig_setmethods__["chunk"] = _ezcod.ezcod_3_10_chunk_set
    __swig_getmethods__["chunk"] = _ezcod.ezcod_3_10_chunk_get
    if _newclass:
        chunk = _swig_property(_ezcod.ezcod_3_10_chunk_get, _ezcod.ezcod_3_10_chunk_set)
    __swig_setmethods__["separator"] = _ezcod.ezcod_3_10_separator_set
    __swig_getmethods__["separator"] = _ezcod.ezcod_3_10_separator_get
    if _newclass:
        separator = _swig_property(_ezcod.ezcod_3_10_separator_get, _ezcod.ezcod_3_10_separator_set)
    __swig_setmethods__["space"] = _ezcod.ezcod_3_10_space_set
    __swig_getmethods__["space"] = _ezcod.ezcod_3_10_space_get
    if _newclass:
        space = _swig_property(_ezcod.ezcod_3_10_space_get, _ezcod.ezcod_3_10_space_set)

    def __init__(self, *args):
        this = _ezcod.new_ezcod_3_10(*args)
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _ezcod.delete_ezcod_3_10
    __del__ = lambda self: None

    def encode(self, _preci=0):
        return _ezcod.ezcod_3_10_encode(self, _preci)

    def decode(self, str):
        return _ezcod.ezcod_3_10_decode(self, str)

    def __repr__(self):
        return _ezcod.ezcod_3_10___repr__(self)

    def __str__(self):
        return _ezcod.ezcod_3_10___str__(self)
ezcod_3_10_swigregister = _ezcod.ezcod_3_10_swigregister
ezcod_3_10_swigregister(ezcod_3_10)

class ezcod_3_11(ezcod_base):
    __swig_setmethods__ = {}
    for _s in [ezcod_base]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ezcod_3_11, name, value)
    __swig_getmethods__ = {}
    for _s in [ezcod_base]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ezcod_3_11, name)
    PARITY = _ezcod.ezcod_3_11_PARITY
    PRECISION = _ezcod.ezcod_3_11_PRECISION
    CHUNK = _ezcod.ezcod_3_11_CHUNK
    SEP_NONE = _ezcod.ezcod_3_11_SEP_NONE
    SEP_DEFAULT = _ezcod.ezcod_3_11_SEP_DEFAULT
    SEP_DOT = _ezcod.ezcod_3_11_SEP_DOT
    SEP_BANG = _ezcod.ezcod_3_11_SEP_BANG
    SEP_SPACE = _ezcod.ezcod_3_11_SEP_SPACE
    CHK_NONE = _ezcod.ezcod_3_11_CHK_NONE
    CHK_DEFAULT = _ezcod.ezcod_3_11_CHK_DEFAULT
    CHK_DASH = _ezcod.ezcod_3_11_CHK_DASH
    CHK_SPACE = _ezcod.ezcod_3_11_CHK_SPACE
    __swig_setmethods__["precision"] = _ezcod.ezcod_3_11_precision_set
    __swig_getmethods__["precision"] = _ezcod.ezcod_3_11_precision_get
    if _newclass:
        precision = _swig_property(_ezcod.ezcod_3_11_precision_get, _ezcod.ezcod_3_11_precision_set)
    __swig_setmethods__["chunk"] = _ezcod.ezcod_3_11_chunk_set
    __swig_getmethods__["chunk"] = _ezcod.ezcod_3_11_chunk_get
    if _newclass:
        chunk = _swig_property(_ezcod.ezcod_3_11_chunk_get, _ezcod.ezcod_3_11_chunk_set)
    __swig_setmethods__["separator"] = _ezcod.ezcod_3_11_separator_set
    __swig_getmethods__["separator"] = _ezcod.ezcod_3_11_separator_get
    if _newclass:
        separator = _swig_property(_ezcod.ezcod_3_11_separator_get, _ezcod.ezcod_3_11_separator_set)
    __swig_setmethods__["space"] = _ezcod.ezcod_3_11_space_set
    __swig_getmethods__["space"] = _ezcod.ezcod_3_11_space_get
    if _newclass:
        space = _swig_property(_ezcod.ezcod_3_11_space_get, _ezcod.ezcod_3_11_space_set)

    def __init__(self, *args):
        this = _ezcod.new_ezcod_3_11(*args)
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _ezcod.delete_ezcod_3_11
    __del__ = lambda self: None

    def encode(self, _preci=0):
        return _ezcod.ezcod_3_11_encode(self, _preci)

    def decode(self, str):
        return _ezcod.ezcod_3_11_decode(self, str)

    def __repr__(self):
        return _ezcod.ezcod_3_11___repr__(self)

    def __str__(self):
        return _ezcod.ezcod_3_11___str__(self)
ezcod_3_11_swigregister = _ezcod.ezcod_3_11_swigregister
ezcod_3_11_swigregister(ezcod_3_11)

class ezcod_3_12(ezcod_base):
    __swig_setmethods__ = {}
    for _s in [ezcod_base]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ezcod_3_12, name, value)
    __swig_getmethods__ = {}
    for _s in [ezcod_base]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ezcod_3_12, name)
    PARITY = _ezcod.ezcod_3_12_PARITY
    PRECISION = _ezcod.ezcod_3_12_PRECISION
    CHUNK = _ezcod.ezcod_3_12_CHUNK
    SEP_NONE = _ezcod.ezcod_3_12_SEP_NONE
    SEP_DEFAULT = _ezcod.ezcod_3_12_SEP_DEFAULT
    SEP_DOT = _ezcod.ezcod_3_12_SEP_DOT
    SEP_BANG = _ezcod.ezcod_3_12_SEP_BANG
    SEP_SPACE = _ezcod.ezcod_3_12_SEP_SPACE
    CHK_NONE = _ezcod.ezcod_3_12_CHK_NONE
    CHK_DEFAULT = _ezcod.ezcod_3_12_CHK_DEFAULT
    CHK_DASH = _ezcod.ezcod_3_12_CHK_DASH
    CHK_SPACE = _ezcod.ezcod_3_12_CHK_SPACE
    __swig_setmethods__["precision"] = _ezcod.ezcod_3_12_precision_set
    __swig_getmethods__["precision"] = _ezcod.ezcod_3_12_precision_get
    if _newclass:
        precision = _swig_property(_ezcod.ezcod_3_12_precision_get, _ezcod.ezcod_3_12_precision_set)
    __swig_setmethods__["chunk"] = _ezcod.ezcod_3_12_chunk_set
    __swig_getmethods__["chunk"] = _ezcod.ezcod_3_12_chunk_get
    if _newclass:
        chunk = _swig_property(_ezcod.ezcod_3_12_chunk_get, _ezcod.ezcod_3_12_chunk_set)
    __swig_setmethods__["separator"] = _ezcod.ezcod_3_12_separator_set
    __swig_getmethods__["separator"] = _ezcod.ezcod_3_12_separator_get
    if _newclass:
        separator = _swig_property(_ezcod.ezcod_3_12_separator_get, _ezcod.ezcod_3_12_separator_set)
    __swig_setmethods__["space"] = _ezcod.ezcod_3_12_space_set
    __swig_getmethods__["space"] = _ezcod.ezcod_3_12_space_get
    if _newclass:
        space = _swig_property(_ezcod.ezcod_3_12_space_get, _ezcod.ezcod_3_12_space_set)

    def __init__(self, *args):
        this = _ezcod.new_ezcod_3_12(*args)
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _ezcod.delete_ezcod_3_12
    __del__ = lambda self: None

    def encode(self, _preci=0):
        return _ezcod.ezcod_3_12_encode(self, _preci)

    def decode(self, str):
        return _ezcod.ezcod_3_12_decode(self, str)

    def __repr__(self):
        return _ezcod.ezcod_3_12___repr__(self)

    def __str__(self):
        return _ezcod.ezcod_3_12___str__(self)
ezcod_3_12_swigregister = _ezcod.ezcod_3_12_swigregister
ezcod_3_12_swigregister(ezcod_3_12)

# This file is compatible with both classic and new-style classes.


