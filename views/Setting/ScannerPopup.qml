import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import QtGraphicalEffects 1.12
import QtQuick.Window 2.14
import "../Components"


Popup {
    id: sensorPopup
    
    topMargin: 0
    bottomMargin: 0
    x: 0
    focus: true
    closePolicy: Popup.CloseOnEscape | Popup.CloseOnPressOutsideParent
    background:Item{
        width: 375
        height: 450
        x: 453
        y: 166
        
        Rectangle {
            anchors.fill: parent
            color: "white"
            layer.enabled: true
            layer.effect: DropShadow {
                horizontalOffset: 1
                verticalOffset: 1
                radius: 10
                samples: 16
                color: "#d3d3d3"
            }
            
            
            Text {
                Layout.fillWidth: true
                text: "Please scan the \nitem barcode"
                font.pixelSize: 32
                color: "black"
                x: 40
                y: 40
                font.bold: true
            }
            
            Image {
                source: "../../Assets/testBarcode.png"
                x:40
                y:176
            }
            
            Rectangle{
                width: 306
                x:40
                y:306
                height: 56
                color: "#F7F7F7"
                
                Text {
                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.verticalCenter: parent.verticalCenter
                    text: "text"
                }
            }
            KButton{
                text: "close"
                y:370
                x:40
                width: 306
                borderRadius: 5
                onClicked: {
                    sensorPopup.close()
                }
            }
        }
    }
}
