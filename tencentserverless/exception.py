#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
scf
~~~~~~~~~~~~~~
This module is exception of scf api
"""

import sys


class TencentServerlessSDKException(Exception):
    """tencentserverlessapi sdk 异常类"""

    def __init__(self, code=None, message=None, request_id=None,
                 response=None, stack_trace=''):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.response = response
        self.stack_trace = stack_trace

    def __str__(self):
        message = "[TencentServerlessSDKException] \ncode:%s \nmessage:%s " \
            "\nstack_trace:%s \nrequestId:%s" % (self.code, self.message,
                                                 self.stack_trace, self.request_id)
        if sys.version_info[0] < 3 and isinstance(message, unicode):
            return message.encode("utf8")
        else:
            return message

    def get_code(self):
        """
        get_code
        ~~~~~~~~~~~~~~
        :return: code
        """
        return self.code

    def get_message(self):
        """
        get_message
        ~~~~~~~~~~~~~~
        :return: message
        """
        return self.message

    def get_request_id(self):
        """
        get_message
        ~~~~~~~~~~~~~~
        :return: request_id
        """
        return self.request_id

    def get_stack_trace(self):
        """
        get_message
        ~~~~~~~~~~~~~~
        :return: stack_trace
        """
        return self.stack_trace

    def get_response(self):
        """
        get_message
        ~~~~~~~~~~~~~~
        :return: response
        """
        return self.response
