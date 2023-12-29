import QtQuick 2.15
import QtGraphicalEffects 1.15
import "../Utiles" as Util
import "../Components"
import KAST.Logic 1.0


Item {
    id: root
    signal back()
    width: 890
    height: 800

    property Logic obj_LogicContainerPLUListItems

    Image {
        source: "../../Assets/StackBackground.png"
        anchors.fill: parent
    }
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
            text: obj_LogicContainerPLUListItems.lang.txt_Lookup_Items
            color: "#6D6D6D"
            font.pixelSize: 24
            lineHeight: Font.Normal
            font.weight: Font.DemiBold
            x: 0
            y: -(94 -28)
        }

        Rectangle{
            id:input_enterName
            width: 300
            height: 56
            color: "white"
            radius: 5
            border.color: "#C6C5CE"
            x: 527
            y: -(104 -28)
            TextEdit{
                id:txt_Name
                anchors.fill: parent
                font.pixelSize: 20
                layer.enabled: true
                x:50
                //horizontalAlignment: TextInput.AlignHCenter
                verticalAlignment:  TextInput.AlignVCenter
                font.family: viewset.danaFuNumFont
                property string placeholderText: ""

                onFocusChanged: {
                    kkey.visible = true
                }
                Text {
                    text: txt_Name.placeholderText
                    color: "white"
                    visible: !txt_Name.text
                    font.pixelSize: 18
                    anchors.verticalCenter: parent.verticalCenter
                    x:50
                    //anchors.horizontalCenter: parent.horizontalCenter
                    font.family: viewset.danaFuNumFont
                }

                onTextChanged: {
                    obj_LogicContainerPLUListItems.shopPage.search_plu(txt_Name.text)
                }
            }
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

                MouseArea{
                    anchors.fill: parent
                    onClicked: {
                        obj_LogicContainerPLUListItems.shopPage.item_PLUClicked(model.barcode)
                    }
                }

                Image {
                    id: productimage
                    source: model.pic
                    width: 110
                    height: 110
                    anchors.horizontalCenter: parent.horizontalCenter
                    y: 8
                }

                Text {
                    text: "# "+model.barcode
                    x: 16
                    y: 134
                    font.pixelSize: 16
                    color: "#9D9D9D"
                    lineHeight: Font.Normal
                }
                Text {
                    text: model.name
                    width: parent.width -16
                    elide: Text.ElideRight
                    x: 16
                    y: 163
                    font.pixelSize: 24
                    color: "#1D1D1D"
                    lineHeight: Font.Normal
                }

                Text {
                    text: model.savingQML
                    x: 16
                    y: 198
                    font.pixelSize: 10
                    color: "#36EB00"
                    lineHeight: Font.Normal
                    font.bold: true
                }

                Text {
                    text: model.finalPriceQML
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

    KKeyboard{
        id:kkey
        inputtext:txt_Name
        leftpad:-50
        toppad:-500
        x:-390
        y:input_enterName.y + 240 + 58
        anchors.top: input_enterPassword.bottom
        visible: false
    }



    KButton{
        x:32
        y:640
        text: "< " + obj_LogicContainerPLUListItems.lang.btn_Back
        width: 120
        borderRadius: 5
        onClicked: {
            root.back()
        }
    }
}


