import QtQuick 2.12
import QtGraphicalEffects 1.0
import QtQuick.Window 2.12
import QtQuick.Controls 2.12
import "../Utiles"
import "../Components"
import KAST.Logic 1.0

Popup {
    id: popup_SetPasssword
    property Logic setting_obj
    ViewSettings{
        id:viewset
    }

    width: 1280
    height: 800
    modal: true
    focus: true

    closePolicy: Popup.CloseOnEscape | Popup.CloseOnPressOutside
    background: Rectangle {
        implicitWidth: 725
        implicitHeight: 269
        radius:10
        color: "#191641"
        opacity: 0.5
    }
    contentItem: Item {
        id:container
        Rectangle{
            width: 725
            height: 269
            radius: 4
            anchors.horizontalCenter: parent.horizontalCenter
            y:140
            color: "white"

            Text {
                text: qsTr("Enter the Password for “ WifiName-2 ”")
                anchors.horizontalCenter: parent.horizontalCenter
                y:24
                font.pixelSize: 16
            }
            Text {
                text: qsTr("enter Password")
                font.pixelSize: 24
                font.bold: true
                anchors.horizontalCenter: parent.horizontalCenter
                y:65
            }

            Text {
                text: qsTr("Cancel")
                y:64
                x:32
                font.pixelSize: 24
                color: "gray"
                MouseArea{
                    anchors.fill: parent
                    onClicked: {
                        popup_SetPasssword.close()
                    }
                }
            }
            Text {
                text: qsTr("Join")
                color: viewset.secondaryColor
                font.pixelSize: 24
                x:641
                y:64
                font.bold: true
                MouseArea{
                    anchors.fill: parent
                    onClicked: {
                        onClicked: setting_obj.settingPage.wifimodel.wifiConfig(txt_password.text)
                        popup_SetPasssword.close()
                    }
                }
            }
            Rectangle{
                width: parent.width
                height: 1
                color: "gray"
                y:115
            }

            Rectangle{
                id:input_enterPassword
                anchors.horizontalCenter: parent.horizontalCenter
                width: 661
                height: 56
                color: "#9D9D9D"
                radius: 5
                border.color: "#C6C5CE"
                y:136
                TextEdit{
                    id:txt_password
                    anchors.fill: parent
                    font.pixelSize: 20
                    layer.enabled: true
                    x:50
                    //horizontalAlignment: TextInput.AlignHCenter
                    verticalAlignment:  TextInput.AlignVCenter
                    font.family: viewset.danaFuNumFont
                    property string placeholderText: "Password"

                    onFocusChanged: {

                    }
                    Text {
                        text: txt_password.placeholderText
                        color: "white"
                        visible: !txt_password.text
                        font.pixelSize: 18
                        anchors.verticalCenter: parent.verticalCenter
                        x:50
                        //anchors.horizontalCenter: parent.horizontalCenter
                        font.family: viewset.danaFuNumFont
                    }
                }
            }
        }
    }
    KKeyboard{
        inputtext:txt_password
        leftpad:-50
        toppad:-500
        x:-12
        y:input_enterPassword.y + 140 + 58
        anchors.top: input_enterPassword.bottom
    }
}

