# (c) Copyright 2017-2018 OLX
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sys

from user_error import UserError
from var_types import VarEntity


class KubeTypeValidationError(Exception):
    def __init__(self, obj, vstr, path, msg):
        self.obj = obj
        self.path = path
        self.vstr = vstr
        self.msg = msg

    def __str__(self):
        path = self.path
        if path is None:
            path = 'self'
        return "KubeType Validation failed for {}: expected {}, got {} ({}): {}".format(path, self.vstr,
                                                                                   self.obj.__class__.__name__,
                                                                                   repr(self.obj),
                                                                                   self.msg)


class KubeType(object):
    wrapper = False

    def __init__(self, *args):
        if self.wrapper:
            if len(args) != 1:
                raise TypeError("Expected 2 arguments for {}, got {:d}".format(self.__class__.__name__, len(args) + 1))
            self.wrap = self.__class__.construct_arg(args[0])
        else:
            if len(args) != 0:
                raise TypeError("Expected 1 argument for {}, got {:d}".format(self.__class__.__name__, len(args) + 1))

    @classmethod
    def construct_arg(cls, arg):
        if isinstance(arg, type):
            ret = arg()
        else:
            ret = arg

        if not isinstance(ret, KubeType):
            ret = Object(ret.__class__)

        return ret

    @classmethod
    def get_description(cls):
        if cls.__doc__ is not None and cls.__doc__ is not '':
            return '\n'.join([line.strip() for line in cls.__doc__.split('\n')])
        return 'TODO: Description is still missing from the class docstring.\nStay tuned to have more hint about this variable.'

    def original_type(self):
        if self.wrapper:
            return self.wrap.original_type()
        return None

    def name(self, render=None):
        if render is None:
            render = lambda x: x
        if self.wrapper:
            return '{}<{}>'.format(render(self.__class__.__name__), self.wrap.name(render=render))
        return render(self.__class__.__name__)

    def check_wrap(self, value, path):
        if self.wrapper:
            return self.wrap.check(value, path=path)
        return True

    def do_check(self, value, path):
        return False

    def check(self, value, path=None):
        if isinstance(value, VarEntity):
            ret = self.do_check(value.validation_value(), path=path)
        else:
            ret = self.do_check(value, path=path)

        if not ret and hasattr(self, 'validation_text'):
            raise UserError(KubeTypeValidationError(value, self.name(), path, self.validation_text))
        elif not ret:
            raise UserError(KubeTypeValidationError(value, self.name(), path, 'Validation failed'))

        return ret


class Object(KubeType):
    def __init__(self, cls):
        self.cls = cls

    def original_type(self):
        return self.cls

    def name(self, render=None):
        if render is None:
            render = lambda x: x
        return render(self.cls.__name__)

    def do_check(self, value, path):
        self.validation_text = "Not the right object type"
        if not isinstance(value, self.cls):
            return False
        self.validation_text = "Validation call failed"
        if hasattr(value, 'validate'):
            return value.validate(path)
        return True


class Nullable(KubeType):
    """
    This wrapper if telling to rubiks that the parameter could be some valid value or null(None in python)
    """
    validation_text = "Expected type or None"
    wrapper = True

    def do_check(self, value, path):
        if value is None:
            return True
        return self.check_wrap(value, path)


class Boolean(KubeType):
    """
    Boolean, or boolean logic, is a subset of algebra used for creating true/false statements. 
    Boolean expressions use the operators AND, OR, XOR, and NOT to compare values and return a true or false result. 
    """
    validation_text = "Expected boolean"

    def do_check(self, value, path):
        return value is True or value is False


class Enum(KubeType):
    """
    Enum, short for "enumerated," is a data type that consists of predefined values. A constant or variable defined as an enum can store one of the values listed in the enum declaration.

    **Example**

    `Enum('Value1', 'Value2', 'Value3')`
    """
    def __init__(self, *args):
        self.enums = args

    def name(self, md=False):
        def fake_repr(x):
            ret = repr(x)
            if ret.startswith("u'"):
                return ret[1:]
            return ret
        if md:
            return '[{}](#{})({})'.format(self.__class__.__name__, self.__class__.__name__.lower(), ', '.join(map(fake_repr, self.enums)))
        return '{}({})'.format(self.__class__.__name__, ', '.join(map(fake_repr, self.enums)))

    def do_check(self, value, path):
        return value in self.enums


class Integer(KubeType):
    """
    An integer is a whole number (not a fraction) that can be positive, negative, or zero. 
    Therefore, the numbers 10, 0, -25, and 5,148 are all integers. Unlike floating point numbers, integers cannot have decimal places.
    """
    validation_text = "Expected integer"

    def do_check(self, value, path):
        if value is True or value is False:
            return False
        if sys.version_info[0] == 2:
            return isinstance(value, (int, long))
        return isinstance(value, int)


