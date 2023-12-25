import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15
import "Components"
import "Utiles" as Util
import "PopUps"
import KAST.Logic 1.0




Item {

    width: 1280
    height: 800

    property Logic obj_LogicContainer

    Util.ViewSettings{
        id:viewset
    }



    Image {
        source: "/home/aptinet/files/AuthenticationBackground.png"
        anchors.fill: parent
    }

    Image {
        anchors.top: parent.top
        anchors.left: parent.left
        source: "../Assets/NavBar.png"
    }

    Rectangle{
        id:imgUser
        width: 300
        height: 300
        x:490
        y:135
        color: viewset.primaryColor
        radius: width/2
        border.width: 20
        border.color: "#D9D9D9"
        Image {
            source: "../Assets/FaceScanning.png"
            anchors.fill: parent
        }
        Behavior on width {
            NumberAnimation{duration: 500}
        }
        Behavior on height {
            NumberAnimation{duration: 500}
        }
        Behavior on x {
            NumberAnimation{duration: 500}
        }
        Behavior on y {
            NumberAnimation{duration: 500}
        }
        Behavior on border.width {
            NumberAnimation{duration: 500}
        }
    }

    //    Text {
    //        id:btn_skip
    //        text: "Skip >"
    //        color: "#4696FA"
    //        font.pixelSize: 24
    //        x:1080
    //        y:659
    //        MouseArea{
    //            anchors.fill: parent
    //            onClicked: {
    //                stackview.push(shoppage)
    //            }
    //        }
    //    }

    //    Timer{
    //        interval: 1000
    //        onTriggered: {
    //            imgUser.width = 300;
    //            imgUser.height = 300;
    //            imgUser.x = 490
    //            imgUser.y = 135
    //        }
    //        running: true
    //    }
    Text {
        id:txt_start
        text: obj_LogicContainer.lang.txt_Get_Started
        x:523
        y:459
        font.pixelSize: 40
        font.bold: true

    }
    Text {
        id:txt_enterPhone
        text: obj_LogicContainer.lang.txt_Please_enter_your_Phone_Number
        x : 480
        y:519
        font.pixelSize: 20
        font.bold: false
        color: viewset.primaryColor
        Behavior on width {
            NumberAnimation{duration: 500}
        }
        Behavior on height {
            NumberAnimation{duration: 500}
        }
        Behavior on x {
            NumberAnimation{duration: 500}
        }
        Behavior on y {
            NumberAnimation{duration: 500}
        }
    }

    Rectangle{
        id:btn_blueContinue
        width: 70
        height: 56
        anchors.top : input_enterPhone.top
        anchors.left: input_enterPhone.right
        anchors.leftMargin: -14
        visible: false
        color: "#4696FA"
        radius: 4
        Image {
            source: "../Assets/arrow_calibrate.png"
            //            font.pixelSize: 24
            //            color: "white"
            //            text:"  >"
            //            font.bold: true
            rotation: 180
            x:35
            anchors.verticalCenter: parent.verticalCenter
        }
        MouseArea{
            anchors.fill: parent
            onClicked: {
                obj_LogicContainer.login_phoneNumber(txt_phone.text)
            }
        }
    }

    Rectangle{
        id:input_enterPhone
        x: 428
        y: 565
        width: 425
        height: 56
        color: "white"
        radius: 5
        border.color: "#C6C5CE"
        TextInput{
            id:txt_phone
            anchors.fill: parent
            font.pixelSize: 18
            layer.enabled: true
            x:50
            horizontalAlignment: TextInput.AlignHCenter
            verticalAlignment:  TextInput.AlignVCenter
            font.family: viewset.danaFuNumFont
            property string placeholderText: obj_LogicContainer.lang.txt_Phone_Number

            onFocusChanged: {
                numpad.inputtext = txt_phone
                topnavbar.backvisible = true

                imgUser.width = 106
                imgUser.height = 106
                imgUser.border.width = 5
                imgUser.x=323
                imgUser.y=178
                txt_enterPhone.x = 455
                txt_enterPhone.y = 180
                input_enterPhone.width = 308
                input_enterPhone.x=455
                input_enterPhone.y = 218
                btn_blueContinue.visible = true
                //                btn_skip.y=233
                //                btn_Continue.visible=false
                txt_start.visible = false
            }
            Text {
                text: txt_phone.placeholderText
                color: "#C6C5CE"
                visible: !txt_phone.text
                font.pixelSize: 20
                anchors.verticalCenter: parent.verticalCenter
                x:50
                //anchors.horizontalCenter: parent.horizontalCenter
                // font.family: viewset.danaFuNumFont
            }
            onWidthChanged: {
                if(width == 425){
                    txt_start.visible = true
                }
                if(width == 308){
                    numpad.visible = true
                    numpad.opacity = 1
                }
            }
        }
        Behavior on width {
            NumberAnimation{duration: 500}
        }
        Behavior on height {
            NumberAnimation{duration: 500}
        }
        Behavior on x {
            NumberAnimation{duration: 500}
        }
        Behavior on y {
            NumberAnimation{duration: 500}
        }
        Behavior on border.width {
            NumberAnimation{duration: 500}
        }
    }


    //    KButton{
    //        id:btn_Continue
    //        text: "Continue with Loyalty Card              "
    //        anchors.horizontalCenter: parent.horizontalCenter
    //        width: 428
    //        y:645
    //        height: 56
    //        borderRadius: 5
    //        btn_borderWidth: 0
    //        isBold: false
    //        onClicked: {
    //            stackview.push(loyalityAuth)
    //        }
    //    }
    Numpad{
        id:numpad
        inputtext : txt_phone
        x:455
        y:298
        Behavior on y{
            NumberAnimation{duration: 500}
        }
        opacity: 0
        Behavior on opacity {
            NumberAnimation{duration: 1000}
        }
        visible: false
        onEnter: {
            obj_LogicContainer.login_phoneNumber(txt_phone.text)
        }
    }

    TopNav{
        id:topnavbar
        backvisible: true
        onBackClicked: {
            stackview.pop()
            txt_phone.focus = false
            numpad.visible = false
            numpad.opacity = 0
            imgUser.width = 300
            imgUser.height = 300
            imgUser.border.width = 5
            imgUser.x=490
            imgUser.y=135
            txt_enterPhone.x = 480
            txt_enterPhone.y = 519
            btn_blueContinue.visible=false
            input_enterPhone.width = 425
            input_enterPhone.x=428
            input_enterPhone.y = 565
            //            btn_skip.y=659
            //            btn_Continue.visible=true
            //txt_start.visible = true
            topnavbar.backvisible = false
        }
    }
}
