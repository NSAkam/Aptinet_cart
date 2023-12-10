import QtQuick 2.15
import QtGraphicalEffects 1.15
import "../Utiles" as Util
import "../Components"
import KAST.Logic 1.0


Item {
    id: root
    width: 572
    height: 450

    property Logic obj_LogicContainerAddPluItemsCountedView

    Image {
        source: "../../Assets/StackBackground.png"
        anchors.fill: parent
    }

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
            source: obj_LogicContainerAddPluItemsCountedView.shopPage.newProduct.pic
            width: 185
            height: 185
            x: 32
            y: 24
        }

        Text {
            id: productidtext
            text: "#" + obj_LogicContainerAddPluItemsCountedView.shopPage.newProduct.barcode
            x: 248
            y: 58
            font.pixelSize: 24
            color: "#9D9D9D"

        }

        Text {
            id: productnametext
            text: obj_LogicContainerAddPluItemsCountedView.shopPage.newProduct.name
            x: 248
            y: 100
            font.pixelSize: 36
            font.bold: true
            color: "#1D1D1D"

        }

        Text {
            id: unitpricetext
            text:obj_LogicContainerAddPluItemsCountedView.shopPage.newProduct.finalPriceQML
            x: 248
            y: 149
            font.pixelSize: 24
            font.weight: Font.DemiBold
            color: "#F08C5A"

        }
        Text {
            id: unitpricetext1
            text: obj_LogicContainerAddPluItemsCountedView.shopPage.newProduct.savingQML
            x: 248
            y: 196
            font.pixelSize: 20
            font.weight: Font.DemiBold
            color: "#36EB00"

        }

        Text{
            text: "Quantity"
            x:44
            y:275
        }
        Rectangle{
            width: 24
            height: 24
            color: "#4696FA"
            x:146
            y:281
            Text {
                text: qsTr("-")
                color: "white"
                anchors.verticalCenter: parent.verticalCenter
                anchors.horizontalCenter: parent.horizontalCenter
                font.pixelSize: 48
            }
            MouseArea{
                anchors.fill: parent
                onClicked: {
                    obj_LogicContainerAddPluItemsCountedView.shopPage.decrease_PLUClicked()
                }
            }
        }
        Text {
            text:obj_LogicContainerAddPluItemsCountedView.shopPage.newProduct.mountQML
            color: "black"
            x:186
            y:275
            font.pixelSize: 24
        }
        Rectangle{
            width: 24
            height: 24
            color: "#4696FA"
            x:217
            y:281
            Text {
                text: qsTr("+")
                color: "white"
                anchors.verticalCenter: parent.verticalCenter
                anchors.horizontalCenter: parent.horizontalCenter
                font.pixelSize: 24
            }
            MouseArea{
                anchors.fill: parent
                onClicked: {
                    obj_LogicContainerAddPluItemsCountedView.shopPage.increase_PLUClicked()
                }
            }
        }

        Text {
            id: totalpricevalue
            text: obj_LogicContainerAddPluItemsCountedView.shopPage.newProduct.totalFinalPriceQML
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
                obj_LogicContainerAddPluItemsCountedView.shopPage.confirm_PLUItemClicked()
            }
        }

    }
}
