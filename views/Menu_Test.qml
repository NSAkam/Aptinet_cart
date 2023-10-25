import QtQuick 2.12
import QtQuick.Window 2.12
import QtQuick.Controls 2.12
import QtGraphicalEffects 1.12
import "Components"


Item {
    width: 1280
    height: 800
    id: root
    signal backbuttonClicked()


    Image {
        id: bg
        source: "../Assets/BG.png"
        anchors.fill: root
        opacity: 0.1

        Rectangle {
            anchors.fill: bg
            color: "white"
            opacity: 0.7
        }

    }

    FastBlur {
        id: bgblur
        anchors.fill: bg
        source: bg
        radius: 70
    }

    Rectangle {
        id: whiterect
        color: "white"
        width: 1280
        height: 92
        x: 0

        Image {
            id: aptinet
            source: "../Assets/Aptinet.png"
            x: 550
            y: 32
        }

        Image {
            id: smartcart
            source: "../Assets/smart_cart.png"
            x: 578
            y: 65
        }
    }


    Row{
        id: rowlayout
        spacing: 36
        x: 248
        y: 312

        Button {
            id: weightbutton
            width: 128
            height: 160

            background: Rectangle{
                color: "white"
                anchors.fill: weightbutton
                radius: 4
            }

            Image {
                id: weightimage
                source: "../Assets/weighticon.png"
                x: 34
                y: 24
            }

            Text {
                id: weightsensortext
                text: qsTr("Weight\nSensor")
                x: 33
                y: 100
                color: "#6D6D6D"
                font.family: "Archivo"
                font.pixelSize: 18
                font.weight: Font.DemiBold
                font.letterSpacing: 0.02 * 18
                horizontalAlignment: Text.AlignHCenter
                //                lineHeight: 24
            }

            MouseArea {
                anchors.fill: weightbutton
                onClicked: {
                    weightanim.running = true
                    weightpopup.open()
                    graypopuprect.z = root.z + 1
                    //                    graypopuprect.visible = true
                    graypopuprect.opacity = 0.9
                    backbuttoninpopup.opacity = 1
                    backbuttoninpopup.visible = true
                    bgblur.radius = 70
                }
            }

            PropertyAnimation {
                id: weightanim
                duration: 200
                target: weightbutton
                property: "opacity"
                from:0
                to:1
                easing.type: Easing.InOutQuad
            }

            Popup {
                id: weightpopup

                background:
                    Rectangle {
                    id: weightpopuprect
                    width: 525
                    height: 387
                    x: 377
                    y: 140 + 92
                    radius: 4

                    Text {
                        id: puttheweighttext
                        text: qsTr("Please put the weight in cart")
                        x: 55
                        y: 40
                        color: "#1D1D1D"
                        font.family: "Archivo"
                        font.pixelSize: 32
                        font.weight: Font.Bold
                        font.letterSpacing: 0.04 * 32
                        horizontalAlignment: Text.AlignLeft
                        lineHeight: 44
                    }

                    Rectangle {
                        id: hollowbox
                        width: 343
                        height: 56
                        x: 141
                        y: 122.5
                        color: "#F7F7F7"
                        radius: 4
                    }

                    Image {
                        id: baskets
                        source: "../Assets/baskets.png"
                        width: 77
                        height: 69
                        x: 40
                        y: 116
                    }

                    Button {
                        id: calibratebutton

                        background:
                            Rectangle {
                            id: calibraterect
                            color: "#F4AE8B"
                            width: 187
                            height: 72
                            x: 40
                            y: 217
                            radius: 4

                            Image {
                                id: arrowimage
                                source: "../Assets/arrow_calibrate"
                                x: 24
                                y: 28
                                width: 9
                                height: 16
                                opacity: 1
                            }

                            Text {
                                id: calibratetext
                                text: qsTr("Calibrate")
                                color: "white"
                                y: 17
                                x: 49
                                //                                width: 106
                                //                                height: 48
                                font.family: "Archivo"
                                font.pixelSize: 24
                                font.weight: Font.DemiBold
                                font.letterSpacing: 0.04 * 24
                                horizontalAlignment: Text.AlignLeft
                                lineHeight: 48
                                opacity: 1
                            }
                        }

                    }


                    Button {
                        id: confirmbutton

                        background:
                            Rectangle {
                            id: confirmrect
                            color: "#4696FA"
                            width: 241
                            height: 72
                            x: 243
                            y: 217
                            radius: 4

                            Text {
                                id: confirmtext
                                text: qsTr("Confirm")
                                color: "white"
                                y: 17
                                x: 72
                                font.family: "Archivo"
                                font.pixelSize: 24
                                font.weight: Font.Bold
                                font.letterSpacing: 0.04 * 24
                                horizontalAlignment: Text.AlignLeft
                                lineHeight: 48
                                font.bold: true
                            }
                        }

                        onClicked: {
                            confirmbtnanim.running = true
                        }

                        PropertyAnimation {
                            id: confirmbtnanim
                            duration: 200
                            target: confirmbutton
                            property: "opacity"
                            from:0
                            to:1
                            easing.type: Easing.InOutQuad
                        }

                    }

                    Text {
                        id: calibrationdatetext
                        text: qsTr("Calibration date")
                        color: "#1D1D1D"
                        y: 333
                        x: 40
                        font.family: "Archivo"
                        font.pixelSize: 20
                        font.weight: Font.Bold
                        font.letterSpacing: 0.02 * 20
                        horizontalAlignment: Text.AlignLeft
                        lineHeight: 21.76
                        font.bold: true
                    }


                    Text {
                        id: datetext
                        text: qsTr("3/22/2023")
                        color: "#6D6D6D"
                        y: 333
                        x: 292
                        font.family: "Archivo"
                        font.pixelSize: 20
                        font.weight: Font.Bold
                        font.letterSpacing: 0.02 * 20
                        horizontalAlignment: Text.AlignLeft
                        lineHeight: 21.76
                        font.bold: true
                    }


                    Text {
                        id: expiredtext
                        text: qsTr("Expired")
                        color: "#F08C5A"
                        y: 333
                        x: 411
                        font.family: "Archivo"
                        font.pixelSize: 20
                        font.weight: Font.Bold
                        font.letterSpacing: 0.02 * 20
                        horizontalAlignment: Text.AlignLeft
                        lineHeight: 21.76
                        font.bold: true
                    }
                }

                parent: Overlay.overlay

            }

        }

        Button {
            id: scannerbutton
            width: 128
            height: 160

            background: Rectangle{
                color: "white"
                anchors.fill: scannerbutton
                radius: 4
            }

            Image {
                id: scannerimage
                source: "../Assets/scanner.png"
                x: 25
                y: 30
            }

            Text {
                id: scannertext
                text: qsTr("Scanner")
                x: 28.5
                y: 124
                color: "#6D6D6D"
                font.family: "Archivo"
                font.pixelSize: 18
                font.weight: Font.DemiBold
                font.letterSpacing: 0.02 * 18
                horizontalAlignment: Text.AlignHCenter
            }

            MouseArea {
                anchors.fill: scannerbutton
                onClicked: {
                    scannerpopup.open()
                    graypopuprect.z = root.z + 1
//                    graypopuprect.visible = true
                    graypopuprect.opacity = 0.9
                    backbuttoninpopup.opacity = 1
                    backbuttoninpopup.visible = true
                    bgblur.radius = 70
                }

            }

            Popup {
                id: scannerpopup
                parent: Overlay.overlay

                background:
                    Rectangle {
                    color: "white"
                    x: 100
                    y: 100
                    width: 100
                    height: 100

                }

//                    Row {
//                        id: scannerpopuprow
//                        x: 363
//                        y: 140 + 92
//                        spacing: 36

//                        Button {
//                            id: uploadbutton
//                            width: 259
//                            height: 364

//                            background:
//                                Rectangle {
//                                id: uploadrect
//                                color: "white"
//                                radius: 4
//                            }

//                            onClicked: {
//                                uploadtoserverrect.color.a = 0.6
//                            }

//                            CircularProgressBar {
//                                x: 41.5
//                                y: 40
//                                id: uploadprogress
//                                degree: 0.3

//                                Text {
//                                    text: parseInt(uploadprogress.degree * 100)
//                                    anchors.centerIn: uploadprogress
//                                    color: uploadprogress.maincolor
//                                    font.family: "Archivo"
//                                    font.pixelSize: 32
//                                    font.weight: Font.Bold
//                                    font.letterSpacing: 0.02 * 32
//                                    horizontalAlignment: Text.AlignLeft
//                                }
//                            }

//                            Rectangle {
//                                id: uploadtoserverrect
//                                width: 179
//                                height: 44
//                                radius: 4
//                                x: 40
//                                y: 280
//                                color: "#4696FA"

//                                Text {
//                                    id: uploadtoservertext
//                                    x: 24
//                                    y: 9
//                                    text: qsTr("Upload to server")
//                                    color: "white"
//                                    font.family: "Archivo"
//                                    font.pixelSize: 18
//                                    font.weight: Font.DemiBold
//                                    font.letterSpacing: 0.02 * 18
//                                    horizontalAlignment: Text.AlignLeft
//                                    lineHeight: 19.58
//                                    font.bold: true
//                                }

//                            }

//                        }

//                        Button {
//                            id: downloadbutton
//                            width: 259
//                            height: 364

//                            background:
//                                Rectangle {
//                                id: downloadrect
//                                color: "white"
//                                radius: 4

//                            }

//                            onClicked: {
//                                getfromserverrect.color.a = 0.6
//                            }

//                            CircularProgressBar {
//                                x: 41.5
//                                y: 40
//                                id: downloadprogress
//                                degree: 0.58

//                                Text {
//                                    text: parseInt(downloadprogress.degree * 100)
//                                    anchors.centerIn: downloadprogress
//                                    color: downloadprogress.maincolor
//                                    font.family: "Archivo"
//                                    font.pixelSize: 32
//                                    font.weight: Font.Bold
//                                    font.letterSpacing: 0.02 * 32
//                                    horizontalAlignment: Text.AlignLeft
//                                }
//                            }

//                            Rectangle {
//                                id: getfromserverrect
//                                width: 179
//                                height: 44
//                                radius: 4
//                                x: 40
//                                y: 280
//                                color: "#4696FA"

//                                Text {
//                                    id: getfromservertext
//                                    x: 24
//                                    y: 9
//                                    text: qsTr("Get from server")
//                                    color: "white"
//                                    font.family: "Archivo"
//                                    font.pixelSize: 18
//                                    font.weight: Font.DemiBold
//                                    font.letterSpacing: 0.02 * 18
//                                    horizontalAlignment: Text.AlignLeft
//                                    lineHeight: 19.58
//                                    font.bold: true
//                                }

//                            }

//                        }

//                    }




            }

        }

        Button {
            id: lightbutton
            width: 128
            height: 160
            z: 1

            background: Rectangle{
                color: "white"
                anchors.fill: lightbutton
                radius: 4
            }

            Image {
                id: lightsimage
                source: "../Assets/light.png"
                x: 30
                y: 30
                z: 1
            }

            Text {
                id: lighttext
                text: qsTr("Lights")
                x: 38
                y: 124
                color: "#6D6D6D"
                font.family: "Archivo"
                font.pixelSize: 18
                font.weight: Font.DemiBold
                font.letterSpacing: 0.02 * 18
                horizontalAlignment: Text.AlignHCenter
            }
        }

        Button {
            id: soundbutton
            width: 128
            height: 160

            background: Rectangle{
                color: "white"
                anchors.fill: soundbutton
                radius: 4
            }

            Image {
                id: soundimage
                source: "../Assets/sound.png"
                x: 28
                y: 30
            }

            Text {
                id: soundtext
                text: qsTr("Sound")
                x: 36
                y: 124
                color: "#6D6D6D"
                font.family: "Archivo"
                font.pixelSize: 18
                font.weight: Font.DemiBold
                font.letterSpacing: 0.02 * 18
                horizontalAlignment: Text.AlignHCenter
            }

        }

        Button {
            id: backbutton
            width: 128
            height: 160
            z: 1

            background: Rectangle{
                color: "#BDBDBDCC"
                anchors.fill: backbutton
                radius: 4
            }

            Image {
                id: backimage
                source: "../Assets/arrow.png"
                x: 30.36
                y: 30
            }

            Text {
                id: backtext
                text: qsTr("Back")
                x: 45
                y: 124
                color: "#6D6D6D"
                font.family: "Archivo"
                font.pixelSize: 18
                font.weight: Font.DemiBold
                font.letterSpacing: 0.02 * 18
                horizontalAlignment: Text.AlignHCenter
            }

        }


    }

    Rectangle {
        id: graypopuprect
        color: "#8282a7"
        width: 1280
        height: 708
        x: 0
        y: 92
        visible: true
        opacity: 0
    }

    Button {
        id: backbuttoninpopup
        width: 92
        height: 92
        x: 0
        y: 0
        opacity: 0

        background: Rectangle {
            id: arrowpopuprect
            color: "#EDEDED"
        }

        Image {
            id: arrowpopup
            source: "../Assets/arrow_popup.png"
            width: 40
            height: 36
            x: 26
            y: 28
        }

        onClicked: {
            root.backbuttonClicked()
            console.log("Signal backbutton clicked")
            backbuttoninpopupanim.running = true
            weightpopup.close()
            scannerpopup.close()
            graypopuprect.z = root.z - 1
            graypopuprect.opacity = 0
            backbuttoninpopup.opacity = 0
            backbuttoninpopup.visible = false
            console.log("clicked on back")
        }


        PropertyAnimation {
            id: backbuttoninpopupanim
            duration: 200
            target: backbuttoninpopup
            property: "opacity"
            from: 0
            to: 1
            easing.type: Easing.InOutQuad
        }
    }

}

