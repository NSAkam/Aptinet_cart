import QtQuick 2.12
import QtQuick.Window 2.12
import QtQuick.Controls 2.12
import QtGraphicalEffects 1.12
import "getTimeFromAPI.js" as GetTimeFromAPI


Window {
    width: 1280
    height: 800
    visible: true
    title: qsTr("Spalsh - Enable")
    id: root

    property alias startbtn: startbutton
    property alias settingsbtn: settingsiconbutton
    property alias languagebtn: languageiconebutton


    Image {
        id: bg
        source: "Resources/BG.png"
        anchors.fill: root
    }

    FastBlur {
        id: bgblur
        anchors.fill: bg
        source: bg
        radius: 10
    }

    Image {
        id: logo
        source: "Resources/enable_logo.png"
        x: 497
        y: 89
        width: 287
        height: 133
    }

    Button {
        id: startbutton
        width: 318
        height: 66
//        color: Qt.rgba(240, 140, 90, 1)
        x: 481
        y: 522


        background:
            Rectangle {
            color: "#F08C5A"
            radius: 4
        }

        Text {
            id: starttext
            text: qsTr("START")
            color: Qt.rgba(255, 255, 255, 1)
            font.family: "Archivo"
            font.pixelSize: 24
            font.weight: Font.Bold
            font.letterSpacing: 0.04 * 24
            horizontalAlignment: Text.AlignHCenter
            lineHeight: 26.11
            x: 118
            y: 15
//            anchors.horizontalCenter: startrect.horizontalCenter
        }

    }


    Button {
        id: viewguidebutton
        width: 318
        height: 66
//        color: Qt.rgba(240, 140, 90, 1)
        x: 481
        y: 612


        background:
            Rectangle {
            color: "transparent"
            radius: 4
            border.width: 1.5
            border.color: "#F08C5A"
        }

        Text {
            id: viewguidetext
            text: qsTr("VIEW GUIDE")
            color: "#F08C5A"
            font.family: "Archivo"
            font.pixelSize: 20
            font.weight: Font.Bold
            font.letterSpacing: 0.04 * 20
            horizontalAlignment: Text.AlignHCenter
            lineHeight: 21.76
            x: 100
            y: 17
//            anchors.horizontalCenter: viewguiderect.horizontalCenter
        }

    }

    Button {
        id: settingsiconbutton
//        color: Qt.hsla(195, 87, 45, 0.6)
        width: 48
        height: 48
        x: 1200
        y: 720

        background:
            Rectangle {
            color: "#F05A28"
            radius: 33
        }

        Image {
            id: gearwhellicon
            source: "Resources/gearwheel.png"
            width: 21.5
            height: 22
            x: 13.25
            y: 13
        }


    }

    Button {
        id: languageiconebutton
//        color: Qt.hsla(195, 87, 45, 0.6)
        width: 48
        height: 48
        x: 32
        y: 720

        background:
            Rectangle {
            color: "#F05A28"
            radius: 33
        }

        Image {
            id: globeicon
            source: "Resources/globe.png"
            width: 22
            height: 22
            x: 13
            y: 13
        }

    }


    Rectangle{
        id: timerect
        color: "#F05A28"
        radius: 32
        width: 100
        height: 38
        x: 1148
        y: 32

        Text {
            id: timetext
            text: qsTr("12:36")
            color: "white"
            font.family: "Archivo"
            font.pixelSize: 24
            font.weight: Font.Bold
            font.letterSpacing: 0.04 * 24
            horizontalAlignment: Text.AlignHCenter
            lineHeight: 26.11
            x: 16
            y: 2

            onTextChanged: {
                    var xhr = new XMLHttpRequest();
                    xhr.open("GET", "https://timeapi.io/api/Time/current/zone?timeZone=Asia/Tehran");
                    xhr.onload = function() {
                      if (xhr.status === 200) {
                        const { hour, minute } = JSON.parse(xhr.responseText);

                        timetext.text = hour + ":" + minute;
                      } else {
                        console.log("خطا در دریافت پاسخ از API");
                      }
                    };
                    xhr.send();
                  }
        }

    }

    BatteryLevelIndicator {
        id: battery

    }

}

