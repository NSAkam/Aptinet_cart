import QtQuick 2.15
import QtGraphicalEffects 1.15
import "../Utiles" as Util
import "../Components"

Item {
    id: root
    signal back()

    GridView {
        id: productsgridview
        width: 890
        height: 640
        cellWidth: 346
        cellHeight:  164

        focus: true
        x: 32
        y: 94
        flow: GridView.FlowTopToBottom
        Text {
            text: qsTr("PLU Items")
            color: "#6D6D6D"
            font.pixelSize: 24
            lineHeight: Font.Normal
            font.weight: Font.DemiBold
            x: 0
            y: -(94 -  28)
        }

        model: 15
        delegate:

            Item {
            width: 326
            height: 144
            Rectangle{
                width: 326
                height: 144
                color: "white"
                opacity: 0.3
            }

            Rectangle{
                width: 326
                height: 144
                color: "transparent"

                Rectangle{
                    width: 144
                    height: 144
                    color: "white"

                    Image {
                        source: "../../Assets/product.png"
                        width: 106
                        height: 106
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.horizontalCenter: parent.horizontalCenter
                    }
                }

                Text {
                    text: qsTr("Nutella Hazelnut Spread with Cocoa, 750g")
                    width: 134
                    height: 66
                    x:164
                    y:20
                    font.pixelSize: 16
                    wrapMode: Text.WordWrap
                }
                Text {
                    x:164
                    y:98
                    text: qsTr("$ 9.99")
                    font.pixelSize: 24
                    color:viewset.primaryColor
                    font.bold: true
                }
                Text {
                    x:248
                    y:98
                    text: qsTr("-9 %")
                    font.pixelSize: 24
                    color: viewset.primaryColor
                }
            }
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
                    console.log("asdasdasd")
                    root.back()
                }
            }
        }
    }


}
