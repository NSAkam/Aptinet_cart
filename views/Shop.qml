import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15
import QtQuick.Window 2.0
import QtQuick.Controls.Styles 1.4
import QtGraphicalEffects 1.0
import "Components"
import "Containers"
import "Utiles" as Util


Item {

    width: 1280
    height: 800

    Util.ViewSettings{
        id:viewset
    }

    Image {
        source: "file://../Assets/AuthenticationBackground.png"
        anchors.fill: parent
    }

    Rectangle{
        width: parent.width
        height: 92
        x:0
        y:0
    }
    Item{
        id:top_Panel
        width: parent.width
        height: 92
        Rectangle{
            width: parent.width
            height: parent.height
            x:0
            y:0
            Rectangle{
                width: 50
                height: 50
                color: viewset.primaryColor
                x:421
                y:25
                radius: width /2
            }
            Text {
                text: qsTr("user Email")
                color: "#6D6D6D"
                width: 148
                height: 15
                font.pixelSize: 14
                x:478
                y:40
            }
            KButton{
                btn_color: "#9D9D9D"
                x:995
                y:32
                borderRadius: 5
                width: 149
                height: 40
                text: "Add PLU Items"
                btn_borderWidth:0
                fontsize: 16
                ishover: false
            }
            Image {
                source: "file://../Assets/Help.png"
                width: 57
                height: 57
                x:1156
                y:25
            }
            Image {
                source: "file://../Assets/Notification.png"
                width: 57
                height: 57
                x:1208
                y:25
            }

        }
    }

    Item {
        id:main_Panel
        Text {
            text: qsTr("To add an item,\n scan its barcode or\n tap the button below.")
            width: 369
            height: 144
            x:261+ 390
            y:326
            font.pixelSize: 36
            color: "#9D9D9D"
            horizontalAlignment:  TextInput.AlignHCenter
        }

        StackView
        {
            id:stackviewContainer
            width: 890
            height: 708
            x:390
            y:92
            //initialItem: lstProductHandler
            initialItem:addPluItem
            onDepthChanged: {
                obj_LogicContainer.shoppage.stackviewDepthChanged(stackviewContainer.depth)
            }
        }
    }

    Item{
        id:leftPanel
        width: 390
        height: parent.height

        Image {
            id:rect_Suggestion
            source: "file://../Assets/leftSideBar.png"
            anchors.fill: parent

        }
        Image {
            source: "file://../Assets/AptinetText.png"
            x:0
            y:0
        }
        Image {
            id: img_UserCaptured
            source: "file://../Assets/UserImage.png"
            width: 326
            height: 184
            x:32
            y:105
        }
        Item{
            id:addPlupanel
            width: parent.width
            Text {
                text: qsTr("ENTER PLU CODE")
                font.pixelSize: 24
                font.bold: true
                x:32
                y:327
            }
            Rectangle{
                id:rectEnterPLU
                x:32
                y:378
                width: 326
                height: 56
                color: "#F1F1F1"
                radius: 4
                TextInput{
                    id:txt_PLUBarcodeInput
                    anchors.fill: parent
                    font.pixelSize: 18
                    layer.enabled: true
                    horizontalAlignment: TextInput.AlignHCenter
                    verticalAlignment:  TextInput.AlignVCenter
                    font.family: viewset.danaFuNumFont
                    property string placeholderText: " "

                    onFocusChanged: {
                        numpad.inputtext = txt_PLUBarcodeInput
                    }
                    Text {
                        text: txt_PLUBarcodeInput.placeholderText
                        color: "#C6C5CE"
                        visible: !txt_PLUBarcodeInput.text
                        font.pixelSize: 18
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.horizontalCenter: parent.horizontalCenter
                        font.family: viewset.danaFuNumFont
                    }
                }
            }
            Numpad{
                anchors.top: rectEnterPLU.bottom
                anchors.topMargin: 30
                x:32
            }
        }

        Item {
            id: adsPanel
            visible: false
            Image {
                id: ads_Image
                source: "file://../Assets/Ads.png"
                width: 326
                height: 184
                x:32
                y:309
            }
            Text {
                text: qsTr("Special Deals")
                font.pixelSize: 24
                color: "white"
                x:32
                y:521
                font.bold: true
            }
            ListView {
                id:slideshow
                width: 326
                height: 800 - y
                x:32
                y:571

                clip: true
                spacing: 10
                model: 10
                orientation: ListView.vertical
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
                                source: "file://../Assets/product.png"
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
        }
    }

    Component{
        id:newProductHandler
        BarcodeScanned{
            tanzimat:obj_LogicContainer
        }
    }

    Component{
        id:lstProductHandler
        LstCheckProducts{
            tanzimat:obj_LogicContainer
        }
    }

    Component{
        id:manualBarcodeHandler
        ManualBarcode{

            tanzimat: obj_LogicContainer
        }
    }
    Component{
        id:addPluItem
        AddPluItems{

        }
    }
}