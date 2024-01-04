import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15
import QtQuick.Window 2.0
import "../Components"
import "../Containers"
import "../Utiles"
import KAST.Logic 1.0


Popup {
    property Logic obj_logic


    property bool showEnterBarcode: false
    id: root
    width: 1280
    height: 800
    modal: true
    focus: true

    signal phoneNumber()
    signal memberShopCart()


    background:
        Rectangle {
        id:rectContainer
        anchors.fill: parent
        color: "#191641"
        opacity: 0.5
    }

    KButton {
        visible:showEnterBarcode
        x: 630 + 390
        y: 32
        borderRadius: 4
        width: 164
        height: 40

        Text {
            text: "+  Enter Barcode"
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter
            font.pixelSize: 16
            font.weight: Font.DemiBold
            color: "white"
        }
    }

    Rectangle {
        id: notifrect
        width: 700
        height: 300
        radius: 4
        y: 274
        //        x: 106 + 390/2
        anchors.horizontalCenter: parent.horizontalCenter




        ViewSettings{
            id:viewset
        }

        Column{
            y:10
            spacing: 10
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.topMargin: 5
            anchors.top: notiftext.bottom
            KButton{
                borderRadius: 5
                height: 75
                text: obj_logic.lang.btn_Enter_Phone_Number
                onClicked: {
                    root.phoneNumber()
                }
            }
            KButton{
                borderRadius: 5
                height: 75
                text: obj_logic.lang.btn_Scan_MemberShop_Cart
                onClicked: {
                    root.memberShopCart()
                }
            }
            KButton{
                borderRadius: 5
                height: 75
                text: "Close"
                onClicked: {
                    root.close()
                }
            }
        }
    }

}
