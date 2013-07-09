from CRABClient.Commands.SubCommand import SubCommand
from CRABClient.ServerInteractions import HTTPRequests
from CRABClient.client_exceptions import RESTCommunicationException

import urllib

class kill(SubCommand):

    visible = True

    def __call__(self):
        if self.options.objects == 'jobs':
            server = HTTPRequests(self.serverurl, self.proxyfilename)
            self.logger.debug('Killing task %s' % self.cachedinfo['RequestName'])
            dictresult, status, reason = server.delete(self.uri, data = urllib.urlencode({ 'workflow' : self.cachedinfo['RequestName'], 'ASO': 0}))
            self.logger.debug("Result: %s" % dictresult)
            if status != 200:
                msg = "Problem killing task %s:\ninput:%s\noutput:%s\nreason:%s" % \
                        (self.cachedinfo['RequestName'], str(self.cachedinfo['RequestName']), str(dictresult), str(reason))
                raise RESTCommunicationException(msg)
            self.logger.info("Task killed")
        if self.options.objects == 'files':
            server = HTTPRequests(self.serverurl, self.proxyfilename)
            self.logger.debug('Killing workflow %s' % self.cachedinfo['RequestName'])
            dictresult, status, reason = server.delete(self.uri, data = urllib.urlencode({ 'workflow' : self.cachedinfo['RequestName'], 'ASO':1 }))
            self.logger.debug("Result: %s" % dictresult)
            if status != 200:
                msg = "Problem killing task %s:\ninput:%s\noutput:%s\nreason:%s" % \
                       (self.cachedinfo['RequestName'], str(self.cachedinfo['RequestName']), str(dictresult), str(reason))
                raise RESTCommunicationException(msg)
            self.logger.info("Task killed")

    def setOptions(self):
        """
        __setOptions__

        This allows to set specific command options
        """

        self.parser.add_option( "-o", "--objects",
                                 dest = "objects",
                                 type   = 'str',
                                 default = 'jobs',
                                 help = "-o files to kill transfering files. Default -o jobs"
                                 )


