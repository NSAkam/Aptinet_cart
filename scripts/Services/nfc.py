from smartcard.CardRequest import CardRequest
from smartcard.Exceptions import CardRequestTimeoutException
from smartcard.CardType import AnyCardType
from smartcard import util


# respond to the insertion of any type of smart card
card_type = AnyCardType()

# create the request. Wait for up to x seconds for a card to be attached
request = CardRequest(timeout=0, cardType=card_type)
hasopened = False

while True:
    # listen for the card
    service = None
    try:
        service = request.waitforcard()
    except CardRequestTimeoutException:
        print("ERROR: No card detected")


    # could add "exit(-1)" to make code terminate

    # when a card is attached, open a connection
    try:
        conn = service.connection
        conn.connect()

        # get the ATR and UID of the card
        get_uid = util.toBytes("FF CA 00 00 00")
        data, sw1, sw2 = conn.transmit(get_uid)
        uid = util.toHexString(data)
        status = util.toHexString([sw1, sw2])

        # print the ATR and UID of the card
        if conn and not hasopened:
            print("ATR = {}".format(util.toHexString(conn.getATR())))
            print("UID = {}\tstatus = {}".format(uid, status))
           

            hasopened=True
    except:
        print("no connection")