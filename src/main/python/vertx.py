# Copyright 2011 the original author or authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

""" 
This module provides the entry point to the vert.x platform 
"""

import org.vertx.java.deploy.impl.VertxLocator
from core.http import HttpServer, HttpClient
from core.net import NetServer, NetClient
from core.sock_js import SockJSServer

__author__ = "Scott Horn"
__email__ = "scott@hornmicro.com"

def create_http_server(**kwargs):
    """ Return a HttpServer """
    return HttpServer(**kwargs)

def create_http_client(**kwargs):
    """ Return a HttpClient """
    return HttpClient(**kwargs)

def create_net_server(**kwargs):
    """ Return a NetServer """
    return NetServer(**kwargs)

def create_net_client(**kwargs):
    """ Return a NetClient """
    return NetClient(**kwargs)

def create_sockjs_server(http_server):
    """ Return a SockJSServer """
    return SockJSServer(http_server)

def get_logger():
    """ Get the logger for the verticle"""
    return org.vertx.java.deploy.impl.VertxLocator.container.getLogger()