class Number(KubeType):
    """
    An integer is a whole number (not a fraction) that can be positive, negative, floating or zero. 
    """
    validation_text = "Expected number"

    def do_check(self, value, path):
        if value is True or value is False:
            return False
        if sys.version_info[0] == 2:
            return isinstance(value, (int, long, float))
        return isinstance(value, (int, float))


class Positive(KubeType):
    """
    Define a number that needs to be positive (0 is included as positive)
    """
    validation_text = "Expected positive"
    wrapper = True

    def do_check(self, value, path):
        return self.check_wrap(value, path) and value >= 0


class NonZero(KubeType):
    """
    Represent any number that is not 0.
    Will be accepted positive and negative of any kind.
    """
    validation_text = "Expected non-zero"
    wrapper = True

    def do_check(self, value, path):
        return self.check_wrap(value, path) and value != 0


class String(KubeType):
    """
    String is any finite sequence of characters (i.e., letters, numerals, symbols and punctuation marks).
    """
    validation_text = "Expected string"

    def do_check(self, value, path):
        if sys.version_info[0] == 2:
            return isinstance(value, basestring)
        return isinstance(value, str)


class SurgeSpec(KubeType):
    """
    SurgeSpec is expection surge/unavailable type ie integer or percent
    """
    validation_text = "Expected surge/unavailable type ie integer or percent"

    def do_check(self, value, path):
        if value is None:
            return True

        if String().do_check(value, path):
            if len(value) < 2:
                return False
            if value.endswith('%') and value[:-1].isdigit() and int(value[:-1]) < 100:
                return True
            return False
        else:
            return Positive(Integer).do_check(value, path)


class SurgeError(Exception):
    pass


class SurgeCheck(object):
    @classmethod
    def validate(cls, surge, unavailable):
        def check_zero(v):
            if v is None:
                return True

            return (String().do_check(v, None) and int(v[:-1]) == 0) or (v == 0)

        if check_zero(surge) and check_zero(unavailable):
            raise UserError(SurgeError("maxSurge and maxUnavailable cannot both be zero"))

        return True


class IPv4(String):
    """
    Internet Protocol Version 4 (IPv4) is the fourth revision of the Internet Protocol and a widely used protocol in data communication over different kinds of networks. 
    
    IPv4 is a connectionless protocol used in packet-switched layer networks, such as Ethernet.
    
    More documentation can be found on [that URL](https://en.wikipedia.org/wiki/IPv6)
    """
    validation_text = "Expected an IPv4 address"

    def do_check(self, value, path):
        if not String.do_check(self, value, path):
            return False
        ip = value.split('.')
        if len(ip) != 4:
            return False
        def comp_ok(x):
            if x == '' or not x.isdigit():
                return False
            if x == '0':
                return True
            if x.startswith('0'):
                return False
            return int(x) <= 255
        if not all(map(comp_ok, ip)):
            return False
        if int(ip[0]) == 0 or int(ip[0]) == 127:
            return False
        return True


class IPv6(String):
    """
    Internet Protocol Version 6 (IPv6) is an Internet Protocol (IP) used for carrying data in packets from a source to a destination over various networks. 
    
    IPv6 is the enhanced version of IPv4 and can support very large numbers of nodes as compared to IPv4. 
    
    It allows for 2128 possible node, or address, combinations.

    More documentation can be found on [that URL](https://en.wikipedia.org/wiki/IPv6)

    **NOTE:** This function is experimental please report any issue with that.
    """
    validation_text = "Expected an IPv6 address"
    def do_check(self, value, path):
        # Needs to be a string in first place
        if not String.do_check(self, value, path):
            return False
        
        valid_characters = 'ABCDEFabcdef:0123456789'
        is_valid = all(current in valid_characters for current in value)
        address_list = value.split(':')
        valid_segment = all(len(current) <= 4 for current in address_list)

        if is_valid and valid_segment and len(address_list) == 8:
            return True
        else:
            return False


class IP(String):
    """
    An Internet Protocol address (IP address) is a numerical label assigned to each device connected to a computer network that uses the Internet Protocol for communication.
    
    An IP address serves two principal functions: host or network interface identification and location addressing.

    Valid IP could be either IPv4 ~~or IPv6~~
    """
    validation_text = "Expected an IP address"

    def do_check(self, value, path):
        return IPv4().do_check(value, path)  # or IPv6().do_check(value, path)


