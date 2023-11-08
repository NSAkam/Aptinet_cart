import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import QtGraphicalEffects 1.12
import QtQuick.Window 2.14





Window {
    id: root
    visible: true
    width: 1280
    height: 800
   

    Image {     id: q
                source: "../assets/AuthenticationBackground.png"
                anchors.fill: parent
                opacity: 0.7
    

                Rectangle {
                    width: parent.width
                    height: parent.height
                    color: "white" 
                    opacity: 0.7
                    anchors.fill: parent
            }
        }

    FastBlur {

            anchors.fill: q
            source: q
            radius: 70
        }


        Rectangle {
            width: parent.width
            height: 92 
            color: "white"

            Image {
                source: "../assets/aptinet.png"
                x: 550
                y: 32
                width: 180
                height: 21
            }

            Image {
                    source: "../assets/smartcart.png"
                    x: 578
                    y: 65
                    width: 124
                    height: 12
            }

        }


        // Rectangle {
        //     width: 725
        //     height: 74
        //     x: 278
        //     y: 200
        //     color: "white"
        //     radius: 12

        //     layer.enabled: true
        //     layer.effect: DropShadow {
        //     horizontalOffset: 3
        //     verticalOffset: 3
        //     radius: 10
        //     samples: 16
        //     color: "gray"
        // }


        //     Text {
        //         text: "WifiName-1"
        //         font.pixelSize: 24
        //         color: "#6D6D6D"
        //         x: 71.11
        //         y: 26
        //         font.family: "Archivo"
        //     }

        //     Image {
        //         source: "../assets/tick.png"
        //         width: 27.11
        //         height: 20
        //         x: 24
        //         y: 27
                
        //     }

        //     Text {
        //         text: "IP: 19.58.12.3"
        //         font.pixelSize: 20
        //         color: "#9D9D9D"
        //         x: 227.11
        //         y: 28
        //         font.family: "Archivo"
                
        //     }

        //     Text {
        //         text: "Signal Level: 24"
        //         font.pixelSize: 20
        //         color: "#9D9D9D"
        //         x: 503
        //         y: 27
        //         font.family: "Archivo"
                
        //     }
        // }

        // Rectangle {
        //     width: 725
        //     height: 74
        //     x: 278
        //     y: 330
        //     color: "white"

        //     layer.enabled: true
        //     layer.effect: DropShadow {
        //     horizontalOffset: 3
        //     verticalOffset: 3
        //     radius: 10
        //     samples: 16
        //     color: "gray"
        // }


        //     Text { 
        //        text: "WifiName-2"
        //         font.pixelSize: 24
        //         color: "#6D6D6D"
        //         x: 36
        //         y: 24
        //         font.family: "Archivo" 
        //     }
        // }

        // Rectangle {
        //     width: 725
        //     height: 1
        //     x: 278
        //     y: 404
        //     color: "#9D9D9D"
        // }


        // Rectangle {
        //     width: 725
        //     height: 74
        //     x: 278
        //     y: 406
        //     color: "white"

        //     layer.enabled: true
        //     layer.effect: DropShadow {
        //     horizontalOffset: 3
        //     verticalOffset: 3
        //     radius: 10
        //     samples: 16
        //     color: "gray"
        // }


        //     Text { 
        //        text: "WifiName-3"
        //         font.pixelSize: 24
        //         color: "#6D6D6D"
        //         x: 36
        //         y: 24
        //         font.family: "Archivo" 
        //     }
        // }

        // Rectangle {
        //     width: 725
        //     height: 1
        //     x: 278
        //     y: 480
        //     color: "#9D9D9D"
        // }

        // Rectangle {
        //     width: 725
        //     height: 74
        //     x: 278
        //     y: 482
        //     color: "white"

        //     layer.enabled: true
        //     layer.effect: DropShadow {
        //     horizontalOffset: 3
        //     verticalOffset: 3
        //     radius: 10
        //     samples: 16
        //     color: "gray"
        // }


        //     Text { 
        //        text: "WifiName-4"
        //         font.pixelSize: 24
        //         color: "#6D6D6D"
        //         x: 36
        //         y: 24
        //         font.family: "Archivo" 
        //     }
        // }

        // Rectangle {
        //     width: 725
        //     height: 1
        //     x: 278
        //     y: 557
        //     color: "#9D9D9D"
        // }

        // Rectangle {
        //     width: 725
        //     height: 74
        //     x: 278
        //     y: 559
        //     color: "white"

        //     layer.enabled: true
        //     layer.effect: DropShadow {
        //     horizontalOffset: 3
        //     verticalOffset: 3
        //     radius: 10
        //     samples: 16
        //     color: "gray"
        // }


        //     Text { 
        //        text: "WifiName-5"
        //         font.pixelSize: 24
        //         color: "#6D6D6D"
        //         x: 36
        //         y: 24
        //         font.family: "Archivo" 
        //     }
        // }

        // Text {
        //     text: "Refresh"
        //     font.pixelSize: 24
        //     color: "#4696FA"
        //     x: 900
        //     y: 650
        //     font.family: "Archivo" 
        
        // }

        // Image {
        //     source: "../assets/loading.png"
        //     width: 20
        //     height: 20
        //     x: 870
        //     y: 654
        // }
        

    
    }

    



    

