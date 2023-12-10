import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import QtGraphicalEffects 1.12
import QtQuick.Window 2.14
import "../Components"
import KAST.Logic 1.0



Popup {
    id: weightsesnsorPopup
    
    property Logic obj_LogicWeightSensorPopUp 
    
    
    topMargin: 0
    bottomMargin: 0
    x: 0
    focus: true
    closePolicy: Popup.CloseOnEscape | Popup.CloseOnPressOutsideParent
    background: Item {
        
        Rectangle {
            width: 525
            height: 387
            color: "white"
            x: 378
            y: 200
            
            Text {
                text: "Please put the weight in cart"
                width: 445
                height: 44
                x: 40
                y: 40
                color: "black"
                font.pixelSize: 32
                font.bold: true
            }
            
            Image {
                source: "../../Assets/bag1.png"
                width: 49.97
                height: 56.52
                x: 40
                y: 122.24
                z: 100
            }
            
            Image {
                source: "../../Assets/bag2.png"
                width: 40.14
                height: 45.05
                x: 76.86
                y: 133.71
                z: 0
            }
            
            Rectangle {
                width: 343
                height: 56
                color: "#F7F7F7"
                x: 141
                y: 122.5
                Text {
                    anchors.verticalCenter: parent.verticalCenter
                    x:50
                    text: obj_LogicWeightSensorPopUp.settingPage.weightsensor.currentweight
                }
                
                Rectangle {
                    width: 56
                    height: 56
                    x: 287
                    y: 0
                    color: "#D9D9D9"
                    
                    Text {
                        text: "gr"
                       
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.horizontalCenter: parent.horizontalCenter
                        color: "#6D6D6D"
                        font.pixelSize: 24
                    }
                }
            }
            
            KButton {
                width: 241
                height: 72
                text:"Confirm"
                anchors.horizontalCenter: parent.horizontalCenter
                y: 217
                borderRadius: 5
                onClicked: {
                    weightsesnsorPopup.close()
                }
            }
            
            Text {
                text: "Calibration Date"
                width: 152
                height: 22
                x: 40
                y: 333
                color: "black"
                font.pixelSize: 20
                font.family: "Archivo"
            }
            
            Text {
                text: "2023/02/03"
                width: 107
                height: 22
                x: 281
                y: 333
                color: "#6D6D6D"
                font.pixelSize: 20
                font.family: "Archivo"
            }
            
            Text {
                text: "Expired"
                width: 73
                height: 22
                x: 412
                y: 333
                color: "#F08C5A"
                font.pixelSize: 20
                font.family: "Archivo"
            }
        }
        
    }
}
