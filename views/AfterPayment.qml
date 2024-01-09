import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15
import QtQuick.Window 2.0
import "Components"
import "Containers"
import "Utiles" as Util
import "PopUps"
import KAST.Logic 1.0


Item {
    id:root
    width: 1280
    height: 800

    property Logic obj_LogicContainerAfterPayment

    property bool canrate: true

    Util.ViewSettings{
        id:viewset
    }

    Image {
        id: bg
        source: "/home/aptinet/files/AuthenticationBackground.png"
        anchors.fill: parent
    }

    Rectangle {
        color: "#1745E8"
        anchors.fill: bg
        opacity: 0.4
    }

    Item{
        id:topPanel
        width: parent.width
        height: 92

        Rectangle {
            id: questionmarkrect
            width: 40
            height: 40
            radius: 4
            color: "white"
            x:1156
            y:32
            visible: false

            Image {
                source: "../Assets/questionmark.png"
                anchors.centerIn: parent
                //                width: 57
                //                height: 57
            }
        }


        Rectangle {
            id: alarmrect
            width: 40
            height: 40
            radius: 4
            color: "white"
            x:1208
            y:32

            Image {
                source: "../Assets/alarm.png"
                anchors.centerIn: parent
                //                width: 57
                //                height: 57
            }
            visible: false
        }



    }

    Item{
        id:leftPanel
        width: 390
        height: parent.height

        Image {
            source: "/home/aptinet/files/AptinetText.png"
            x:32
            y:32
        }
    }

    Item {
        id: mainPanel
        width: 1280
        height: 800

        Rectangle {
            width: 502
            height: 72
            x: 389
            y: -9
            radius: 12
            color: Qt.hsla(0, 0, 100, 0.2)
        }

        Canvas {
            x: 401
            y: 63
            width: 478
            height: 1

            onPaint: {
                var ctx = getContext("2d");
                ctx.strokeStyle = "#9D9D9D";
                ctx.lineWidth = 2;
                ctx.setLineDash([4, 4]); // Set the dash pattern
                ctx.beginPath();
                ctx.moveTo(0, height / 2);
                ctx.lineTo(width, height / 2);
                ctx.stroke();
            }
        }

        Rectangle {
            width: 502
            height: 379
            x: 389
            y: 63
            radius: 12
            color: Qt.hsla(0, 0, 100, 0.2)

            Rectangle {
                width: 167.9
                height: 167.9
                radius: width / 2
                color: "#36EB00"
                x: 167
                y: 47.2

                AnimatedImage {
                    source: "../Assets/5601968.gif"
                    anchors.fill: parent
                }
            }

            Text {
                text: obj_LogicContainerAfterPayment.lang.txt_You_good_to_go
                font.pixelSize: 40
                color: "#36EB00"
                anchors.horizontalCenter: parent.horizontalCenter
                y: 246
                font.bold: true
            }

            Text {
                text: obj_LogicContainerAfterPayment.lang.txt_Thanks_for_shopping_with_us
                font.pixelSize: 30
                color: "white"
                x: 51
                y: 314
                font.weight: Font.DemiBold
            }

        }
        Item{
            anchors.horizontalCenter: parent.horizontalCenter
            width: 550
            Rectangle{
                id:rect_emeiltxt
                width: 350
                height: 50
                radius: 5
                y:473
                MouseArea{
                    anchors.fill: parent
                    onClicked: {
                        popup_SetEmail.open()
                    }
                }

                Text {
                    id:txt_email

                    text: obj_LogicContainerAfterPayment.shopPage.user.email
                    anchors.verticalCenter: parent.verticalCenter
                    anchors.horizontalCenter: parent.horizontalCenter
                }
            }
            KButton{
                borderRadius: 5
                anchors.left: rect_emeiltxt.right
                anchors.top: rect_emeiltxt.top
                text: obj_LogicContainerAfterPayment.lang.btn_Send_Email
                width: 200
                height: 50
                onClicked: {
                    obj_LogicContainerAfterPayment.shopPage.send_factorEmailClicked(txt_email.text)
                }
            }
        }


        Text {
            text: obj_LogicContainerAfterPayment.lang.txt_How_would_you_rate_your_shopping_experience
            font.pixelSize: 24
            horizontalAlignment: Text.AlignHCenter
            anchors.horizontalCenter: parent.horizontalCenter
            y: 530
            color: "#1D1D1D"
        }

        Row {
            spacing: 32
            y: 610
            anchors.horizontalCenter: parent.horizontalCenter


            Rectangle {
                width: 70
                height: 70
                radius: 70
                KButton {
                    anchors.fill: parent
                    btn_color: "#92dc7c"
                    btn_bordercolor: "#92dc7c"


                    Image {
                        source: "../Assets/badrate.png"
                        anchors.centerIn: parent
                    }
                    ishover: false
                    onClicked: {
                        if(root.canrate === true){
                            obj_LogicContainerAfterPayment.shopPage.rate_cart(1)
                            parent.color = viewset.primaryColor
                            root.canrate = false
                        }
                    }
                }

            }



            Rectangle {
                width: 70
                height: 70
                radius: 70

                KButton {
                    anchors.fill: parent
                    btn_color: "#7ad35f"
                    btn_bordercolor: "#7ad35f"

                    Image {
                        source: "../Assets/goodrate.png"
                        anchors.centerIn: parent
                    }
                    ishover: false
                    onClicked: {
                        if(root.canrate === true){
                            obj_LogicContainerAfterPayment.shopPage.rate_cart(2)
                            parent.color = viewset.primaryColor
                            root.canrate = false
                        }
                    }
                }

            }


            Rectangle {
                width: 70
                height: 70
                radius: 70

                KButton {
                    anchors.fill: parent
                    btn_color: "#67db45"
                    btn_bordercolor: "#67db45"

                    Image {
                        source: "../Assets/verygoodrate.png"
                        anchors.centerIn: parent
                    }
                    ishover: false
                    onClicked: {
                        if(root.canrate === true){
                            obj_LogicContainerAfterPayment.shopPage.rate_cart(3)
                            parent.color = viewset.primaryColor
                            root.canrate = false
                        }
                    }
                }

            }


            Rectangle {
                width: 70
                height: 70
                radius: 70
                color: "#4ce51f"

                KButton {
                    anchors.fill: parent
                    btn_color: "#4ce51f"
                    btn_bordercolor: "#4ce51f"

                    Image {
                        source: "../Assets/excellentrate.png"
                        anchors.centerIn: parent
                    }
                    ishover: false
                    onClicked: {
                        if(root.canrate === true){
                            obj_LogicContainerAfterPayment.shopPage.rate_cart(4)
                            parent.color = viewset.primaryColor
                            root.canrate = false
                        }
                    }


                }
            }

        }

        Timer{
            interval:  180000
            onTriggered: {
                cameraProvider.stop()
            }
            running: true
            repeat: true
        }

        KButton{
            id:btn_reset
            anchors.horizontalCenter: parent.horizontalCenter
            y:700
            text:"Start New Shopping"
            height: 70
            borderRadius: 5
            visible: false
            onClicked: {
                cameraProvider.stop()
            }
        }
        Timer{
            running: true
            repeat: false
            interval: 10000
            onTriggered: {
                btn_reset.visible = true
            }
        }

    }



    Popup {
        id: popup_SetEmail
        property QtObject setting_obj


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
                    text: obj_LogicContainerAfterPayment.lang.txt_Enter_your_Email_Address
                    anchors.horizontalCenter: parent.horizontalCenter
                    y:24
                    font.pixelSize: 16
                }
                Text {
                    text: obj_LogicContainerAfterPayment.lang.txt_enter_Email
                    font.pixelSize: 24
                    font.bold: true
                    anchors.horizontalCenter: parent.horizontalCenter
                    y:65
                }

                Text {
                    text: obj_LogicContainerAfterPayment.lang.txt_Cancel
                    y:64
                    x:32
                    font.pixelSize: 24
                    color: "gray"
                    MouseArea{
                        anchors.fill: parent
                        onClicked: {
                            popup_SetEmail.close()
                        }
                    }
                }
                Text {
                    text: obj_LogicContainerAfterPayment.lang.txt_Enter
                    color: viewset.secondaryColor
                    font.pixelSize: 24
                    x:641
                    y:64
                    font.bold: true
                    MouseArea{
                        anchors.fill: parent
                        onClicked: {
                            txt_email.text=txt_password.text
                            //onClicked: setting_obj.settingPage.wifimodel.wifiConfig(txt_password.text)
                            popup_SetEmail.close()
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
                        property string placeholderText: obj_LogicContainerAfterPayment.lang.txt_Email

                        onFocusChanged: {
                            keyboard.visible = true
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
            id:keyboard
            inputtext:txt_password
            leftpad:-50
            toppad:-500
            x:-12
            y:input_enterPassword.y + 140 + 58
            anchors.top: input_enterPassword.bottom
            onEnter: {
                txt_email.text=txt_password.text
                //onClicked: setting_obj.settingPage.wifimodel.wifiConfig(txt_password.text)
                popup_SetEmail.close()
            }
        }
    }

}
