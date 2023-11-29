import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15
import QtQuick.Window 2.0
import "../Components"
import "../Containers"
import "../Utiles"

Popup {
    id: root
    width: 1280
    height: 800
    modal: true
    focus: true
    
    background:
        Rectangle {
        color: "black"
        opacity: 0.4
        x: 0
        y: 0
        width: parent.width
        height: parent.height
    }
    
    Rectangle {
        x: 818 + 390
        y: 32
        radius: 4
        color: "white"
        width: 40
        height: 40
        
        Image {
            source: "../../Assets/alarm.png"
            width: 18
            height: 20
            anchors.centerIn: parent
        }
    }
    
    
    Column {
        spacing: 16
        anchors.verticalCenter: parent.verticalCenter
        anchors.horizontalCenter: parent.horizontalCenter
        Rectangle {
            id: notifrect
            width: 758
            height: 72
            radius: 4
            
            LinearGradient {
                anchors.fill: parent
                start: Qt.point(0, 10)
                end: Qt.point(72, 60)
                gradient: Gradient {
                    GradientStop { position: 0.5417; color: "#F08C5A" }
                    GradientStop { position: 1.0; color: "#F05A28" }
                }
            }
            
            Text {
                anchors.fill: notifrect
                text: qsTr("Are you sure to remove the products?")
                font.bold: true
                font.pixelSize: 24
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                color: "white"
            }
        }
        
        Rectangle{
            width: 758
            height: 300
            
            
            
            ListView {
                id:slideshow
                width: 758
                height: 210
                clip: true
                spacing: 10
                model: 10
                orientation: ListView.vertical
                delegate:Item{
                    width: 758
                    height: 140
                    Rectangle {
                        anchors.fill: parent
                        color: "white"
                        Image {
                            source: "../../Assets/product.png"
                            x: 41
                            y: 41
                            width: 90
                            height: 90
                        }
                        Text {
                            text: qsTr("Doritos Tortilla Chips,\nTapatio, 9.75 oz")
                            x: 180
                            y: 40
                            font.pixelSize: 24
                            font.weight: Font.DemiBold
                            color: "black"
                            font.letterSpacing: 0.04 * 24
                            lineHeight: 1.5
                        }
                        
                        Text {
                            text: qsTr("Qty:")
                            x: 647
                            y: 48
                            font.pixelSize: 20
                            //              font.weight: Font.DemiBold
                            color: "#6D6D6D"
                        }
                        
                        Text {
                            text: qsTr("4")
                            x: 695
                            y: 45
                            font.pixelSize: 24
                            font.weight: Font.Bold
                            color: "#F08C5A"
                        }
                        
                        Text {
                            text: qsTr("$ 8.00")
                            x: 615
                            y: 102
                            font.pixelSize: 24
                            font.weight: Font.Bold
                            color: viewset.primaryColor
                        }
                    }
                }
            }
            KButton{
                text: "Confirm"
                borderRadius: 4
                height: 64
                width: 726
                anchors.horizontalCenter: parent.horizontalCenter
                y:230
                btn_color: viewset.secondaryColor
                btn_borderWidth: 0
            }
        }
    }
}