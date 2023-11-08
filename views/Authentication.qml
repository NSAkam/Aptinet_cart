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
        source: "../Assets/AuthenticationBackground.png"
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
        id:btn_skip
        text: qsTr("Skip >")
        color: "#4696FA"
        font.pixelSize: 24
        x:1080
        y:659
    }

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
        text: qsTr("Get Started ")
        anchors.horizontalCenter: parent.horizontalCenter
        y:459
        font.pixelSize: 40
        font.bold: true

    }
    Text {
        id:txt_enterPhone
        text: qsTr("Please enter your Email or Phone Number")
        x : 455
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
        id:input_enterPhone
        x: 455
        y: 565
        width: 308
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
            //horizontalAlignment: TextInput.AlignHCenter
            verticalAlignment:  TextInput.AlignVCenter
            font.family: viewset.danaFuNumFont
            property string placeholderText: "Email / Phone Number"

            onFocusChanged: {
                //numpad.inputtext = txt_phone
                topnavbar.backvisible = true
                numpad.visible = true
                numpad.opacity = 1
                imgUser.width = 106
                imgUser.height = 106
                imgUser.border.width = 5
                imgUser.x=323
                imgUser.y=178
                btn_Continue.btn_color=viewset.secondaryColor
                txt_enterPhone.x = 434
                txt_enterPhone.y = 180
                input_enterPhone.x=434
                input_enterPhone.y = 218
                btn_skip.y=233
                btn_Continue.visible=false
                txt_start.visible = false
            }
            Text {
                text: txt_phone.placeholderText
                color: "#C6C5CE"
                visible: !txt_phone.text
                font.pixelSize: 18
                anchors.verticalCenter: parent.verticalCenter
                x:50
                //anchors.horizontalCenter: parent.horizontalCenter
                // font.family: viewset.danaFuNumFont
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
    Rectangle{
        width: 56
        height: 56
        anchors.top : input_enterPhone.top
        anchors.left: input_enterPhone.right
        color: "#4696FA"
        radius: 4
        Text{
            font.pixelSize: 24
            color: "white"
            text:"->"
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter
        }
        MouseArea{
            anchors.fill: parent
            onClicked: {
                stackview.push(tostepAuthPage)
            }
        }
    }

    KButton{
        id:btn_Continue
        text: "Continue with Loyalty Card"
        anchors.horizontalCenter: parent.horizontalCenter
        width: 365
        y:645
        height: 56
        borderRadius: 5
        onClicked: {
            stackview.push(loyalityAuth)
        }
    }
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
    }

    TopNav{
        id:topnavbar
        backvisible: false
        onBackClicked: {
            topnavbar.backvisible = false
            txt_phone.focus = false
            numpad.visible = false
            numpad.opacity = 0
            imgUser.width = 300
            imgUser.height = 300
            imgUser.border.width = 5
            imgUser.x=490
            imgUser.y=135
            btn_Continue.btn_color = viewset.secondaryColor
            txt_enterPhone.x = 455
            txt_enterPhone.y = 519
            input_enterPhone.x=428
            input_enterPhone.y = 565
            btn_skip.y=659
            btn_Continue.visible=true
            txt_start.visible = true
        }
    }
    Component{
        id:tostepAuthPage
        TowStepAuthentication{

        }
    }
    Component{
        id:loyalityAuth
        LoyalityAuth{

        }
    }
}
