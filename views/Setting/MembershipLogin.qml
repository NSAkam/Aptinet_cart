import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import QtGraphicalEffects 1.12
import "../Components"
import "../Utiles"
import KAST.Logic 1.0



Item {
    id: root

    property Logic obj_LogicContainer

    visible: true
    width: 1280
    height: 800

    ViewSettings{
        id:viewset
    }

    Image {
        id: q
        source: "../../Assets/AuthenticationBackground.png"
        anchors.fill: parent
    }




    Rectangle {
        width: 687
        height: 72
        color: "#4696FA"
        x: 296
        y: 212
        radius: 6

        Text {
            text: "Please scan the membership card"
            width: 413
            height: 48
            color: "white"
            font.pixelSize: 24
            x: 137
            y: 20
            font.family: "Archivo"
            font.weight: Font.Bold
        }
    }

    Rectangle {
        width: 320
        height: 328
        color: "white"
        x: 300
        y: 304

        layer.enabled: true
        layer.effect: DropShadow {
            horizontalOffset: 3
            verticalOffset: 0
            radius: 15
            samples: 19
            color: "#BDBDBD"
        }

        Image {
            source: "../../Assets/QR.png"
            width: 170
            height: 170
            x: 75
            y: 79
        }
    }

    Rectangle {
        width: 343
        height: 328
        color: "white"
        x: 641
        y: 304

        layer.enabled: true
        layer.effect: DropShadow {
            horizontalOffset: 3
            verticalOffset: 0
            radius: 15
            samples: 19
            color: "#BDBDBD"
        }
        Rectangle{
            id:input_username
            width: 295
            height: 56
            x: 24
            y: 24
            color: "white"
            radius: 5
            border.color: "#C6C5CE"
            TextEdit{
                id:txt_username
                anchors.fill: parent
                font.pixelSize: 18
                layer.enabled: true
                x:50
                horizontalAlignment: TextInput.AlignLeft
                verticalAlignment:  TextInput.AlignVCenter
                font.family: viewset.danaFuNumFont
                property string placeholderText: "Username"

                onFocusChanged: {
                    keyboard.visible = true
                    keyboard.inputtext = txt_username

                }
                Text {
                    text: txt_username.placeholderText
                    color: "#C6C5CE"
                    visible: !txt_username.text
                    font.pixelSize: 20
                    anchors.verticalCenter: parent.verticalCenter
                    x:50
                    //anchors.horizontalCenter: parent.horizontalCenter
                    // font.family: viewset.danaFuNumFont
                }
            }
        }

        Rectangle{
            id:input_password
            width: 295
            height: 56
            x: 24
            y: 92
            color: "white"
            radius: 5
            border.color: "#C6C5CE"
            TextEdit{
                id:txt_password
                anchors.fill: parent
                font.pixelSize: 18
                layer.enabled: true
                x:50
                horizontalAlignment: TextInput.AlignLeft
                verticalAlignment:  TextInput.AlignVCenter
                font.family: viewset.danaFuNumFont
                property string placeholderText: "Password"

                onFocusChanged: {
                    console.log("asdasdasdasd")
                    keyboard.visible = true
                    keyboard.inputtext = txt_password

                }
                Text {
                    text: txt_password.placeholderText
                    color: "#C6C5CE"
                    visible: !txt_password.text
                    font.pixelSize: 20
                    anchors.verticalCenter: parent.verticalCenter
                    x:50
                    //anchors.horizontalCenter: parent.horizontalCenter
                    // font.family: viewset.danaFuNumFont
                }
            }
        }


        KButton{
            width: 295
            height: 64
            x: 24
            y: 168
            borderRadius: 4
            text: "Confirm >"
            fontsize: 25
            isBold: false
            btn_color: "#4696FA"
            btn_borderWidth: 0
            onClicked: {
                obj_LogicContainer.settingPage.confirm_clicked(txt_username.text,txt_password.text)
            }
        }

        KButton{
            width: 295
            height: 64
            x: 24
            y: 248
            borderRadius: 4
            text: "Back"
            fontsize: 25
            isBold: false
            onClicked: {
                cameraProvider.stop()
            }
        }

    }
    TopNav{
        onBackClicked: {
            cameraProvider.stop()
        }
    }
    KKeyboard{
        id:keyboard
        inputtext : txt_username
        toppad: 500
        leftpad: 500
        y:parent.height - 450
        x:0
        visible: false

    }
    Component{
        id:settingPage
        SettingPage{
            obj_Logic: obj_LogicContainer
        }
    }
    Connections{
        target:obj_LogicContainer.settingPage
        function onLoginConfirmedSignal(){
            stackview.push(settingPage)
        }
    }
}
