
import QtQuick 2.15
import QtQuick.Window 2.12
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.0


Popup {
    id: dataEntryPopup

    Rectangle {
        width: 652
       height: 72
       color: "#4696FA"
       x:  542
       y: 223
       radius: 2

       Text {
        text: "Please scan the Product QR Code "
        color: "white"
        font.pixelSize: 24
        font.family: "Archivo"
        font.bold: true
        x: 120
        y: 12
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
            source: "../../Assets/group.png"
            width: 170
            height: 170
            x: 57.5
            y: 57
        }
    }

    Rectangle {
        width: 343
        height: 284
        color: "white"
        x: 851
        y: 315
        radius: 4

        Column {
                spacing: -20
                y: 24

            Text {
                text: "Nutella Hazelnut Spread"
                width: 239
                height: 64
                x: 30
                font.family: "Archivo"
                color: "black"
                font.pixelSize: 20
            }

            Text {
                text: "with Cocoa, 750g"
                width: 239
                height: 64
                x: 40
                font.family: "Archivo"
                color: "black"
                font.pixelSize: 20
            }
            }

        Rectangle {
            width: 295
            height: 64

            Button {
                width: 295
                height: 64
                onClicked: {
                    stackview.push(dataEntry2)
                    toggleRectangles()
                }
                background: Rectangle {
                    color: "#4696FA"
                    radius: 4

                    Text {
                        text: "Save"
                        font.pixelSize: 24
                        color: "white"
                        x: 118
                        y: 19
                    }
                }
                x: 24
                y: 124
            }
        }

        Rectangle {
            width: 295
            height: 56

            Button {
                width: 295
                height: 56
                x: 24
                y: 204
                background: Rectangle {
                    color: "#F5AF8C"

                    Text {
                        text: "Cancel"
                        width: 67
                        height: 22
                        color: "white"
                        font.family: "Archivo"
                        font.pixelSize: 20
                        x: 114
                        y: 17
                    }
                }
            }
        }
    }

    function toggleRectangles() {
            dataEntryPopup.visible = !dataEntryPopup.visible;
        }

    Component {
        id: dataEntry2
        DataEntry2 {}
    }
}
