import QtQuick 2.15
import KAST.Logic 1.0


Item {
    id:root
    width: 890
    height: 708
    property Logic obj_LogicContainerAddPluItems



    signal back()
    signal seeAll()

    Text {
        text: "Search Results"
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
            text: "#0000"
        }
        Text {
            x:204
            y:106
            font.pixelSize: 24
            font.bold: true
            color: "#D9D9D9"
            text: "Name"
        }
        Text {
            x:204
            y:156
            font.pixelSize: 24
            font.bold: true
            color: "#D9D9D9"
            text: "$ 0.0 /kg"
        }
    }
    Rectangle{
        width: 398
        height: 249
        x:32
        y:359
        radius: 4
        Text {
            text: "How to add PLU items"
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
        text: "Recomended"
        x:462
        y:40
        font.pixelSize: 24
        color: "#6D6D6D"

    }
    GridView {
        id: productsgridview
        x:462
        width: 410
        height: 640
        cellWidth: 190 + 22
        cellHeight: 249 + 16
        focus: true
        y: 94
        flow: GridView.FlowTopToBottom
        clip: true
        interactive: false


        model: obj_LogicContainerPLUListItems.shopPage.pluTopFour
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

    Rectangle{
        x:741
        y:640
        Text {
            text: "See All >"
            font.pixelSize: 24
            MouseArea{
                anchors.fill: parent
                onClicked: {
                    root.seeAll()
                }
            }
        }
    }

    Rectangle{
        x:32
        y:640
        Text {
            text: "< Back"
            font.pixelSize: 24

            MouseArea{
                anchors.fill: parent
                onClicked: {
                    root.back()
                }
            }
        }
    }
}
