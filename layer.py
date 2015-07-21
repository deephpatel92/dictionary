from yowsup.layers.interface                           import YowInterfaceLayer, ProtocolEntityCallback
from yowsup.layers.protocol_messages.protocolentities  import TextMessageProtocolEntity
from yowsup.layers.protocol_receipts.protocolentities  import OutgoingReceiptProtocolEntity
from yowsup.layers.protocol_acks.protocolentities      import OutgoingAckProtocolEntity

import time
import datetime
import json
import unirest


class EchoLayer(YowInterfaceLayer):

    @ProtocolEntityCallback("message")
    def onMessage(self, messageProtocolEntity):
        #send receipt otherwise we keep receiving the same message over and over

        if True:
            receipt = OutgoingReceiptProtocolEntity(messageProtocolEntity.getId(), messageProtocolEntity.getFrom())

        print messageProtocolEntity.getFrom();

        wordformean = messageProtocolEntity.getBody().lower()
        response = self.dictionaryword(wordformean)

        phone =  messageProtocolEntity.getFrom()

        if '@' in phone:
            outgoingMessageProtocolEntity = TextMessageProtocolEntity(message, to = phone)
        elif '-' in phone:
            outgoingMessageProtocolEntity = TextMessageProtocolEntity(message, to = "%s@g.us" % phone)
        else:
            outgoingMessageProtocolEntity = TextMessageProtocolEntity(message, to = "%s@s.whatsapp.net" % phone)

        self.toLower(receipt)
        self.toLower(outgoingMessageProtocolEntity)

    @ProtocolEntityCallback("receipt")
    def onReceipt(self, entity):
        ack = OutgoingAckProtocolEntity(entity.getId(), "receipt", "delivery", entity.getFrom())
        self.toLower(ack)

    def dictionaryword(self, word):

        url = "https://montanaflynn-dictionary.p.mashape.com/define?word=" + word

        # These code snippets use an open-source library.
        response = unirest.get(url,
            headers={
                "X-Mashape-Key": "j6rDcjfVcVmshxp0Y102O2cL6vDrp16mL1FjsnsgRqpcl6fC3L",
                "Accept": "application/json"
            }
        )
        
        
        resp = word + '\n\n'
        
        if ' ' in word:
                text_response = "Dictionary word does not allow 'Space'"
        else:

            data = json.dumps(response.body, separators=(',',':'))
            meanings = (json.loads(data))["definitions"]
        
            count = 0
            for meaning in meanings:
                count = count + 1
                resp = resp + 'm' + str(count) +' : ' + str(meaning["text"].encode('ascii', 'ignore')) + '\n\n'

            # Create Text response
            text_response = str(resp)

        #Return details
        return str(text_response)
