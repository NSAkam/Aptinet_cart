import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15
import QtQuick.Window 2.0
import "Components"
import "Utiles" as Util
import "Setting"
import "PopUps"
import KAST.Logic 1.0



Item {

    width: 1280
    height: 800

    Util.ViewSettings{
        id:viewset
    }

    Logic{
        id:obj_logic
    }



    Image {
        id: background
        source: "../Assets/SplashBackground.png"
        anchors.fill: parent
        Rectangle{
            id:backgroundOpacity
            color: "#1D1D1D"
            anchors.fill:parent
            opacity: 0
            Behavior on opacity {
                NumberAnimation { duration: 1000 }
            }
        }
    }

    FastBlur {

        anchors.fill: background
        source: background
        radius: 32
    }


    Image {
        id: aptinetIcon
        source: "../Assets/AptinetIcon1.png"
        y:124
        width: 208
        height: 154
        anchors.horizontalCenter: parent.horizontalCenter

    }


    Text {
        id:txt_welcome
        text: qsTr(obj_logic.lang.txt_welcome)
        font.pixelSize: 64
        anchors.horizontalCenter: parent.horizontalCenter
        y:342
        opacity: 1
    }
    Text {
        id:txt_welcomebot
        text: qsTr(obj_logic.lang.txt_Toaquickshoppingexperience)
        font.pixelSize: 20
        y:428
        opacity: 1
        anchors.horizontalCenter: parent.horizontalCenter
    }
    Rectangle {
        anchors.horizontalCenter: parent.horizontalCenter
        width: 650

        KButton{
            id:btn_enterPhone
            width: 318
            height: 66

            y:522
            fontsize: 22
            text:  obj_logic.lang.btn_Enter_Phone_Number
            borderRadius: 5
            ishover: false
            shadow: false
            opacity: 1

            onClicked: {
                stackview.push(authenticationPage)
            }
        }
        KButton{
            id:btn_scanMemberShopCart
            anchors.top:btn_enterPhone.top
            anchors.left: btn_enterPhone.right
            anchors.leftMargin: 20
            width: 318
            height: 66


            y:522
            fontsize: 22
            text:  obj_logic.lang.btn_Scan_MemberShop_Cart
            borderRadius: 5
            ishover: false
            shadow: false
            opacity: 1

            onClicked: {
                obj_logic.login_loyaltyCartClicked()
                stackview.push(loyalityAuth)
            }
        }
        KButton{
            id:btn_help
            anchors.top:btn_enterPhone.bottom
            anchors.left: btn_enterPhone.left
            anchors.topMargin: 20
            width: 318
            height: 66

            y:522
            fontsize: 22
            text:  obj_logic.lang.btn_Help
            borderRadius: 5
            ishover: false
            shadow: false
            opacity: 1

            onClicked: {
                stackview.push(guidpage)
            }
        }
        KButton{
            id:btn_continue
            anchors.top:btn_scanMemberShopCart.bottom
            anchors.left: btn_scanMemberShopCart.left
            anchors.topMargin: 20
            width: 318
            height: 66

            y:522
            fontsize: 22
            text:  obj_logic.lang.btn_Continue
            borderRadius: 5
            ishover: false
            shadow: false
            opacity: 1

            onClicked: {
                obj_logic.continue_clicked();
            }
        }
    }


    Rectangle{
        id:languageButton
        x:0
        y:688
        width: 112
        height: 112
        color: "transparent"
        Image {
            anchors.fill: parent
            source: "../Assets/LanguageCircle.png"
            width: parent.width
            height: parent.height
        }
        Behavior on opacity{
            NumberAnimation{duration: 1000}
        }
        MouseArea{
            anchors.fill: parent
            onClicked: {
                backgroundOpacity.opacity = 0.75
                languageButtons.visible = true
            }
        }
    }
    KBattery{
        battery_level: obj_logic.battery.batteryLevel
        x:32
        y:32

    }
    Rectangle{
        id:rect_Clock
        width: 100
        height: 38
        color: viewset.primaryColor
        radius: 50
        x:1148
        y:32
        Timer{
            running: true
            repeat: true
            interval: 1000
            onTriggered: {
                txt_time.text =  new Date().getHours() + ":" + new Date().getMinutes()
            }
        }
        Text {
            id:txt_time
            text: new Date().getHours() + ":" + new Date().getMinutes()

            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter
            font.pixelSize: 24
            color: "white"
            font.bold: true
        }
    }
    Item{
        id: languageButtons
        anchors.fill: parent
        width: parent.width
        height: parent.height
        visible: false
        Rectangle{
            anchors.fill: parent
            color: "transparent"
            MouseArea{
                anchors.fill: parent
                onClicked: {
                    backgroundOpacity.opacity = 0
                    languageButtons.visible = false
                }
            }
        }

        Rectangle{
            id:backgroundselectLangOpacity
            anchors.fill: parent
            color: "#1D1D1D"
            opacity: 0.75
        }

        GridView {
            id: productsgridview
            x:213
            width: 854
            height: 170
            cellWidth: 200
            cellHeight: 80
            focus: true
            anchors.verticalCenter: parent.verticalCenter
            flow: GridView.FlowLeftToRight
            clip: true
            interactive: true

            model: obj_logic.langList
            delegate:KBorderButton{
                borderwidth:0
                text: model.name
                x:213
                y:315
                width: 185
                height: 66
                MouseArea{
                    anchors.fill: parent
                    onClicked: {
                        obj_logic.language_Changed(parent.text)
                    }
                }
            }
        }
    }


    Component{
        id:authenticationPage
        Authentication{
            obj_LogicContainer: obj_logic
        }

    }

    Component{
        id:guidpage
        GuideTips{
            obj_LogicContainerGuidTips: obj_logic
        }
    }
    Component{
        id:loyalityAuth
        LoyalityAuth{
            obj_LogicContainerLoyalityAuth: obj_logic
        }
    }

    Component{
        id:settingPage
        SettingPage{
            obj_LogicSetting: obj_logic;
        }
    }

    Component{
        id:shoppage
        Shop{
            obj_LogicContainerShop: obj_logic;
        }
    }

    FullMessageTimer{
        id:messageTimer
    }

    Connections{
        target:obj_logic
        function onGoToShopPageSignal(){
            stackview.push(shoppage)
        }

        function onGoToSettingPageSignal(){
            stackview.push(settingPage)
        }

        function onShowPopupMessageTimerSignal(v){
            messageTimer.messageText = v
            messageTimer.open()
        }
        function onValidPhoneNumberSignal(){

        }

        function onLanguageChangedSignal(){
            cameraProvider.stop()
        }
    }
}
