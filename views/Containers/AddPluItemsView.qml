import QtQuick 2.15
import QtGraphicalEffects 1.15
import "../Utiles" as Util
import "../Components"


Item {
    id: root
    width: 572
    height: 450

    Rectangle{
        id: viewitemrect
        width: parent.width
        height: parent.height
        x: 159
        y: 120
        color: "white"
        radius: 4

        Image {
            id: productimage
            source: "../../Assets/product.png"
//            width: 158.57
//            height: 121.57
            x: 45.21
            y: 55.71
        }

        Text {
            id: productidtext
            text: qsTr("#8560")
            x: 248
            y: 58
            font.pixelSize: 24
            color: "#9D9D9D"

        }

        Text {
            id: productnametext
            text: qsTr("Pineapple")
            x: 248
            y: 100
            font.pixelSize: 36
            font.bold: true
            color: "#1D1D1D"

        }

        Text {
            id: unitpricetext
            text: qsTr("$ 6.99/kg")
            x: 248
            y: 149
            font.pixelSize: 24
            font.weight: Font.DemiBold
            color: "#F08C5A"

        }

        Image {
            id: weightimage
            source: "../../Assets/weight.png"
            x: 44
            y: 264
        }

        Text {
            id: addtocarttext
            text: qsTr("Add to cart\nto be calculated")
            font.pixelSize: 20
            x: 108
            y: 262
            color: "#9D9D9D"
        }

        Text {
            id: totalpricevalue
            text: qsTr("$ 0.0")
            x: 428
            y: 241
            font.pixelSize: 32
            font.bold: true
            color: "#4696FA"
        }

        Text {
            id: totalpricetext
            text: qsTr("Total Price")
            x: 406
            y: 288
            font.pixelSize: 24
            color: "#9D9D9D"
        }

        KButton{
            text: "Cancel"
            x: 32
            y: 354
            btn_width: 225
            btn_height: 64
            borderRadius: 4
            btn_color: viewset.primaryColor
        }

        KButton {
            text: "Confirm"
            x: 273
            y: 354
            btn_width: 267
            btn_height: 64
            borderRadius: 4
            btn_color: viewset.secondaryColor
            btn_bordercolor: viewset.secondaryColor

            Image {
                source: "../../Assets/goRightInItemView.png"
                x: 226
                y: 24

            }
        }

    }

    DropShadow {
        anchors.fill: viewitemrect
        cached: true
        horizontalOffset: 0
        verticalOffset: 8
        radius: 2
        y: 5
        samples: 30
        color: "#0000000A"
        smooth: true
        source: viewitemrect
        visible: shadow?true:false
    }



}