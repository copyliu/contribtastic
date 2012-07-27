#Embedded file name: evecache.pyo
from sys import version_info
if version_info >= (2, 6, 0):

    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_evecache', [dirname(__file__)])
        except ImportError:
            import _evecache
            return _evecache

        if fp is not None:
            try:
                _mod = imp.load_module('_evecache', fp, pathname, description)
            finally:
                fp.close()

            return _mod


    _evecache = swig_import_helper()
    del swig_import_helper
else:
    import _evecache
del version_info

def _swig_setattr_nondynamic(self, class_type, name, value, static = 1):
    if name == 'thisown':
        return self.this.own(value)
    if name == 'this':
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if not static:
        self.__dict__[name] = value
    else:
        raise AttributeError('You cannot add attributes to %s' % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if name == 'thisown':
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError(name)


def _swig_repr(self):
    try:
        strthis = 'proxy of ' + self.this.__repr__()
    except:
        strthis = ''

    return '<%s.%s; %s >' % (self.__class__.__module__, self.__class__.__name__, strthis)


class SwigPyIterator:
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError('No constructor defined - class is abstract')

    __repr__ = _swig_repr
    __swig_destroy__ = _evecache.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _evecache.SwigPyIterator_value(self)

    def incr(self, n = 1):
        return _evecache.SwigPyIterator_incr(self, n)

    def decr(self, n = 1):
        return _evecache.SwigPyIterator_decr(self, n)

    def distance(self, *args):
        return _evecache.SwigPyIterator_distance(self, *args)

    def equal(self, *args):
        return _evecache.SwigPyIterator_equal(self, *args)

    def copy(self):
        return _evecache.SwigPyIterator_copy(self)

    def next(self):
        return _evecache.SwigPyIterator_next(self)

    def __next__(self):
        return _evecache.SwigPyIterator___next__(self)

    def previous(self):
        return _evecache.SwigPyIterator_previous(self)

    def advance(self, *args):
        return _evecache.SwigPyIterator_advance(self, *args)

    def __eq__(self, *args):
        return _evecache.SwigPyIterator___eq__(self, *args)

    def __ne__(self, *args):
        return _evecache.SwigPyIterator___ne__(self, *args)

    def __iadd__(self, *args):
        return _evecache.SwigPyIterator___iadd__(self, *args)

    def __isub__(self, *args):
        return _evecache.SwigPyIterator___isub__(self, *args)

    def __add__(self, *args):
        return _evecache.SwigPyIterator___add__(self, *args)

    def __sub__(self, *args):
        return _evecache.SwigPyIterator___sub__(self, *args)

    def __iter__(self):
        return self


SwigPyIterator_swigregister = _evecache.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)
EStreamStart = _evecache.EStreamStart
ETuple = _evecache.ETuple
ETuple2 = _evecache.ETuple2
E2Tuple = _evecache.E2Tuple
E1Tuple = _evecache.E1Tuple
E1Tuple2 = _evecache.E1Tuple2
E0Tuple = _evecache.E0Tuple
E0Tuple2 = _evecache.E0Tuple2
EMarker = _evecache.EMarker
EIdent = _evecache.EIdent
EString = _evecache.EString
EString2 = _evecache.EString2
EString3 = _evecache.EString3
EString4 = _evecache.EString4
EUnicodeString = _evecache.EUnicodeString
EUnicodeString2 = _evecache.EUnicodeString2
EEmptyString = _evecache.EEmptyString
EInteger = _evecache.EInteger
EReal = _evecache.EReal
E0Real = _evecache.E0Real
E0Integer = _evecache.E0Integer
ENeg1Integer = _evecache.ENeg1Integer
E1Integer = _evecache.E1Integer
EBoolTrue = _evecache.EBoolTrue
EBoolFalse = _evecache.EBoolFalse
EByte = _evecache.EByte
ESizedInt = _evecache.ESizedInt
EShort = _evecache.EShort
EDict = _evecache.EDict
EObject = _evecache.EObject
ENone = _evecache.ENone
ESubstream = _evecache.ESubstream
ELongLong = _evecache.ELongLong
ECompressedRow = _evecache.ECompressedRow
EObject22 = _evecache.EObject22
EObject23 = _evecache.EObject23
ESharedObj = _evecache.ESharedObj

