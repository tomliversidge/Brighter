#!/usr/bin/env python
""""
File         : kombu_messaging.py
Author           : ian
Created          : 09-28-2016

Last Modified By : ian
Last Modified On : 09-28-2016
***********************************************************************
The MIT License (MIT)
Copyright © 2016 Ian Cooper <ian_hammond_cooper@yahoo.co.uk>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
**********************************************************************i*
"""
from kombu.message import Message as KombuMessage
from core.messaging import Message, MessageHeader, MessageBody, MessageType
from uuid import UUID, uuid4


class ReadError:
    pass


class KombuMessageFactory:
    """
    The message factory turn an 'on-the-wire' message into our internal representation. We try to be as
    tolerant as possible (following Postel's Law: https://en.wikipedia.org/wiki/Robustness_principle) Be conservative
    in what you do, be liberal in what you accept
    """

    def create_message(self, message: KombuMessage) -> Message:

        def _get_correlation_id() -> UUID:
            pass

        def _get_message_type() -> MessageType:
            pass

        def _get_payload() -> str:
            pass

        def _get_payload_type() -> str:
            pass

        def _getTopic() -> str:
            pass

        id = uuid4()
        topic = _getTopic()
        message_type = _get_message_type()
        correlation_id = _get_correlation_id()
        payload = _get_payload()
        payload_type = _get_payload_type()

        message_header = MessageHeader(identity=id, topic=topic, message_type=message_type,
                correlation_id=correlation_id, content_type=type)

        message_body =  MessageBody(body=payload, body_type=payload_type)

        return Message(message_header, message_body)

    def _read_header(self, header_key: str, message: KombuMessage) -> (str, ReadError):
        pass

