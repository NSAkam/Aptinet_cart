import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15
import QtQuick.Window 2.0
import QtQuick.Controls.Styles 1.4
import "Components"
import "Containers"
import "Utiles" as Util


Item {

    width: 1280
    height: 800

    Util.ViewSettings{
        id:viewset
    }

    Image {
        source: "../Assets/AuthenticationBackground.png"
        anchors.fill: parent
    }

    Rectangle {
        color: "#A37A544D"
        anchors.fill: parent
        opacity: 0.3
    }

    Rectangle{
        width: parent.width
        height: 92
        x:0
        y:0
    }

    Item{
        id:topPanel
        width: parent.width
        height: 92
        Rectangle{
            width: parent.width
            height: parent.height
            x:0
            y:0
            Rectangle{
                width: 50
                height: 50
                color: viewset.primaryColor
                x:530 + 390
                y:24
                radius: width /2
            }
            Text {
                text: qsTr("user Email")
                color: "#6D6D6D"
                width: 148
                height: 15
                font.pixelSize: 14
                x:586 + 390
                y:40.5
            }
            Image {
                source: "../Assets/Help.png"
                width: 57
                height: 57
                x:1156
                y:25
            }
            Image {
                source: "../Assets/Notification.png"
                width: 57
                height: 57
                x:1208
                y:25
            }

        }
    }

    Item{
        id:leftPanel
        width: 390
        height: parent.height

        Rectangle {
            id:rect_leftPanel
            color: "white"
            width: 390
            height: 92
            x: 0
            y: 0

        }

        Image {
            source: "../Assets/AptinetText.png"
            x:0
            y:0
        }
    }

    Image {
        source: "../Assets/payment_animation.png"
        x: 498
        y: 185 + topPanel.height
    }

    Text {
        text: "<font color='#1D1D1D'>Please hold your phone</font><font color='" + viewset.primaryColor + "'> near the display<br></font><font color='#1D1D1D'>until you see a check mark</font>"
        font.pixelSize: 32
        y: 348 + topPanel.height
        x: 314
        font.bold: true
        horizontalAlignment: Text.AlignHCenter
    }

    Image {
        source: "../Assets/ApplePay.png"
        x: 522
        y: 550 + topPanel.height
    }

    Image {
        source: "../Assets/GooglePay.png"
        x: 672
        y: 550 + topPanel.height
    }

    Text {
        text: qsTr("What are NFC payments? NFC technology powers contactless payments via mobile wallets\n\n like Apple Pay and Google Pay, as well as contactless cards.")
        x: 292
        y: 612 + topPanel.height
        font.pixelSize: 16
        color: "#6D6D6D"
        horizontalAlignment: Text.AlignHCenter
    }




}
