import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import QtGraphicalEffects 1.12
import QtQuick.Window 2.14



Popup {
        id: serverPopup
        // background: Item {}

        background: Rectangle {
            Item {
                width: 128
                height: 160
                
                Rectangle {
                    width: 128
                    height: 160
                    x: 494
                    y: 328
                    radius: 4

                    Image {
                        source: "../../Assets/greenlight.png"
                        width: 68
                        height: 60
                        x: 30
                        y: 30
                    }

                    Text {
                        text: "Green Light"
                        width: 99
                        height: 20
                        x: 14.5
                        y: 124
                        color: "#6D6D6D"
                        font.pixelSize: 18
                        font.family: "Archivo"
                    }
                    
                }

                Rectangle {
                    width: 128
                    height: 160
                    x: 658
                    y: 328

                    Image {
                        source: "../../Assets/blueLight.png"
                        width: 68
                        height: 60
                        x: 30
                        y: 30
                    }

                    Text {
                        text: "Blue Light"
                        width: 99
                        height: 20
                        x: 14.5
                        y: 124
                        color: "#6D6D6D"
                        font.pixelSize: 18
                        font.family: "Archivo"
                    }
                }
            }
        }
    }
