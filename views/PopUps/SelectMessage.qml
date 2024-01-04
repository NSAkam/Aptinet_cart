import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15
import QtQuick.Window 2.0
import "../Components"
import "../Containers"
import "../Utiles"

Popup {
    property string message: "message"
    property bool showEnterBarcode: false
    id: root
    width: 1280
    height: 800
    modal: true
    focus: true

    signal ok()

    background:
        Rectangle {
        id:rectContainer
        anchors.fill: parent
        color: "#191641"
        opacity: 0.5
    }

    Image {
        source: "../Assets/Notification.png"
        width: 57
        height: 57
        x:1208
        y:25
        MouseArea{
            anchors.fill: parent
            onClicked: {
                obj_LogicContainerShop.shopPage.call_forHelpClicked()
            }
        }
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

        Image {
            source: "../../Assets/popupwarning.png"
            width: 99
            height: 88
            y: 48
            anchors.horizontalCenter: parent.horizontalCenter
        }

        Text {
            id: notiftext
            text: root.message
            anchors.horizontalCenter: parent.horizontalCenter
            horizontalAlignment: Text.AlignHCenter
            y: 168
            color: "black"
            font.pixelSize: 24
            wrapMode: Text.WordWrap
            width: 300
            //height: 500
            //            font.letterSpacing: 0.8
        }
        ViewSettings{
            id:viewset
        }

        Row{
            spacing: 10
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.topMargin: 5
            anchors.top: notiftext.bottom
            KButton{
                borderRadius: 5
                height: 75
                text: "No"
                onClicked: root.close()
            }
            KButton{
                borderRadius: 5
                height: 75
                text: "Yes"
                onClicked: {
                    root.ok()
                }
            }
        }


    }

}
