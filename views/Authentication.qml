import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15
import "Components"
import "Utiles" as Util




Item {

    width: 1280
    height: 800


    Util.ViewSettings{
        id:viewset
    }

    Image {
        source: "file://../Assets/AuthenticationBackground.png"
        anchors.fill: parent
    }

    Image {
        anchors.top: parent.top
        anchors.left: parent.left
        source: "file://../Assets/NavBar.png"
    }
    Rectangle{
        id:imgUser
        width: 390
        height: 390
        x:445
        y:182
        color: viewset.primaryColor
        radius: 390/2
        border.width: 20
        border.color: "#D9D9D9"
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

    Text {
        id: txtLookingDirect
        text: qsTr("Keep Looking Directly On Camera")
        anchors.horizontalCenter: parent.horizontalCenter
        y:imgUser.y + imgUser.height + 100
        opacity: 0
        font.pixelSize: 24
        color: "black"
        Behavior on opacity {
            NumberAnimation{duration: 500}
        }
    }

    Timer{
        interval: 5000
        onTriggered: {
            txtLookingDirect.opacity = 0.75
        }
        running: true
    }
    Text {
        id:btn_skip
        text: qsTr("Skip >")
        color: "#4696FA"
        font.pixelSize: 24
        x:1080
        y:659
    }

    Timer{
        interval: 1000
        onTriggered: {
            imgUser.width = 300;
            imgUser.height = 300;
            imgUser.x = 490
            imgUser.y = 135
        }
        running: true
    }
    Text {
        id:txt_start
        text: qsTr("Get Started ")
        anchors.horizontalCenter: parent.horizontalCenter
        y:459
        font.pixelSize: 40
        font.bold: true

    }
    Text {
        id:txt_enterEmail
        text: qsTr("Please enter your Email or Phone Number")
        x : 438
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
        id:input_enterEmail
        x : 438
        y:565
        width: 425
        height: 56
        color: "white"
        radius: 5
        border.color: "#C6C5CE"
        TextEdit{
            id:txt_Email
            anchors.fill: parent
            font.pixelSize: 18
            layer.enabled: true
            x:50
            //horizontalAlignment: TextInput.AlignHCenter
            verticalAlignment:  TextInput.AlignVCenter
            font.family: viewset.danaFuNumFont
            property string placeholderText: "Email / Phone Number"

            onFocusChanged: {
                //numpad.inputtext = txt_Email
                keyboard.y = 800 - 430
                imgUser.width = 106
                imgUser.height = 106
                imgUser.border.width = 5
                imgUser.x=323
                imgUser.y=178
                btn_Continue.btn_color=viewset.secondaryColor
                txt_enterEmail.x = 434
                txt_enterEmail.y = 180
                input_enterEmail.x=434
                input_enterEmail.y = 218
                btn_skip.y=233
                btn_Continue.visible=false
                txt_start.visible = false
                txtLookingDirect.visible = false
            }
            Text {
                text: txt_Email.placeholderText
                color: "#C6C5CE"
                visible: !txt_Email.text
                font.pixelSize: 18
                anchors.verticalCenter: parent.verticalCenter
                x:50
                //anchors.horizontalCenter: parent.horizontalCenter
                font.family: viewset.danaFuNumFont
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
    KButton{
        id:btn_Continue
        text: "Continue with Aptinet Card"
        anchors.horizontalCenter: parent.horizontalCenter
        width: 425
        y:645
        height: 56
        borderRadius: 5
    }
    KKeyboard{
        id:keyboard
        inputtext : txt_Email
        toppad: 500
        leftpad: 500
        y:parent.height
        x:0
        Behavior on y{
            NumberAnimation{duration: 500}
        }
    }
}