class Domain(String):
    """
    The definitive descriptions of the rules for forming domain names appear in [RFC 1035](https://tools.ietf.org/html/rfc1035), [RFC 1123](https://tools.ietf.org/html/rfc1123), and [RFC 2181](https://tools.ietf.org/html/rfc2181). A domain name consists of one or more parts, technically called labels, that are conventionally concatenated, and delimited by dots, such as `example.com`.

    The right-most label conveys the top-level domain; for example, the domain name `www.example.com` belongs to the top-level domain `com`.

    The hierarchy of domains descends from right to left; each label to the left specifies a subdivision, or subdomain of the domain to the right. For example, the label example specifies a subdomain of the com domain, and www is a subdomain of example.com. 
    This tree of subdivisions may have up to 127 levels.

    A label may contain zero to 63 characters. The null label, of length zero, is reserved for the root zone. 
    The full domain name may not exceed the length of 253 characters in its textual representation.In the internal binary representation of the DNS the maximum length requires 255 octets of storage, as it also stores the length of the name.

    Although no technical limitation exists to use any character in domain name labels which are representable by an octet, hostnames use a preferred format and character set. 
    The characters allowed in labels are a subset of the ASCII character set, consisting of characters a through z, A through Z, digits 0 through 9, and hyphen. 
    This rule is known as the LDH rule (letters, digits, hyphen). 
    Domain names are interpreted in case-independent manner. 
    Labels may not start or end with a hyphen. An additional rule requires that top-level domain names should not be all-numeric.[20]
    """
    validation_text = "Expected a domain name"

    def do_check(self, value, path):
        if not String.do_check(self, value, path):
            return False
        if IPv4().do_check(value, path):
            return True
        if value == 'localhost':
            return True
        dm = value.split('.')
        if len(dm) < 2:
            return False
        if all(map(lambda x: x.isdigit(), dm)):
            return False
        def comp_ok(x):
            if x == '' or x.strip('abcdefghijklmnopqrstuvwxyz-0123456789') != '':
                return False
            if x.startswith('-') or x.endswith('-'):
                return False
            return True
        return all(map(comp_ok, dm))


class Identifier(String):
    """
    An Identifier should be shorter than 253 chars and lc alphanum or . or -
    """
    validation_text = "Identifiers should be <253 chars and lc alphanum or . or -"

    def do_check(self, value, path):
        if not String.do_check(self, value, path):
            return False
        id_chars = 'abcdefghijklmnopqrstuvwxyz0123456789.-'
        if len(value) == 0 or len(value) > 253:
            return False
        for v in value:
            if v not in id_chars:
                return False
        return True


class CaseIdentifier(Identifier):
    """
    An Identifier should be shorten thsn 253 chars and alphanum or . or -
    """
    validation_text = "Identifiers should be <253 chars and alphanum or . or -"

    def do_check(self, value, path):
        if not String.do_check(self, value, path):
            return False
        id_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.-'
        if len(value) == 0 or len(value) > 253:
            return False
        for v in value:
            if v not in id_chars:
                return False
        return True


class SystemIdentifier(Identifier):
    """
    An Identifier should be  shorten than 253 chars and lc alphanum or . or - or :
    """
    validation_text = "Identifiers should be <253 chars and lc alphanum or . or - or :"

    def do_check(self, value, path):
        if not String.do_check(self, value, path):
            return False

        if value.startswith('system:'):
            id_chars = 'abcdefghijklmnopqrstuvwxyz0123456789.-:'
        else:
            id_chars = 'abcdefghijklmnopqrstuvwxyz0123456789.-'

        if len(value) == 0 or len(value) > 253:
            return False
        for v in value:
            if v not in id_chars:
                return False
        return True


class ColonIdentifier(Identifier):
    """
    An Identifier should be  shorten than 253 chars and lc alphanum or . or - or :
    """
    validation_text = "Identifiers should be <253 chars and lc alphanum or . or - and a :"

    def do_check(self, value, path):
        if not String.do_check(self, value, path):
            return False

        if len(value.split(':')) != 2:
            return False

        id_chars = 'abcdefghijklmnopqrstuvwxyz0123456789.-:'

        if len(value) == 0 or len(value) > 253:
            return False
        for v in value:
            if v not in id_chars:
                return False
        return True


class ARN(String):
    """
    Amazon Resource Names (ARNs) uniquely identify AWS resources.

    The following are the general formats for ARNs; the specific components and values used depend on the AWS service.
    
    ```
    arn:partition:service:region:account-id:resource
    arn:partition:service:region:account-id:resourcetype/resource
    arn:partition:service:region:account-id:resourcetype:resource
    ```
    
    **partition**

    The partition that the resource is in. For standard AWS regions, the partition is aws. If you have resources in other partitions, the partition is aws-partitionname. For example, the partition for resources in the China (Beijing) region is aws-cn.
    
    **service**

    The service namespace that identifies the AWS product (for example, Amazon S3, IAM, or Amazon RDS). For a list of namespaces, see AWS Service Namespaces.
    
    **region**
    
    The region the resource resides in. Note that the ARNs for some resources do not require a region, so this component might be omitted.
    
    **account**
    
    The ID of the AWS account that owns the resource, without the hyphens. For example, 123456789012. Note that the ARNs for some resources don't require an account number, so this component might be omitted.
    
    **resource, resourcetype:resource, or resourcetype/resource**
    
    The content of this part of the ARN varies by service. It often includes an indicator of the type of resource—for example, an IAM user or Amazon RDS database —followed by a slash (/) or a colon (:), followed by the resource name itself. Some services allow paths for resource names, as described in Paths in ARNs.
    """

    validation_text = "Amazon ARNs start with arn:aws:..."

    def do_check(self, value, path):
        if not String.do_check(self, value, path):
            return False
        if not value.startswith('arn:aws:') and not value.startswith('arn:aws-'):
            return False
        return True


class Path(String):
    """
    A path, the general form of the name of a file or directory, specifies a unique location in a file system. 
    A path points to a file system location by following the directory tree hierarchy expressed in a string of characters in which path components, separated by a delimiting character, represent each directory. 
    The delimiting character is most commonly the slash ("/"), the backslash character ("\"), or colon (":"), though some operating systems may use a different delimiter. 
    Paths are used extensively in computer science to represent the directory/file relationships common in modern operating systems, and are essential in the construction of Uniform Resource Locators (URLs). 
    Resources can be represented by either absolute or relative paths.

    More info could be fount [here](https://en.wikipedia.org/wiki/Path_(computing))
    """
    validation_text = "Expecting a fully qualified path"

    def do_check(self, value, path):
        if not String.do_check(self, value, path):
            return False
        return value == '' or value.startswith('/')


class NonEmpty(KubeType):
    """
    This wrapper is ensuring that a field could not be left empty but needs to have a valid value.
    """
    validation_text = "Expecting non-empty"

    wrapper = True

    def do_check(self, value, path):
        return self.check_wrap(value, path) and len(value) != 0


class OneOf(KubeType):
    """
    This wrapper is defininig the possibility for a field to be either multiple types.
    """
    def __init__(self, *types):
        assert len(types) > 1
        self.types = list(map(self.__class__.construct_arg, types))

    def name(self, md=False):
        if md:
            return '[{}](#{})<{}>'.format(self.__class__.__name__, self.__class__.__name__.lower(), ', '.join(map(lambda x: x.name(md=True), self.types)))
        return self.__class__.__name__ + '<' + ', '.join(map(lambda x: x.name(), self.types)) + '>'

    def original_type(self):
        # XXX this becomes complicated to do - for the moment assume none
        return None

    def check(self, value, path=None):
        if path is None:
            path = 'self'

        for t in self.types:
            try:
                if t.check(value, path):
                    return True
            except UserError as e:
                if not isinstance(e.exc, KubeTypeValidationError):
                    raise
            except KubeTypeValidationError:
                pass
        raise UserError(KubeTypeValidationError(value, self.name(), path,
                                                "couldn't match any possible types"))


class List(KubeType):
    """
    This field is enforcing a check to a field to determinate if a list was actually provided as parameter.
    """
    validation_text = "Expecting list"

    wrapper = True

    def original_type(self):
        t = self.wrap.original_type()
        if t is not None:
            return [t]
        return None

    def do_check(self, value, path):
        if not isinstance(value, (list, tuple)):
            return False

        count = 0
        for v in value:
            if not self.check_wrap(v, path="{}[{:d}]".format(path, count)):
                return False
            count += 1

        return True


class Map(KubeType):
    """
    Enforce a Map to be composed by pre-defined types specified on the initialization.

    **Esample:**

    `Map(String, String)`
    `Map(Int, String)`
    `Map(Int, Int)`

    This will allow to perform some authomatic checks inside the imput of an Object
    """
    def __init__(self, key, value):
        self.key = self.__class__.construct_arg(key)
        self.value = self.__class__.construct_arg(value)

    def name(self, md=False):
        if md:
            return '[{}](#{})<{}, {}>'.format(self.__class__.__name__, self.__class__.__name__.lower(), self.key.name(md=True), self.value.name(md=True))
        return '{}<{}, {}>'.format(self.__class__.__name__, self.key.name(), self.value.name())

    def original_type(self):
        t = self.value.original_type()
        if t is not None:
            return {'value': t}
        return None

    def check(self, value, path=None):
        if not isinstance(value, dict):
            raise UserError(KubeTypeValidationError(value, self.name(), path, "not a dictionary"))

        if path is None:
            path = 'self'

        for k in value.keys():
            self.key.check(k, path='{}[{}] (key)'.format(path, k))
            self.value.check(value[k], path='{}[{}]'.format(path, k))

        return True
