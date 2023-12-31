import QtQuick 2.15
import QtGraphicalEffects 1.15
import "../Utiles" as Util
import "../Components"
import KAST.Logic 1.0


Item {
    id: root
    signal back()

    property Logic obj_LogicContainerLstSpecialDeals

    Image {
        source: "../../Assets/StackBackground.png"
        anchors.fill: parent
    }

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
            text: obj_LogicContainerLstSpecialDeals.lang.txt_Special_Deals
            color: "#6D6D6D"
            font.pixelSize: 24
            lineHeight: Font.Normal
            font.weight: Font.DemiBold
            x: 0
            y: -(94 -  28)
        }

        model: obj_LogicContainerLstSpecialDeals.shopPage.offersList
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
                        source: model.pic
                        width: 106
                        height: 106
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.horizontalCenter: parent.horizontalCenter
                    }
                }

                Text {
                    text: model.name
                    width: 134
                    height: 66
                    x:164
                    y:20
                    font.pixelSize: 16
                    wrapMode: Text.WordWrap
                }
                Text {
                    x:164
                    y:90
                    text:model.finalPriceQML
                    font.pixelSize: 20
                    color:viewset.primaryColor
                    font.bold: true
                }
                Text {
                    x:248
                    y:98
                    text: "-9 %"
                    font.pixelSize: 24
                    color: viewset.primaryColor
                    visible: false
                }
            }
        }

    }

    KButton{
        x:32
        y:640
        width: 120
        text: "< " + obj_LogicContainerLstSpecialDeals.lang.btn_Back
        borderRadius: 5
        onClicked: {
            root.back()
        }
    }
}
