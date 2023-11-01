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
                source: "/home/mahnaz/akam/ui_aptinet/assets/akam.png" 
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
                source: "/home/mahnaz/akam/ui_aptinet/assets/aptinet.png"
                x: 550
                y: 32
                width: 180
                height: 21
            }

            Image {
                    source: "/home/mahnaz/akam/ui_aptinet/assets/smartcart.png"
                    x: 578
                    y: 65
                    width: 124
                    height: 12
            }

        }

        Row {
            spacing: 30
            // x: 166
            // y: 400
            anchors {
                top: parent.top
                horizontalCenter: parent.horizontalCenter
                topMargin:300
            }

            Button {
                width: 128
                height: 160

                onClicked: {
                    serverPopup.open()
                    b.z = root.z + 1
                    b.visible = true
                    b.opacity = 0.4
                    
                }
                background: Rectangle {
                    
                    color: "white"
                    
                }
        

                Image {
                    source: "/home/mahnaz/akam/ui_aptinet/assets/server.png"
                    width: 64
                    height: 64
                    x: 34
                    y: 30
                }

                Text {
                    text: "server"
                    width: 70
                    height: 20
                    x: 42
                    y: 124
                    font.family: "Archivo"
                    color: "gray"
                }
            }

            Button {
                width: 128
                height: 160

                background: Rectangle {
                    
                    color: "white"
                    
                }
                onClicked: {
                    wifiPopup.open()
                    wi.z = root.z + 1
                    wi.visible = true
                    wi.opacity = 0.8
                }

                Image {
                    source: "/home/mahnaz/akam/ui_aptinet/assets/wifi.png" 
                    height: 64
                    x: 25
                    y: 30
                }

                Text {
                    text: "Wi-Fi"
                    width: 56
                    height: 20
                    x: 45
                    y: 124
                    color: "gray"
                }
            }

            Button {
                width: 128
                height: 160

                background: Rectangle {
                    
                    color: "white"
                    
                }

                Image {
                    source: "/home/mahnaz/akam/ui_aptinet/assets/calibrate.png" 
                    width: 64
                    height: 64
                    x: 34
                    y: 30
                }

                Text {
                    text: "Calibrate"
                    width: 56
                    height: 20
                    x: 33
                    y: 124
                    color: "gray"
                }
            }

            Button {
                width: 128
                height: 160

                background: Rectangle {
                    
                    color: "white"
                    
                }

                Image {
                    source: "/home/mahnaz/akam/ui_aptinet/assets/data.png"
                    width: 64
                    height: 64
                    x: 34
                    y: 30
                }

                Text {
                    text: "Data Entry"
                    x: 33
                    y: 124
                    width: 56
                    height: 20
                    color: "gray"
                }
            }

            Button {
                width: 128
                height: 160
                
                background: Rectangle {
                    
                    color: "white"
                    
                }

                Image {
                    source: "/home/mahnaz/akam/ui_aptinet/assets/device.png"
                    width: 64
                    height: 64
                    x: 34
                    y: 30
                }

                Text {
                    text: "Device Test"
                    width: 70
                    height: 20
                    x: 30
                    y: 124
                    font.family: "Archivo"
                    color: "gray"
                }
            }

            Button {
                width: 128
                height: 160
                background: Rectangle {
                    
                    color: "white"
                    
                }
                onClicked: {
                    cartinfopopup.open()
                    cart.z = root.z + 1
                    cart.visible = true
                    cart.opacity = 0.8
                }

                Image {
                    source: "/home/mahnaz/akam/ui_aptinet/assets/cartinfo.png" 
                    height: 64
                    x: 32
                    y: 30
                }

                Text {
                    text: "Cart Info"
                    width: 56
                    height: 20
                    x: 38
                    y: 124
                    color: "gray"
                }
            }
        }

        Button {
            background: Rectangle {
                color: "white"
            }
            Image {
                source: "/home/mahnaz/akam/ui_aptinet/assets/turnoff.png"
                width: 76
                height: 76
                x: 684
                y: 607
            }
        }

        Button {
            background: Rectangle {
                color: "white"
            }
            Image {
                source: "/home/mahnaz/akam/ui_aptinet/assets/restart.png"
                width: 76
                height: 76
                x: 530
                y: 607
            }
        }


    Popup {

    id: serverPopup

    // modal: true
        background: Rectangle {
        Item {
                width: 259
                height: 364
                anchors.centerIn: parent

                Rectangle {
                    width: 259
                    height: 364
                    x: 480
                    y: 390
                    radius: 4

                        Image {
                    source: "/home/mahnaz/akam/ui_aptinet/assets/flashback.png"
                    width: 92
                    height: 92
                    x: -360
                    y: -220
                }

                    // C1 {
                    //         primaryColor: "#F8C6AD"
                    //         secondaryColor: "#F08C5A"
                    //         value: 0.3
                    //         width: 176
                    //         height: 176
                    //         x: 41.5
                    //         y: 40
                            
                            // Text {
                                
                            //     anchors.centerIn: parent
                            //     text: 
                                
                            // }
                        
                        // }

                    Rectangle {
                            width: 179
                            height: 44
                            color: "#4696FA"
                            x: 42
                            y: 280
                            radius: 3

                            Image {
                                source: "/home/mahnaz/akam/ui_aptinet/assets/upload.png"
                                x: 20
                                y: 12
                            }
                            
                        }

                }

                Rectangle {
                        width: 259
                        height: 364
                        x: 770
                        y: 390
                        radius: 4

                        // C1 {
                        //     primaryColor: "#F8C6AD"
                        //     secondaryColor: "#F08C5A"
                        //     value: 0.3
                        //     width: 176
                        //     height: 176
                        //     x: 41.5
                        //     y: 40
                            
                        //     // Text {
                                
                        //     //     anchors.centerIn: parent
                        //     //     text: 
                                
                        //     // }
                        
                        // }



                        Rectangle {
                            width: 179
                            height: 44
                            x: 28
                            y: 280

                            Image {
                                source: "/home/mahnaz/akam/ui_aptinet/assets/frame.png"
                                x: 20
                                y: 2
                            }
                            
                        }

                    }
                }
                }

    }

    WifiPopup {
        id: wifiPopup
    }

    CartinfoPopup {
        id: cartinfopopup
    }

     Rectangle {
        id: b
        color: "gray"
        width: 1280
        height: 708
        visible: true
        opacity: 0
        x: 0
        y: 92

        FastBlur {

            anchors.fill: b
            source: q
            radius: 70
        }
    }

     Rectangle {
        id: wi
        color: "gray"
        width: 1280
        height: 708
        visible: true
        opacity: 0
        x: 0
        y: 92

        FastBlur {

            anchors.fill: wi
            source: q
            radius: 70
        }
    }

    Rectangle {
        id: cart
        color: "white"
        width: 1280
        height: 708
        visible: true
        opacity: 0
        x: 0
        y: 92

        FastBlur {

            anchors.fill: cart
            source: q
            radius: 70
        }
    }

    

}



    

