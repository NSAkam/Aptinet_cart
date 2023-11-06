import QtQuick 2.15
import QtQuick.Window 2.12
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.0


Popup {
    id: dataEntryPopup

    background: Rectangle {
        width: 652
       height: 72
       radius: 4
       color: "#4696FA"
       x:  542
       y: 223

       Text {
        text: "Please scan the Product QR Code"
        color: "white"
        font.family: "Archivo"
        font.pixelSize: 24
        width: 412
        height: 48
        x: 120
        y: 17
       }
    }

    Rectangle {
        width: 285
        height: 284
        color: "white"
        x: 542
        y: 315
        radius: 4

        Image {
            source: "/home/mahnaz/akam/ui_aptinet/assets/union2.png"
            width: 170
            height: 170
            x: 57.5
            y: 57
        }

        Image {
            source: "/home/mahnaz/akam/ui_aptinet/assets/scan.png"
            width: 95
            height: 95
            x: 94.5
            y: 94
        }

        Image {
            source: "/home/mahnaz/akam/ui_aptinet/assets/orangeline.png"
            width: 170
            height: 12
            x: 57.5
            y: 136
        }
    }

    Rectangle {
        width: 343
        height: 284
        color: "white"
        x: 851
        y: 315

        Column {
                spacing: -20
                y: 24

            Text {
                text: "Nutella Hazelnut Spread"
                width: 239
                height: 64
                x: 48
                font.family: "Archivo"
                color: "black"
                font.pixelSize: 20
            }

            Text {
                text: "with Cocoa, 750g"
                width: 239
                height: 64
                x: 48
                font.family: "Archivo"
                color: "black"
                font.pixelSize: 20
            }
        }

        Rectangle {
            width: 295
            height: 64
            x: 24
            y: 124

            Button {
                width: 295
                height: 64
                // x: 24
                // y: 200
                background: Rectangle {
                    color: "#4696FA"
                    radius: 4
                }
                onClicked: {
                    stackview.push(dataEntry4)
                }
            }

            Text {
                text: "Save"
                width: 59
                height: 26
                color: "white"
                x: 118
                y: 19
                font.pixelSize: 24
                font.family:"Archivo"
            }
        }

        Rectangle {
            width: 295
            height: 56
            x: 24
            y: 204

            Button {
                width: 295
                height: 56
                background: Rectangle {
                    color: "#F5AF8C"
                    radius: 4
                }
                onClicked: {
                    stackview.push(dataEntry4)
                }
            }

            Text {
                text: "Cancel"
                width: 67
                height: 22
                x: 114
                y: 17
                color: "white"
                font.pixelSize: 20
            }
        }
    }

Component  {

    id:dataEntry4
    DataEntry4{}
}

}