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
        id: background
<<<<<<< HEAD
        source: "../Assets/SplashBackground.png"
=======
        source: "file://../Assets/SplashBackground.png"
>>>>>>> origin/main
        anchors.fill: parent
        Rectangle{
            id:backgroundOpacity
            anchors.fill: parent
            color: "#1D1D1D"
            opacity: 0.75
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
    KBattery{
        battery_level: 45
    }

    Image {
        id: aptinetIcon
<<<<<<< HEAD
        source: "../Assets/AptinetImage.png"
=======
        source: "file://../Assets/AptinetImage.png"
>>>>>>> origin/main
        x:381
        y:251
        width: 518
        height: 240
        Behavior on x {
            NumberAnimation { duration: 1000 }
        }
        Behavior on y {
            NumberAnimation { duration: 1000 }
        }
        Behavior on width {
            NumberAnimation { duration: 1000 }
        }
        Behavior on height {
            NumberAnimation { duration: 1000 }
        }
    }

    Rectangle{
        id:statrtButton
        width: 374
        height: 179
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        color: "transparent"
        Text {
            id: txtStartButton
            color: "#F5AF8C"
            text: qsTr("Tap To Start >")
            font.bold: true
            font.pixelSize: 32
            font.letterSpacing: -0.5
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter
        }

        NumberAnimation {
            target: txtStartButton
            property: "opacity"
            duration: 1000
            easing.type: Easing.InOutQuad
            from:0.25
            to:1
            running: true
            loops: Animation.Infinite
        }
        MouseArea{
            anchors.fill: parent
            onClicked: {
                backgroundOpacity.opacity = 0
                aptinetIcon.x=497;
                aptinetIcon.y=89;
                aptinetIcon.width=287;
                aptinetIcon.height=133;
                startshoppingButton.opacity = 1;
                guideButton.opacity = 1;
                statrtButton.visible = false
                startshoppingButton.enabled = true;
                guideButton.enabled = true;
                settingButton.enabled=true;
                settingButton.opacity = 1;
                languageButton.enabled = true
                languageButton.opacity = 1
            }
        }

    }
    KButton{
        id:startshoppingButton
        width: 318
        height: 66
        x:477
        y:522
        fontsize: 24
        text:  qsTr("START")
        borderRadius: 5
        ishover: false
        shadow: false
        enabled: false
        opacity: 0
        Behavior on opacity{
            NumberAnimation{duration: 1000}
        }
        onClicked: {
            stackview.push(authenticationPage)
        }
    }
    KBorderButton{
        id:guideButton
        width: 318
        height: 66
        radius: 5
        x:477
        y:612
        text: "VIEW GUIDE"
        enabled: false
        opacity: 0
        Behavior on opacity{
            NumberAnimation{duration: 1000}
        }
    }
    Rectangle{
        id:settingButton
        x:1168
        y:688
        width: 112
        height: 112
        color: "transparent"
        Image {
            anchors.fill: parent
<<<<<<< HEAD
            source: "../Assets/SettingCircle.png"
=======
            source: "file://../Assets/SettingCircle.png"
>>>>>>> origin/main
            width: parent.width
            height: parent.height
        }
        enabled: false
        opacity: 0
        Behavior on opacity{
            NumberAnimation{duration: 1000}
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
<<<<<<< HEAD
            source: "../Assets/LanguageCircle.png"
=======
            source: "file://../Assets/LanguageCircle.png"
>>>>>>> origin/main
            width: parent.width
            height: parent.height
        }
        enabled: false
        opacity: 0
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

    Item{
        id: languageButtons
        anchors.fill: parent
        width: parent.width
        height: parent.height
        visible: false

        Rectangle{
            id:backgroundselectLangOpacity
            anchors.fill: parent
            color: "#1D1D1D"
            opacity: 0.75
        }
        FastBlur {

            anchors.fill: parent
            source: parent
            radius: 32
        }

        KBorderButton{
            borderwidth:0
            text: "English"
            x:213
            y:315
            width: 185
            height: 66
        }
        KBorderButton{
            borderwidth:0
            text: "Deutsch"
            x:436
            y:315
            width: 185
            height: 66
            textColor: "black"
        }
        KBorderButton{
            borderwidth:0
            text: "Français"
            x:659
            y:315
            width: 185
            height: 66

            textColor: "black"
        }
        KBorderButton{
            borderwidth:0
            text: "Italiano"
            x:882
            y:315
            width: 185
            height: 66
            textColor: "black"
        }
        KBorderButton{
            borderwidth:0
            text: "Español"
            x:213
            y:419
            width: 185
            height: 66
            textColor: "black"

        }
        KBorderButton{
            borderwidth:0
            text: "Português"
            x:436
            y:419
            width: 185
            height: 66
            textColor: "black"
        }
        KBorderButton{
            borderwidth:0
            text: "Türkçe"
            x:659
            y:419
            width: 185
            height: 66
            textColor: "black"
        }
        KBorderButton{
            borderwidth:0
            text: "العربية"
            x:882
            y:419
            width: 185
            height: 66
            textColor: "black"
        }
    }
    Component{
        id:authenticationPage
        Authentication{

        }
    }
}