class SNode:
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SNode, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SNode, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _evecache.new_SNode(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    __swig_destroy__ = _evecache.delete_SNode
    __del__ = lambda self: None

    def repl(self):
        return _evecache.SNode_repl(self)

    def type(self):
        return _evecache.SNode_type(self)

    def setType(self, *args):
        return _evecache.SNode_setType(self, *args)

    def addMember(self, *args):
        return _evecache.SNode_addMember(self, *args)

    def members(self):
        return _evecache.SNode_members(self)

    def clone(self):
        return _evecache.SNode_clone(self)


SNode_swigregister = _evecache.SNode_swigregister
SNode_swigregister(SNode)

class SStreamNode(SNode):
    __swig_setmethods__ = {}
    for _s in [SNode]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))

    __setattr__ = lambda self, name, value: _swig_setattr(self, SStreamNode, name, value)
    __swig_getmethods__ = {}
    for _s in [SNode]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))

    __getattr__ = lambda self, name: _swig_getattr(self, SStreamNode, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _evecache.new_SStreamNode(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    __swig_destroy__ = _evecache.delete_SStreamNode
    __del__ = lambda self: None

    def repl(self):
        return _evecache.SStreamNode_repl(self)

    def clone(self):
        return _evecache.SStreamNode_clone(self)


SStreamNode_swigregister = _evecache.SStreamNode_swigregister
SStreamNode_swigregister(SStreamNode)

class SDBHeader(SNode):
    __swig_setmethods__ = {}
    for _s in [SNode]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))

    __setattr__ = lambda self, name, value: _swig_setattr(self, SDBHeader, name, value)
    __swig_getmethods__ = {}
    for _s in [SNode]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))

    __getattr__ = lambda self, name: _swig_getattr(self, SDBHeader, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _evecache.new_SDBHeader()
        try:
            self.this.append(this)
        except:
            self.this = this

    def repl(self):
        return _evecache.SDBHeader_repl(self)

    def clone(self):
        return _evecache.SDBHeader_clone(self)

    __swig_destroy__ = _evecache.delete_SDBHeader
    __del__ = lambda self: None


SDBHeader_swigregister = _evecache.SDBHeader_swigregister
SDBHeader_swigregister(SDBHeader)

class STuple(SNode):
    __swig_setmethods__ = {}
    for _s in [SNode]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))

    __setattr__ = lambda self, name, value: _swig_setattr(self, STuple, name, value)
    __swig_getmethods__ = {}
    for _s in [SNode]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))

    __getattr__ = lambda self, name: _swig_getattr(self, STuple, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _evecache.new_STuple(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    __swig_destroy__ = _evecache.delete_STuple
    __del__ = lambda self: None

    def givenLength(self):
        return _evecache.STuple_givenLength(self)

    def addMember(self, *args):
        return _evecache.STuple_addMember(self, *args)

    def repl(self):
        return _evecache.STuple_repl(self)

    def clone(self):
        return _evecache.STuple_clone(self)


STuple_swigregister = _evecache.STuple_swigregister
STuple_swigregister(STuple)

class SDict(SNode):
    __swig_setmethods__ = {}
    for _s in [SNode]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))

    __setattr__ = lambda self, name, value: _swig_setattr(self, SDict, name, value)
    __swig_getmethods__ = {}
    for _s in [SNode]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))

    __getattr__ = lambda self, name: _swig_getattr(self, SDict, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _evecache.new_SDict(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    __swig_destroy__ = _evecache.delete_SDict
    __del__ = lambda self: None

    def givenLength(self):
        return _evecache.SDict_givenLength(self)

    def addMember(self, *args):
        return _evecache.SDict_addMember(self, *args)

    def repl(self):
        return _evecache.SDict_repl(self)

    def clone(self):
        return _evecache.SDict_clone(self)

    def getByName(self, *args):
        return _evecache.SDict_getByName(self, *args)


SDict_swigregister = _evecache.SDict_swigregister
SDict_swigregister(SDict)

class SNone(SNode):
    __swig_setmethods__ = {}
    for _s in [SNode]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))

    __setattr__ = lambda self, name, value: _swig_setattr(self, SNone, name, value)
    __swig_getmethods__ = {}
    for _s in [SNode]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))

    __getattr__ = lambda self, name: _swig_getattr(self, SNone, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _evecache.new_SNone()
        try:
            self.this.append(this)
        except:
            self.this = this

    def repl(self):
        return _evecache.SNone_repl(self)

    def clone(self):
        return _evecache.SNone_clone(self)

    __swig_destroy__ = _evecache.delete_SNone
    __del__ = lambda self: None


SNone_swigregister = _evecache.SNone_swigregister
SNone_swigregister(SNone)

class SMarker(SNode):
    __swig_setmethods__ = {}
    for _s in [SNode]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))

    __setattr__ = lambda self, name, value: _swig_setattr(self, SMarker, name, value)
    __swig_getmethods__ = {}
    for _s in [SNode]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))

    __getattr__ = lambda self, name: _swig_getattr(self, SMarker, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _evecache.new_SMarker(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def id(self):
        return _evecache.SMarker_id(self)

    def string(self):
        return _evecache.SMarker_string(self)

    def repl(self):
        return _evecache.SMarker_repl(self)

    def clone(self):
        return _evecache.SMarker_clone(self)

    __swig_destroy__ = _evecache.delete_SMarker
    __del__ = lambda self: None


SMarker_swigregister = _evecache.SMarker_swigregister
SMarker_swigregister(SMarker)

class SIdent(SNode):
    __swig_setmethods__ = {}
    for _s in [SNode]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))

    __setattr__ = lambda self, name, value: _swig_setattr(self, SIdent, name, value)
    __swig_getmethods__ = {}
    for _s in [SNode]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))

    __getattr__ = lambda self, name: _swig_getattr(self, SIdent, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _evecache.new_SIdent(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def name(self):
        return _evecache.SIdent_name(self)

    def repl(self):
        return _evecache.SIdent_repl(self)

    def clone(self):
        return _evecache.SIdent_clone(self)

    __swig_destroy__ = _evecache.delete_SIdent
    __del__ = lambda self: None


SIdent_swigregister = _evecache.SIdent_swigregister
SIdent_swigregister(SIdent)

class SString(SNode):
    __swig_setmethods__ = {}
    for _s in [SNode]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))

    __setattr__ = lambda self, name, value: _swig_setattr(self, SString, name, value)
    __swig_getmethods__ = {}
    for _s in [SNode]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))

    __getattr__ = lambda self, name: _swig_getattr(self, SString, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _evecache.new_SString(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def string(self):
        return _evecache.SString_string(self)

    def repl(self):
        return _evecache.SString_repl(self)

    def clone(self):
        return _evecache.SString_clone(self)

    __swig_destroy__ = _evecache.delete_SString
    __del__ = lambda self: None


SString_swigregister = _evecache.SString_swigregister
SString_swigregister(SString)

class SInt(SNode):
    __swig_setmethods__ = {}
    for _s in [SNode]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))

    __setattr__ = lambda self, name, value: _swig_setattr(self, SInt, name, value)
    __swig_getmethods__ = {}
    for _s in [SNode]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))

    __getattr__ = lambda self, name: _swig_getattr(self, SInt, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _evecache.new_SInt(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def value(self):
        return _evecache.SInt_value(self)

    def repl(self):
        return _evecache.SInt_repl(self)

    def clone(self):
        return _evecache.SInt_clone(self)

    __swig_destroy__ = _evecache.delete_SInt
    __del__ = lambda self: None


SInt_swigregister = _evecache.SInt_swigregister
SInt_swigregister(SInt)

class SReal(SNode):
    __swig_setmethods__ = {}
    for _s in [SNode]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))

    __setattr__ = lambda self, name, value: _swig_setattr(self, SReal, name, value)
    __swig_getmethods__ = {}
    for _s in [SNode]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))

    __getattr__ = lambda self, name: _swig_getattr(self, SReal, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _evecache.new_SReal(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def value(self):
        return _evecache.SReal_value(self)

    def repl(self):
        return _evecache.SReal_repl(self)

    def clone(self):
        return _evecache.SReal_clone(self)

    __swig_destroy__ = _evecache.delete_SReal
    __del__ = lambda self: None


SReal_swigregister = _evecache.SReal_swigregister
SReal_swigregister(SReal)

class SLongLong(SNode):
    __swig_setmethods__ = {}
    for _s in [SNode]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))

    __setattr__ = lambda self, name, value: _swig_setattr(self, SLongLong, name, value)
    __swig_getmethods__ = {}
    for _s in [SNode]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))

    __getattr__ = lambda self, name: _swig_getattr(self, SLongLong, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _evecache.new_SLongLong(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def value(self):
        return _evecache.SLongLong_value(self)

    def repl(self):
        return _evecache.SLongLong_repl(self)

    def clone(self):
        return _evecache.SLongLong_clone(self)

    __swig_destroy__ = _evecache.delete_SLongLong
    __del__ = lambda self: None


SLongLong_swigregister = _evecache.SLongLong_swigregister
SLongLong_swigregister(SLongLong)

class SObject(SNode):
    __swig_setmethods__ = {}
    for _s in [SNode]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))

    __setattr__ = lambda self, name, value: _swig_setattr(self, SObject, name, value)
    __swig_getmethods__ = {}
    for _s in [SNode]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))

    __getattr__ = lambda self, name: _swig_getattr(self, SObject, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _evecache.new_SObject()
        try:
            self.this.append(this)
        except:
            self.this = this

    def name(self):
        return _evecache.SObject_name(self)

    def repl(self):
        return _evecache.SObject_repl(self)

    def clone(self):
        return _evecache.SObject_clone(self)

    __swig_destroy__ = _evecache.delete_SObject
    __del__ = lambda self: None


SObject_swigregister = _evecache.SObject_swigregister
SObject_swigregister(SObject)

class SSubstream(SNode):
    __swig_setmethods__ = {}
    for _s in [SNode]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))

    __setattr__ = lambda self, name, value: _swig_setattr(self, SSubstream, name, value)
    __swig_getmethods__ = {}
    for _s in [SNode]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))

    __getattr__ = lambda self, name: _swig_getattr(self, SSubstream, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _evecache.new_SSubstream(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def repl(self):
        return _evecache.SSubstream_repl(self)

    def clone(self):
        return _evecache.SSubstream_clone(self)

    __swig_destroy__ = _evecache.delete_SSubstream
    __del__ = lambda self: None


SSubstream_swigregister = _evecache.SSubstream_swigregister
SSubstream_swigregister(SSubstream)

class SDBRow(SNode):
    __swig_setmethods__ = {}
    for _s in [SNode]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))

    __setattr__ = lambda self, name, value: _swig_setattr(self, SDBRow, name, value)
    __swig_getmethods__ = {}
    for _s in [SNode]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))

    __getattr__ = lambda self, name: _swig_getattr(self, SDBRow, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _evecache.new_SDBRow(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def isLast(self):
        return _evecache.SDBRow_isLast(self)

    def setLast(self, *args):
        return _evecache.SDBRow_setLast(self, *args)

    def repl(self):
        return _evecache.SDBRow_repl(self)

    def clone(self):
        return _evecache.SDBRow_clone(self)

    __swig_destroy__ = _evecache.delete_SDBRow
    __del__ = lambda self: None


SDBRow_swigregister = _evecache.SDBRow_swigregister
SDBRow_swigregister(SDBRow)

class SDBRecords(SNode):
    __swig_setmethods__ = {}
    for _s in [SNode]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))

    __setattr__ = lambda self, name, value: _swig_setattr(self, SDBRecords, name, value)
    __swig_getmethods__ = {}
    for _s in [SNode]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))

    __getattr__ = lambda self, name: _swig_getattr(self, SDBRecords, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _evecache.new_SDBRecords()
        try:
            self.this.append(this)
        except:
            self.this = this

    def repl(self):
        return _evecache.SDBRecords_repl(self)

    def clone(self):
        return _evecache.SDBRecords_clone(self)

    __swig_destroy__ = _evecache.delete_SDBRecords
    __del__ = lambda self: None


SDBRecords_swigregister = _evecache.SDBRecords_swigregister
SDBRecords_swigregister(SDBRecords)

class Parser:
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Parser, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Parser, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _evecache.new_Parser(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    __swig_destroy__ = _evecache.delete_Parser
    __del__ = lambda self: None

    def parse(self):
        return _evecache.Parser_parse(self)

    def streams(self):
        return _evecache.Parser_streams(self)


Parser_swigregister = _evecache.Parser_swigregister
Parser_swigregister(Parser)

class MarketOrder:
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MarketOrder, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MarketOrder, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _evecache.new_MarketOrder()
        try:
            self.this.append(this)
        except:
            self.this = this

    def toCsv(self):
        return _evecache.MarketOrder_toCsv(self)

    def setPrice(self, *args):
        return _evecache.MarketOrder_setPrice(self, *args)

    def setVolRemaining(self, *args):
        return _evecache.MarketOrder_setVolRemaining(self, *args)

    def setRange(self, *args):
        return _evecache.MarketOrder_setRange(self, *args)

    def setOrderID(self, *args):
        return _evecache.MarketOrder_setOrderID(self, *args)

    def setVolEntered(self, *args):
        return _evecache.MarketOrder_setVolEntered(self, *args)

    def setMinVolume(self, *args):
        return _evecache.MarketOrder_setMinVolume(self, *args)

    def setBid(self, *args):
        return _evecache.MarketOrder_setBid(self, *args)

    def setIssued(self, *args):
        return _evecache.MarketOrder_setIssued(self, *args)

    def setDuration(self, *args):
        return _evecache.MarketOrder_setDuration(self, *args)

    def setStationID(self, *args):
        return _evecache.MarketOrder_setStationID(self, *args)

    def setRegionID(self, *args):
        return _evecache.MarketOrder_setRegionID(self, *args)

    def setSolarSystemID(self, *args):
        return _evecache.MarketOrder_setSolarSystemID(self, *args)

    def setJumps(self, *args):
        return _evecache.MarketOrder_setJumps(self, *args)

    def setType(self, *args):
        return _evecache.MarketOrder_setType(self, *args)

    def price(self):
        return _evecache.MarketOrder_price(self)

    def volRemaining(self):
        return _evecache.MarketOrder_volRemaining(self)

    def range(self):
        return _evecache.MarketOrder_range(self)

    def orderID(self):
        return _evecache.MarketOrder_orderID(self)

    def volEntered(self):
        return _evecache.MarketOrder_volEntered(self)

    def minVolume(self):
        return _evecache.MarketOrder_minVolume(self)

    def isBid(self):
        return _evecache.MarketOrder_isBid(self)

    def issued(self):
        return _evecache.MarketOrder_issued(self)

    def duration(self):
        return _evecache.MarketOrder_duration(self)

    def stationID(self):
        return _evecache.MarketOrder_stationID(self)

    def regionID(self):
        return _evecache.MarketOrder_regionID(self)

    def solarSystemID(self):
        return _evecache.MarketOrder_solarSystemID(self)

    def jumps(self):
        return _evecache.MarketOrder_jumps(self)

    def type(self):
        return _evecache.MarketOrder_type(self)

    __swig_destroy__ = _evecache.delete_MarketOrder
    __del__ = lambda self: None


MarketOrder_swigregister = _evecache.MarketOrder_swigregister
MarketOrder_swigregister(MarketOrder)

class MarketList:
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MarketList, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MarketList, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _evecache.new_MarketList(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def setType(self, *args):
        return _evecache.MarketList_setType(self, *args)

    def setRegion(self, *args):
        return _evecache.MarketList_setRegion(self, *args)

    def setTimestamp(self, *args):
        return _evecache.MarketList_setTimestamp(self, *args)

    def type(self):
        return _evecache.MarketList_type(self)

    def region(self):
        return _evecache.MarketList_region(self)

    def timestamp(self):
        return _evecache.MarketList_timestamp(self)

    def getSellOrders(self):
        return _evecache.MarketList_getSellOrders(self)

    def getBuyOrders(self):
        return _evecache.MarketList_getBuyOrders(self)

    def addOrder(self, *args):
        return _evecache.MarketList_addOrder(self, *args)

    __swig_destroy__ = _evecache.delete_MarketList
    __del__ = lambda self: None


MarketList_swigregister = _evecache.MarketList_swigregister
MarketList_swigregister(MarketList)

class MarketParser:
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MarketParser, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MarketParser, name)
    __repr__ = _swig_repr
    __swig_destroy__ = _evecache.delete_MarketParser
    __del__ = lambda self: None

    def getList(self):
        return _evecache.MarketParser_getList(self)

    def parse(self):
        return _evecache.MarketParser_parse(self)

    def valid(self):
        return _evecache.MarketParser_valid(self)

    def __init__(self, *args):
        this = _evecache.new_MarketParser(*args)
        try:
            self.this.append(this)
        except:
            self.this = this


MarketParser_swigregister = _evecache.MarketParser_swigregister
MarketParser_swigregister(MarketParser)

class CacheFile:
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CacheFile, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CacheFile, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _evecache.new_CacheFile(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    __swig_destroy__ = _evecache.delete_CacheFile
    __del__ = lambda self: None

    def readFile(self):
        return _evecache.CacheFile_readFile(self)

    def getLength(self):
        return _evecache.CacheFile_getLength(self)

    def end(self):
        return _evecache.CacheFile_end(self)

    def begin(self):
        return _evecache.CacheFile_begin(self)

    def byteAt(self, *args):
        return _evecache.CacheFile_byteAt(self, *args)

    def peekAt(self, *args):
        return _evecache.CacheFile_peekAt(self, *args)


CacheFile_swigregister = _evecache.CacheFile_swigregister
CacheFile_swigregister(CacheFile)

class CacheFile_Iterator:
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CacheFile_Iterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CacheFile_Iterator, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _evecache.new_CacheFile_Iterator(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    __swig_destroy__ = _evecache.delete_CacheFile_Iterator
    __del__ = lambda self: None

    def __eq__(self, *args):
        return _evecache.CacheFile_Iterator___eq__(self, *args)

    def __ne__(self, *args):
        return _evecache.CacheFile_Iterator___ne__(self, *args)

    def atEnd(self):
        return _evecache.CacheFile_Iterator_atEnd(self)

    def position(self):
        return _evecache.CacheFile_Iterator_position(self)

    def limit(self):
        return _evecache.CacheFile_Iterator_limit(self)

    def __iadd__(self, *args):
        return _evecache.CacheFile_Iterator___iadd__(self, *args)

    def peekShort(self):
        return _evecache.CacheFile_Iterator_peekShort(self)

    def peekInt(self):
        return _evecache.CacheFile_Iterator_peekInt(self)

    def peekChar(self):
        return _evecache.CacheFile_Iterator_peekChar(self)

    def peekFloat(self):
        return _evecache.CacheFile_Iterator_peekFloat(self)

    def peekDouble(self):
        return _evecache.CacheFile_Iterator_peekDouble(self)

    def peekString(self, *args):
        return _evecache.CacheFile_Iterator_peekString(self, *args)

    def readShort(self):
        return _evecache.CacheFile_Iterator_readShort(self)

    def readInt(self):
        return _evecache.CacheFile_Iterator_readInt(self)

    def readChar(self):
        return _evecache.CacheFile_Iterator_readChar(self)

    def readFloat(self):
        return _evecache.CacheFile_Iterator_readFloat(self)

    def readDouble(self):
        return _evecache.CacheFile_Iterator_readDouble(self)

    def readString(self, *args):
        return _evecache.CacheFile_Iterator_readString(self, *args)

    def readLongLong(self):
        return _evecache.CacheFile_Iterator_readLongLong(self)

    def seek(self, *args):
        return _evecache.CacheFile_Iterator_seek(self, *args)

    def advance(self, *args):
        return _evecache.CacheFile_Iterator_advance(self, *args)

    def setLimit(self, *args):
        return _evecache.CacheFile_Iterator_setLimit(self, *args)


CacheFile_Iterator_swigregister = _evecache.CacheFile_Iterator_swigregister
CacheFile_Iterator_swigregister(CacheFile_Iterator)

class MarketOrderVector:
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MarketOrderVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MarketOrderVector, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _evecache.MarketOrderVector_iterator(self)

    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _evecache.MarketOrderVector___nonzero__(self)

    def __bool__(self):
        return _evecache.MarketOrderVector___bool__(self)

    def __len__(self):
        return _evecache.MarketOrderVector___len__(self)

    def pop(self):
        return _evecache.MarketOrderVector_pop(self)

    def __getslice__(self, *args):
        return _evecache.MarketOrderVector___getslice__(self, *args)

    def __setslice__(self, *args):
        return _evecache.MarketOrderVector___setslice__(self, *args)

    def __delslice__(self, *args):
        return _evecache.MarketOrderVector___delslice__(self, *args)

    def __delitem__(self, *args):
        return _evecache.MarketOrderVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _evecache.MarketOrderVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _evecache.MarketOrderVector___setitem__(self, *args)

    def append(self, *args):
        return _evecache.MarketOrderVector_append(self, *args)

    def empty(self):
        return _evecache.MarketOrderVector_empty(self)

    def size(self):
        return _evecache.MarketOrderVector_size(self)

    def clear(self):
        return _evecache.MarketOrderVector_clear(self)

    def swap(self, *args):
        return _evecache.MarketOrderVector_swap(self, *args)

    def get_allocator(self):
        return _evecache.MarketOrderVector_get_allocator(self)

    def begin(self):
        return _evecache.MarketOrderVector_begin(self)

    def end(self):
        return _evecache.MarketOrderVector_end(self)

    def rbegin(self):
        return _evecache.MarketOrderVector_rbegin(self)

    def rend(self):
        return _evecache.MarketOrderVector_rend(self)

    def pop_back(self):
        return _evecache.MarketOrderVector_pop_back(self)

    def erase(self, *args):
        return _evecache.MarketOrderVector_erase(self, *args)

    def __init__(self, *args):
        this = _evecache.new_MarketOrderVector(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def push_back(self, *args):
        return _evecache.MarketOrderVector_push_back(self, *args)

    def front(self):
        return _evecache.MarketOrderVector_front(self)

    def back(self):
        return _evecache.MarketOrderVector_back(self)

    def assign(self, *args):
        return _evecache.MarketOrderVector_assign(self, *args)

    def resize(self, *args):
        return _evecache.MarketOrderVector_resize(self, *args)

    def insert(self, *args):
        return _evecache.MarketOrderVector_insert(self, *args)

    def reserve(self, *args):
        return _evecache.MarketOrderVector_reserve(self, *args)

    def capacity(self):
        return _evecache.MarketOrderVector_capacity(self)

    __swig_destroy__ = _evecache.delete_MarketOrderVector
    __del__ = lambda self: None


MarketOrderVector_swigregister = _evecache.MarketOrderVector_swigregister
MarketOrderVector_swigregister(MarketOrderVector)

class UnsignedCharVector:
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, UnsignedCharVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, UnsignedCharVector, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _evecache.UnsignedCharVector_iterator(self)

    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _evecache.UnsignedCharVector___nonzero__(self)

    def __bool__(self):
        return _evecache.UnsignedCharVector___bool__(self)

    def __len__(self):
        return _evecache.UnsignedCharVector___len__(self)

    def pop(self):
        return _evecache.UnsignedCharVector_pop(self)

    def __getslice__(self, *args):
        return _evecache.UnsignedCharVector___getslice__(self, *args)

    def __setslice__(self, *args):
        return _evecache.UnsignedCharVector___setslice__(self, *args)

    def __delslice__(self, *args):
        return _evecache.UnsignedCharVector___delslice__(self, *args)

    def __delitem__(self, *args):
        return _evecache.UnsignedCharVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _evecache.UnsignedCharVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _evecache.UnsignedCharVector___setitem__(self, *args)

    def append(self, *args):
        return _evecache.UnsignedCharVector_append(self, *args)

    def empty(self):
        return _evecache.UnsignedCharVector_empty(self)

    def size(self):
        return _evecache.UnsignedCharVector_size(self)

    def clear(self):
        return _evecache.UnsignedCharVector_clear(self)

    def swap(self, *args):
        return _evecache.UnsignedCharVector_swap(self, *args)

    def get_allocator(self):
        return _evecache.UnsignedCharVector_get_allocator(self)

    def begin(self):
        return _evecache.UnsignedCharVector_begin(self)

    def end(self):
        return _evecache.UnsignedCharVector_end(self)

    def rbegin(self):
        return _evecache.UnsignedCharVector_rbegin(self)

    def rend(self):
        return _evecache.UnsignedCharVector_rend(self)

    def pop_back(self):
        return _evecache.UnsignedCharVector_pop_back(self)

    def erase(self, *args):
        return _evecache.UnsignedCharVector_erase(self, *args)

    def __init__(self, *args):
        this = _evecache.new_UnsignedCharVector(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def push_back(self, *args):
        return _evecache.UnsignedCharVector_push_back(self, *args)

    def front(self):
        return _evecache.UnsignedCharVector_front(self)

    def back(self):
        return _evecache.UnsignedCharVector_back(self)

    def assign(self, *args):
        return _evecache.UnsignedCharVector_assign(self, *args)

    def resize(self, *args):
        return _evecache.UnsignedCharVector_resize(self, *args)

    def insert(self, *args):
        return _evecache.UnsignedCharVector_insert(self, *args)

    def reserve(self, *args):
        return _evecache.UnsignedCharVector_reserve(self, *args)

    def capacity(self):
        return _evecache.UnsignedCharVector_capacity(self)

    __swig_destroy__ = _evecache.delete_UnsignedCharVector
    __del__ = lambda self: None


UnsignedCharVector_swigregister = _evecache.UnsignedCharVector_swigregister
UnsignedCharVector_swigregister(UnsignedCharVector)
#+++ okay decompyling C:\Users\Administrator\Desktop\evecache.pyo
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed

