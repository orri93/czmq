################################################################################
#  THIS FILE IS 100% GENERATED BY ZPROJECT; DO NOT EDIT EXCEPT EXPERIMENTALLY  #
#  Read the zproject/README.md for information about making permanent changes. #
################################################################################
from . import utils
from . import destructors
libczmq_destructors = destructors.lib

class Zstr(object):
    """
    sending and receiving strings
    """

    @staticmethod
    def recv(source):
        """
        Receive C string from socket. Caller must free returned string using
        zstr_free(). Returns NULL if the context is being terminated or the
        process was interrupted.
        """
        return utils.lib.zstr_recv(source._p)

    @staticmethod
    def recvx(source, string_p, *string_p_args):
        """
        Receive a series of strings (until NULL) from multipart data.
        Each string is allocated and filled with string data; if there
        are not enough frames, unallocated strings are set to NULL.
        Returns -1 if the message could not be read, else returns the
        number of strings filled, zero or more. Free each returned string
        using zstr_free(). If not enough strings are provided, remaining
        multipart frames in the message are dropped.
        """
        return utils.lib.zstr_recvx(source._p, utils.to_bytes(string_p), *string_p_args)

    @staticmethod
    def recv_compress(source):
        """
        De-compress and receive C string from socket, received as a message
        with two frames: size of the uncompressed string, and the string itself.
        Caller must free returned string using zstr_free(). Returns NULL if the
        context is being terminated or the process was interrupted.
        """
        return utils.lib.zstr_recv_compress(source._p)

    @staticmethod
    def send(dest, string):
        """
        Send a C string to a socket, as a frame. The string is sent without
        trailing null byte; to read this you can use zstr_recv, or a similar
        method that adds a null terminator on the received string. String
        may be NULL, which is sent as "".
        """
        return utils.lib.zstr_send(dest._p, utils.to_bytes(string))

    @staticmethod
    def sendm(dest, string):
        """
        Send a C string to a socket, as zstr_send(), with a MORE flag, so that
        you can send further strings in the same multi-part message.
        """
        return utils.lib.zstr_sendm(dest._p, utils.to_bytes(string))

    @staticmethod
    def sendf(dest, format, *format_args):
        """
        Send a formatted string to a socket. Note that you should NOT use
        user-supplied strings in the format (they may contain '%' which
        will create security holes).
        """
        return utils.lib.zstr_sendf(dest._p, format, *format_args)

    @staticmethod
    def sendfm(dest, format, *format_args):
        """
        Send a formatted string to a socket, as for zstr_sendf(), with a
        MORE flag, so that you can send further strings in the same multi-part
        message.
        """
        return utils.lib.zstr_sendfm(dest._p, format, *format_args)

    @staticmethod
    def sendx(dest, string, *string_args):
        """
        Send a series of strings (until NULL) as multipart data
        Returns 0 if the strings could be sent OK, or -1 on error.
        """
        return utils.lib.zstr_sendx(dest._p, utils.to_bytes(string), *string_args)

    @staticmethod
    def send_compress(dest, string):
        """
        Compress and send a C string to a socket, as a message with two frames:
        size of the uncompressed string, and the string itself. The string is
        sent without trailing null byte; to read this you can use
        zstr_recv_compress, or a similar method that de-compresses and adds a
        null terminator on the received string.
        """
        return utils.lib.zstr_send_compress(dest._p, utils.to_bytes(string))

    @staticmethod
    def sendm_compress(dest, string):
        """
        Compress and send a C string to a socket, as zstr_send_compress(),
        with a MORE flag, so that you can send further strings in the same
        multi-part message.
        """
        return utils.lib.zstr_sendm_compress(dest._p, utils.to_bytes(string))

    @staticmethod
    def str(source):
        """
        Accepts a void pointer and returns a fresh character string. If source
        is null, returns an empty string.
        """
        return utils.lib.zstr_str(source._p)

    @staticmethod
    def free(string_p):
        """
        Free a provided string, and nullify the parent pointer. Safe to call on
        a null pointer.
        """
        utils.lib.zstr_free(utils.to_bytes(string_p))

    @staticmethod
    def test(verbose):
        """
        Self test of this class.
        """
        utils.lib.zstr_test(verbose)

################################################################################
#  THIS FILE IS 100% GENERATED BY ZPROJECT; DO NOT EDIT EXCEPT EXPERIMENTALLY  #
#  Read the zproject/README.md for information about making permanent changes. #
################################################################################
