from yowsup.layers.interface                           import YowInterfaceLayer, ProtocolEntityCallback
from yowsup.layers.protocol_messages.protocolentities  import TextMessageProtocolEntity
from yowsup.layers.protocol_receipts.protocolentities  import OutgoingReceiptProtocolEntity
from yowsup.layers.protocol_acks.protocolentities      import OutgoingAckProtocolEntity

import time
import datetime
import json
import unirest


# word input
wordmeaning = '';

class EchoLayer(YowInterfaceLayer):

    @ProtocolEntityCallback("message")
    def onMessage(self, messageProtocolEntity):
        #send receipt otherwise we keep receiving the same message over and over

        if True:
            receipt = OutgoingReceiptProtocolEntity(messageProtocolEntity.getId(), messageProtocolEntity.getFrom())

            wordmeaning = messageProtocolEntity.getBody().lower()
            response = self.GetMeaning(wordmeaning)
            
            outgoingMessageProtocolEntity = TextMessageProtocolEntity(
                response,
                to = messageProtocolEntity.getFrom())

            self.toLower(receipt)
            self.toLower(outgoingMessageProtocolEntity)

    @ProtocolEntityCallback("receipt")
    def onReceipt(self, entity):
        ack = OutgoingAckProtocolEntity(entity.getId(), "receipt", "delivery")
        self.toLower(ack)

    def GetMeaning(pWord):

        # Get current time
        current_time = int(time.time())

        # These code snippets use an open-source library.
        response = unirest.get("https://montanaflynn-dictionary.p.mashape.com/define?word=hello",
            headers={
                "X-Mashape-Key": "j6rDcjfVcVmshxp0Y102O2cL6vDrp16mL1FjsnsgRqpcl6fC3L",
                "Accept": "application/json"
            }
        )

            data = json.dumps(response.body, separators=(',',':'))
            meaning = json.loads(data)

            current_s = ''

            for pword in meaning :

                if match['srsid'] == WORLDCUP_ID :
                
                    if match['header']['mchState'] == 'inprogress' or match['header']['mchState'] == 'complete' :

                        bat_id = match['miniscore']['batteamid']
                        bowl_id = match['miniscore']['bowlteamid']

                        if match['team1']['id'] == bat_id :
                            bat_name = match['team1']['sName']
                            bowl_name = match['team2']['sName']
                        else :
                            bat_name = match['team2']['sName']
                            bowl_name = match['team1']['sName']

                        score_head = match['header']['mnum']

                        batting_score = str(bat_name) + ' ' + match['miniscore']['batteamscore'] + '(' + match['miniscore']['overs'] + ')'

                        summary = match['miniscore']['striker']['fullName'] + ' ' + match['miniscore']['striker']['runs'] + '(' + match['miniscore']['striker']['balls'] + ')' + ', ' + match['miniscore']['nonStriker']['fullName'] + ' ' + match['miniscore']['nonStriker']['runs'] + '(' + match['miniscore']['nonStriker']['balls'] + ')'

                        bowl_score = match['miniscore']['bowlteamscore'] + ' ' + str(bowl_name)

                        status = match['header']['status']

                        score = score_head + ': ' + batting_score + ' v ' + bowl_score + ', ' + summary + ', ' + status

                        current_s = current_s + score + '\n'

            current_score[1] = current_s

        # Create Text response
        text_response = current_score[1]

        #Return details
        return text_response





        
