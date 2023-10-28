import QtQuick 2.15
import QtGraphicalEffects 1.15
import "../Utiles" as Util
import "../Components"

Item {
    id: root
    signal closepanel()

    GridView {
        id: productsgridview
        width: 890
        height: 640
        //    spacing: 16 /*22*/
        //    flickableDirection: Flickable.HorizontalFlick
        //    orientation: ListView.Horizontal
        cellWidth: 190 + 22
        cellHeight: 249 + 16
        focus: true
        x: 32
        y: 94
//        flow: GridView.LeftToRight

        onMovingHorizontallyChanged: {
//            productsgridview.currentIndex = theCircle.index
            console.log("Moving...")
        }

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
            Rectangle {
                id: mainrect
                width: 190
                height: 249
                color: "white"
                radius: 4

                DropShadow {
                    anchors.fill: mainrect
                    cached: true
                    horizontalOffset: 0
                    verticalOffset: 8
                    radius: 16.0
                    y: 5
                    samples: 30
                    color: "#0000000A"
                    smooth: true
                    source: mainrect
                    visible: shadow?true:false

                    Image {
                        id: productimage
                        source: index === 1 ? "../../Assets/Ads.png" : "../../Assets/product.png"
                        width: 114
                        height: 86
                        x: 38
                        y: 29
                    }

                    Text {
                        text: qsTr("#2540")
                        x: 16
                        y: 144
                        font.pixelSize: 16
                        color: "#9D9D9D"
                        lineHeight: Font.Normal
                    }
                    Text {
                        text: qsTr("Apple")
                        x: 16
                        y: 173
                        font.pixelSize: 24
                        color: "#1D1D1D"
                        lineHeight: Font.Normal
                    }

                    Text {
                        text: qsTr("$ 2.99/kg")
                        x: 16
                        y: 211
                        font.pixelSize: 20
                        color: "#F08C5A"
                        lineHeight: Font.Normal
                    }

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
                    root.closepanel()
                }
            }
        }
    }


    Row {
        property int currentPage: 0

        id: circlesRow
        y: 650
        x:  421
        spacing: 8

        Repeater {
            model: Math.ceil(productsgridview.model / 8)

            delegate: Rectangle {
                id: theCircle
                width: 12
                height: 12
                radius: width / 2
                color: index === productsgridview.currentIndex ? viewset.primaryColor : "#F8C6AD"


                MouseArea {
                    anchors.fill: parent
                    onClicked: {
                        productsgridview.currentIndex = index
//                        console.log("index is", index)
//                        console.log("currentIndex: ", productsgridview.currentIndex)
                    }
            }
        }
    }

}
}
