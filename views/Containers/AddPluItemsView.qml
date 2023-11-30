import QtQuick 2.15
import QtGraphicalEffects 1.15
import "../Utiles" as Util
import "../Components"
import KAST.Logic 1.0


Item {
    id: root
    width: 572
    height: 450

    property Logic obj_LogicContainerAddPluItemsView


    signal cancel()
    signal confirm()

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
            width: 185
            height: 185
            x: 32
            y: 24
        }

        Text {
            id: productidtext
            text: "#8560"
            x: 248
            y: 58
            font.pixelSize: 24
            color: "#9D9D9D"

        }

        Text {
            id: productnametext
            text: "Pineapple"
            x: 248
            y: 100
            font.pixelSize: 36
            font.bold: true
            color: "#1D1D1D"

        }

        Text {
            id: unitpricetext
            text: "$ 6.99/kg"
            x: 248
            y: 149
            font.pixelSize: 24
            font.weight: Font.DemiBold
            color: "#F08C5A"

        }

        Image {
            id: weightimage
            source: "../../Assets/weighticon.png"
            width: 48
            height: 48
            x: 44
            y: 264
        }

        Text {
            id: addtocarttext
            text: "Add to cart\nto be calculated"
            font.pixelSize: 20
            x: 108
            y: 262
            color: "#9D9D9D"
        }

        Text {
            id: totalpricevalue
            text: "$ 0.0"
            x: 428
            y: 241
            font.pixelSize: 32
            font.bold: true
            color: "#4696FA"
        }

        Text {
            id: totalpricetext
            text: "Total Price"
            x: 406
            y: 288
            font.pixelSize: 24
            color: "#9D9D9D"
        }

        KButton{
            text: "Cancel"
            x: 32
            y: 354
            borderRadius: 4
            btn_color: viewset.primaryColor
            width: 225
            height: 64
            onClicked: {
                root.cancel()
            }
        }

        KButton {
            text: "Confirm"
            x: 273
            y: 354
            width: 267
            height: 64
            borderRadius: 4
            btn_color: viewset.secondaryColor
            btn_bordercolor: viewset.secondaryColor

            Image {
                source: "../../Assets/goRightInItemView.png"
                x: 226
                y: 24

            }
            onClicked: {
                root.confirm()
            }
        }

    }
}
