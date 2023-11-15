import QtQuick 2.15

Item {
    id:root
    width: 890
    height: 708

    signal closepanel()

    Text {
        text: qsTr("Search Results")
        x:32
        y:40
        font.pixelSize: 24
        color: "#6D6D6D"
    }
    Rectangle{
        width: 398
        height: 249
        x:32
        y:94
        radius: 4
        color: white
        Image {
            source: "../../Assets/pluAddItem.png"
            x:32
            y:54
        }
        Text {
            x:204
            y:56
            font.pixelSize: 24
            font.bold: true
            color: "#D9D9D9"
            text: qsTr("#0000")
        }
        Text {
            x:204
            y:106
            font.pixelSize: 24
            font.bold: true
            color: "#D9D9D9"
            text: qsTr("Name")
        }
        Text {
            x:204
            y:156
            font.pixelSize: 24
            font.bold: true
            color: "#D9D9D9"
            text: qsTr("$ 0.0 /kg")
        }
    }
    Rectangle{
        width: 398
        height: 249
        x:32
        y:359
        radius: 4
        Text {
            text: qsTr("How to add PLU items")
            anchors.horizontalCenter:  parent.horizontalCenter
            y:35
            font.pixelSize: 24
            font.bold: true
        }
        Image {
            source: "../../Assets/addPluItemsSteps.png"
            x:32
            y:113
        }
    }

    Text {
        text: qsTr("Recomended")
        x:462
        y:40
        font.pixelSize: 24
        color: "#6D6D6D"

    }
    Rectangle{
        width: 190
        height: 249
        x:462
        y:94
        radius: 4
        Image {
            source: "../../Assets/product.png"
            anchors.horizontalCenter: parent.horizontalCenter
            width: 128
            height: 128
        }

        Text {
            text: qsTr("#2540")
            x:16
            y:144
            font.pixelSize: 16
        }
        Text {
            text: qsTr("Apple")
            x:16
            y:173
            font.pixelSize: 24
        }
        Text {
            text: qsTr("$ 2.99/kg")
            x:16
            y:211
            font.pixelSize: 20
            color: viewset.primaryColor
        }
    }

    Rectangle{
        width: 190
        height: 249
        x:668
        y:94
        radius: 4
        Image {
            source: "../../Assets/product.png"
            anchors.horizontalCenter: parent.horizontalCenter
            width: 128
            height: 128
        }

        Text {
            text: qsTr("#2540")
            x:16
            y:144
            font.pixelSize: 16
        }
        Text {
            text: qsTr("Apple")
            x:16
            y:173
            font.pixelSize: 24
        }
        Text {
            text: qsTr("$ 2.99/kg")
            x:16
            y:211
            font.pixelSize: 20
             color: viewset.primaryColor
        }
    }

    Rectangle{
        width: 190
        height: 249
        x:462
        y:359
        radius: 4
        Image {
            source: "../../Assets/product.png"
            anchors.horizontalCenter: parent.horizontalCenter
            width: 128
            height: 128
        }

        Text {
            text: qsTr("#2540")
            x:16
            y:144
            font.pixelSize: 16
        }
        Text {
            text: qsTr("Apple")
            x:16
            y:173
            font.pixelSize: 24
        }
        Text {
            text: qsTr("$ 2.99/kg")
            x:16
            y:211
            font.pixelSize: 20
             color: viewset.primaryColor
        }
    }
    Rectangle{
        width: 190
        height: 249
        x:668
        y:359
        radius: 4
        Image {
            source: "../../Assets/product.png"
            anchors.horizontalCenter: parent.horizontalCenter
            width: 128
            height: 128
        }

        Text {
            text: qsTr("#2540")
            x:16
            y:144
            font.pixelSize: 16
        }
        Text {
            text: qsTr("Apple")
            x:16
            y:173
            font.pixelSize: 24
        }
        Text {
            text: qsTr("$ 2.99/kg")
            x:16
            y:211
            font.pixelSize: 20
             color: viewset.primaryColor
        }
    }

    Rectangle{
        x:741
        y:640
        Text {
            text: qsTr("See All >")
            font.pixelSize: 24

        }
    }

    Rectangle{
        x:32
        y:640
        Text {
            text: qsTr("< Back")
            font.pixelSize: 24

            MouseArea{
                anchors.fill: parent
                onClicked: {
                    root.closepanel()
                }
            }
        }
    }
}
