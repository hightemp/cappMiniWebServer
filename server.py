#!/usr/bin/python
# encoding: UTF8

from gevent import monkey; monkey.patch_all()
from gevent.pywsgi import WSGIServer
from threading import *
import os
from os.path import *
import re
from requests.compat import urljoin, quote_plus
from urlparse import *

import settings

class TaskThread(Thread):

    bPaused = False
    bActive = True

    def run(self):
        while (self.bActive):
            while (not self.bPaused):
                self.task()

    def start(self):
        self.bPaused = False
        self.bActive = True

    def stop(self):
        self.bPaused = True
        self.bActive = False

    def pause(self):
        self.bPaused = True

    def task(self):
        pass

class HTTPServer(object):
    aHeaders = [('Content-Type', 'text/html'), ('Cache-control', 'no-cache')]
    dVariables = {}
    aAccessDirectories = ['assets', 'temporary']
    sTasksDir = 'tasks'
    sTemplatesDir = 'templates'
    sAssetsDir = 'assets'
    sTemporaryDir = 'temporary'
    sHost = ''
    iPort = 8080
    aTasks = []

    # dir(HTTPServer)

    def __init__(self,
                 in_sHost='127.0.0.1',
                 in_iPort=8080):

        self.dSettings = settings.gdSettings

        for sKey, objValue in self.dSettings.iteritems():
            if self.dSettings[sKey] != None:
                if len(self.dSettings[sKey]) > 0:
                    self.__setattr__(sKey, self.dSettings[sKey])

        self.sRootPath = os.path.dirname(os.path.abspath(__file__))

        self.sTasksPath = join(self.sRootPath, self.sTasksDir)

        for os.listdir()
            aTasks

        self.sTemplatePath = join(self.sRootPath, self.sTemplatesDir)
        self.sAssetsPath = join(self.sRootPath, self.sAssetsDir)
        self.sTemporaryPath = join(self.sRootPath, self.sTemporaryDir)

        self.sHost = in_sHost
        self.iPort = in_iPort

        WSGIServer("%s:%d" % (in_sHost, in_iPort), self.fnResponse).serve_forever()

    def fnGetHostURL(self,
                     sPath=''):

        objPath = urlsplit("http://%s:%d" % (self.sHost, self.iPort))
        sURL = os.path.join(objPath.geturl(), sPath)

        return sURL

    def fnReadTemplate(self,
                       in_sTemplateName):

        sResult = ''

        objReadFileHandler = file(join(self.sTemplatePath, in_sTemplateName), "r")
        sResult = objReadFileHandler.read()
        objReadFileHandler.close()

        return sResult

    def fnSetVariablesInTemplate(self, sVariableName):

        return sVariableName

    def fnSendPage(self,
                   in_sCode='200 OK',
                   in_aHeaders=[('Content-Type', 'text/html')],
                   in_sTemplateName="index.html",
                   in_sController="index.py"):

        sResult = [in_sCode, in_aHeaders, '']

        try:
            sResult[2] = self.fnReadTemplate(in_sTemplateName)

            sResult[2] = re.sub(r'\<\?=([A-Z0-9_-]+?)\?\>', self.fnSetVariblesInTemplate, sResult[2])
        except Exception as objException:
            print("[E] %s" % objException)
            sResult[0] = '404 Not found'
            sResult[2] = self.fnReadTemplate(self.dSettings['dTemplates']["error"])

        return sResult

    def fnMatchItemsByMask(self,
                           in_sText,
                           in_dDictonary):

        objResult = []

        for sKey, objValue in in_dDictonary.iteritems():
            sMask = sKey
            sMask = re.escape(sMask)
            sMask = re.sub(r'\\[*]', r'.*?', sMask)
            sMask = re.sub(r'\\[?]', r'.{1,1}', sMask)
            aMatches = re.match(sMask, in_sText)

            if aMatches is not None:
                objResult.append(objValue)

        return objResult

    def fnResponse(self,
                   in_aEnv,
                   in_objResponse):
        aResult = []
        sHTTPHeader = '200 OK'
        aHeaders = self.aHeaders

        try:
            sHost    = in_aEnv['HTTP_HOST']
            sMethod  = in_aEnv['REQUEST_METHOD']
            sPath    = in_aEnv['PATH_INFO']

            aMatchRouterResult = self.fnMatchItemsByMask(sPath, self.dSettings['dRouter'])

            if len(aMatchResult) > 0:
                sLocation = self.fnGetHostURL(aMatchRouterResult[0])
                sHTTPHeader = '301 Moved Permanently'
                aHeaders = [('Location', sLocation)]
            else:
                aMatchControllersResult = self.fnMatchItemsByMask(sPath, self.dSettings['dControlers'])
                aMatchTemplatesResult = self.fnMatchItemsByMask(sPath, self.dSettings['dTemplates'])
                aResult = fnSendPage()

            # if (sPath):
            # fnSendHTMLPage()

            # print self.fnMatchItemsByMask(sPath, self.dSettings['dControlers'])
        except Exception as objException:
            print objException

        in_objResponse(sHTTPHeader, aHeaders)
        return aResult

if __name__ == "__main__":
    HTTPServer(in_iPort=8089)