import QtQuick 2.15
import QtGraphicalEffects 1.15
import "../Utiles" as Util
import "../Components"
import KAST.Logic 1.0


Item {
    id: root
    signal back()

    property Logic obj_LogicContainerPLUListItems


    GridView {
        id: productsgridview
        width: 890
        height: 640
        cellWidth: 190 + 22
        cellHeight: 249 + 16
        focus: true
        x: 32
        y: 94
        flow: GridView.FlowTopToBottom
        Text {
            text: "PLU Items"
            color: "#6D6D6D"
            font.pixelSize: 24
            lineHeight: Font.Normal
            font.weight: Font.DemiBold
            x: 0
            y: -(94 -28)
        }

        model: obj_LogicContainerPLUListItems.shopPage.pluList
        delegate:
            Item {
            Rectangle {
                id: mainrect
                width: 190
                height: 249
                color: "white"
                radius: 4

                Image {
                    id: productimage
                    source: model.pic
                    width: 120
                    height: 120
                    anchors.horizontalCenter: parent.horizontalCenter
                    y: 8
                }

                Text {
                    text: "# "+model.barcode
                    x: 16
                    y: 144
                    font.pixelSize: 16
                    color: "#9D9D9D"
                    lineHeight: Font.Normal
                }
                Text {
                    text: model.name
                    x: 16
                    y: 173
                    font.pixelSize: 24
                    color: "#1D1D1D"
                    lineHeight: Font.Normal
                }

                Text {
                    text: "$ "+model.finalPrice+"/kg"
                    x: 16
                    y: 211
                    font.pixelSize: 20
                    color: "#F08C5A"
                    lineHeight: Font.Normal
                    font.bold: true
                }

            }

        }
    }



    KButton{
        x:32
        y:640
        text: "< Back"
        width: 120
        borderRadius: 5
        onClicked: {
            root.back()
        }
    }
}


