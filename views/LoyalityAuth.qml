import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15
import "Components"
import "Utiles" as Util




Item {

    width: 1280
    height: 800
    Component.onCompleted: {
        txt_Enterloyality.visible = false
        input_enterEmail.visible = false
        btn_Action.visible = false
        //keyboard.visible = false
        btn_Enter.visible = true
        icon_loyality.visible = true
        message.visible = true
    }



    Util.ViewSettings{
        id:viewset
    }

    Image {
        source: "../Assets/AuthenticationBackground.png"
        anchors.fill: parent
    }

    Text {
        id:message
        text: qsTr("Please scan the Loyalty card or Enter Loyalty Code")
        anchors.horizontalCenter: parent.horizontalCenter
        y:156
        font.pixelSize: 24
        visible: true
    }
    Image {
        id:icon_loyality
        source: "../Assets/loyalityIcon.png"
        anchors.horizontalCenter: parent.horizontalCenter
        y:228
        visible: true
    }

    Text {
        id:btn_skip
        text: qsTr("Skip >")
        color: "#4696FA"
        font.pixelSize: 24
        x:1080
        y:659
        MouseArea{
            anchors.fill: parent
            onClicked: {
                stackview.push(shoppage)
            }
        }
    }


    KButton{
        id:btn_Enter
        text: "Enter Loyalty Card  >"
        anchors.horizontalCenter: parent.horizontalCenter
        width: 260
        y:645
        height: 56
        borderRadius: 5
        visible: false
        isBold: false
        fontsize: 20
        onClicked: {
            txt_Enterloyality.visible = true
            input_enterEmail.visible = true
            btn_Action.visible = true
            keyboard.y = keyboard.y- 458
            btn_Enter.visible = false
            icon_loyality.visible = false
            message.visible = false
        }
    }



    Text{
        id:txt_Enterloyality
        text: "Please enter your loyalty code"
        font.pixelSize: 20
        anchors.horizontalCenter: parent.horizontalCenter
        y:172
        visible: false
    }

    Rectangle{
        id:btn_Action
        width: 70
        height: 56
        anchors.top : input_enterEmail.top
        anchors.left: input_enterEmail.right
        anchors.leftMargin: -14
        visible: false
        color: "#4696FA"
        radius: 4
        Image {
            source: "../Assets/arrow_calibrate.png"
            rotation: 180
            x:35
            anchors.verticalCenter: parent.verticalCenter
        }
        MouseArea{
            anchors.fill: parent
            onClicked: {
                stackview.push(tostepAuthPage)
            }
        }
    }
    Rectangle{
        id:input_enterEmail
        anchors.horizontalCenter: parent.horizontalCenter
        y: 218
        width: 308
        height: 56
        color: "white"
        radius: 5
        border.color: "#C6C5CE"
        visible: false
        TextEdit{
            id:txt_Email
            anchors.fill: parent
            font.pixelSize: 20
            layer.enabled: true
            x:50
            //horizontalAlignment: TextInput.AlignHCenter
            verticalAlignment:  TextInput.AlignVCenter
            font.family: viewset.danaFuNumFont
            property string placeholderText: "Loyalty Code"

            onFocusChanged: {

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




    KKeyboard{
        id:keyboard
        inputtext : txt_Email
        toppad: 500
        leftpad: 500
        y:parent.height - 0
        x:0
        visible: true

        Behavior on y{
            NumberAnimation{duration: 500}
        }
    }

    TopNav{
        id:topnavbar
        backvisible: true
        onBackClicked: {
            stackview.pop()
        }
    }
    Component{
        id:tostepAuthPage
        TowStepAuthentication{

        }
    }
    Component{
        id:shoppage
        Shop{

        }
    }
}
