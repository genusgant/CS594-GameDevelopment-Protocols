from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseReady(ServerResponse):

    def execute(self, conn, data):

        try:
            self.msg = data.getString()

            print "ResponseReady - ", self.msg

            #self.log('Received [' + str(Constants.SMSG_READY) + '] String Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_READY) + '] String Response')
            print_exc()
