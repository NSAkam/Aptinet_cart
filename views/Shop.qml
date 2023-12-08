import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15
import QtQuick.Window 2.0
import QtQuick.Controls.Styles 1.4
import QtGraphicalEffects 1.0
import "Components"
import "Containers"
import "Utiles" as Util
import "PopUps"
import KAST.Logic 1.0



Item {
    id: root
    width: 1280
    height: 800

    property Logic obj_LogicContainerShop

    property bool isfactorlistview: false

//    signal addpluitemsClicked()

    Util.ViewSettings{
        id:viewset
    }
    Timer{
        id:t1
        interval: 3000
        running: true
        onTriggered: {
            loader.opacity = 0
        }
    }

    Image {
        source: "../Assets/AuthenticationBackground.png"
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
                Image {
                    source: "../Assets/guest1.png"
                    width: parent.width - 4
                    height: parent.height -4
                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.verticalCenter: parent.verticalCenter
                }
            }
            Text {
                text: obj_LogicContainerShop.shopPage.user.loggedInUser.name
                color: "#6D6D6D"
                width: 148
                height: 15
                font.pixelSize: 14
                x:478
                y:40
            }
            KButton{
                id:btn_lookupbyname
                btn_color: "#9D9D9D"
                x:995 -40
                y:32
                borderRadius: 5
                width: 200
                height: 40
                text: "Lookup By Name"
                btn_borderWidth:0
                fontsize: 16
                ishover: false
                onClicked: {
                    obj_LogicContainerShop.shopPage.show_addPLUItemsClicked()
                }
            }
            KButton{
                id:btn_lookupbynumber
                btn_color: viewset.primaryColor
                x:819 -76
                y:32
                borderRadius: 5
                width: 200
                height: 40
                text: "+ Lookup By Number"
                btn_borderWidth:0
                fontsize: 16
                ishover: false
                onClicked: {
                    obj_LogicContainerShop.shopPage.manual_barcodeClicked()
                }
            }
            Image {
                source: "../Assets/Help.png"
                width: 57
                height: 57
                x:1156
                y:25
            }
            Image {
                source: "../Assets/Notification.png"
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
            id:toaddItem
            text: "To add an item,\n scan its barcode or\n tap the Lookup By Number."
            width: 369
            height: 144
            x:261+ 390
            y:326
            font.pixelSize: 36
            color: "#9D9D9D"
            font.bold: true
            horizontalAlignment:  TextInput.AlignHCenter
        }
        Rectangle{
            id:loader
            x:635
            y:200
            width: 400
            height: 400
            color: "#343434"
            radius: width /2
            AnimatedImage{
                source: "../Assets/sphere-line-loader.gif"
                anchors.verticalCenter: parent.verticalCenter
                anchors.horizontalCenter: parent.horizontalCenter
                width: 220
                height: 220
            }
            Text {
                text: "Loading"
                color: "white"
                anchors.horizontalCenter: parent.horizontalCenter
                anchors.verticalCenter: parent.verticalCenter
                font.pixelSize: 24
            }
            onOpacityChanged: {
                if(opacity == 1){
                    visible = true
                    t1.restart()
                    t1.running = true
                }
                if(opacity == 0){
                    visible = false
                }
            }
            Behavior on opacity {
                NumberAnimation{duration: 1000}
            }
        }



        //        KButton{
        //            id:btn_entermanualBarcode
        //            text: "+ Lookup By Number"
        //            x:645
        //            y:610
        //            width: 382
        //            height: 62
        //            borderRadius: 4
        //            onClicked: {

        //                stackviewContainer.push(manualBarcodeHandler)

        //            }
        //        }

        StackView
        {
            id:stackviewContainer
            width: 890
            height: 708
            x:390
            y:92
            //initialItem: lstProductFactor
            //initialItem: addPluItemview
            //initialItem: newProductHandler
            //initialItem: addPluItem
            //initialItem: manualBarcodeHandler
            //initialItem: plulist
            //initialItem: specialdealslist
            //initialItem: checkout
            onDepthChanged: {
                //                if(stackviewContainer.depth > 0){
                //                    loader.opacity =0;
                //                    loader.visible = false;
                //                    toaddItem.visible = false
                //                    btn_entermanualBarcode.visible = false
                //                }
                //                else{
                //                    loader.opacity =1;
                //                    loader.visible = true;
                //                    toaddItem.visible = true
                //                    btn_entermanualBarcode.visible = true
                //                }
                //obj_LogicContainerShop.shopPage.stackview_depthChanged(stackviewContainer.depth)
            }
        }
    }


    Item{
        id:addPlupanel
        visible: false
        width: 390
        height: parent.height

        Rectangle {
            id:rect_Suggestion
            anchors.fill: parent
            color: "white"
        }
        Image {
            source: "../Assets/AptinetText1.png"
            x:32
            y:32
        }
        Image {
            id: img_UserCaptured
            source: "image://KCameraProvider/1"
            width: 326
            height: 184
            x:32
            y:105
            property bool counter: false
            cache: false

            function reloadImage() {
                counter = !counter
                source = "image://KCameraProvider/?id=" + counter
            }
        }
        Text {
            text: "ENTER PLU CODE"
            font.pixelSize: 24
            font.bold: true
            x:32
            y:327
            color: viewset.primaryColor
        }
        Image {
            source: "../Assets/EnterPLUIcon.png"
            x:313
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
                onTextChanged: {
                    if(text.length > 3)
                    {
                        obj_LogicContainerShop.shopPage.search_PLUItem(text)
                    }
                }
            }

        }
        Numpad{
            id:numpad
            anchors.top: rectEnterPLU.bottom
            anchors.topMargin: 0
            x:32
        }
    }

    Item {
        id: adsPanel
        visible: true
        width: 390
        height: parent.height

        Image {
            id:rect_SuggestionadsPanel
            source: "../Assets/leftSideBar.png"
            anchors.fill: parent

        }
        Image {
            source: "../Assets/AptinetText1.png"
            x:32
            y:32
        }

        Image {
            id: img_UserCapturedadsPanel
            source: "image://KCameraProvider/1"
            width: 326
            height: 184
            x:32
            y:105
            cache: false
            property bool counter: false


            function reloadImage() {
                counter = !counter
                source = "image://KCameraProvider/?id=" + counter

            }
        }
        Image {
            id: ads_Image
            source: "../Assets/Ads.png"
            width: 326
            height: 184
            x:32
            y:309
        }
        Text {
            text: "Special Deals"
            font.pixelSize: 24
            color: "white"
            x:32
            y:521
            font.bold: true
        }
        KButton {
            text: "more >"
            x:270
            y:520
            width: 100
            font.pixelSize: 20
            font.bold: true
            MouseArea{
                anchors.fill: parent
                onClicked: {
                    obj_LogicContainerShop.shopPage.see_allOfferListClicked()
                }
            }
        }
        ListView {
            id:slideshow
            width: 326
            height: 800 - y
            x:32
            y:571

            clip: true
            spacing: 10
            model: obj_LogicContainerShop.shopPage.offersList
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
                        y:98
                        text: "$ "+model.price
                        font.pixelSize: 24
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

    }
    Item {
        id: checkoutPanel
        visible: false
        width: 390
        height: parent.height

        Rectangle {
            color: "white"
            id:rect_SuggestionadsPanel1
            anchors.fill: parent
        }
        Image {
            source: "../Assets/AptinetText1.png"
            x:32
            y:32
        }
        Image {
            id: img_UserCapturedadsPanel1
            source: "image://KCameraProvider/1"
            width: 326
            height: 184
            x:32
            y:105
            property bool counter: false
            cache: false

            function reloadImage() {
                counter = !counter
                source = "image://KCameraProvider/?id=" + counter
            }
        }

        Text {
            text: "My Cart"
            font.pixelSize: 24
            color: "gray"
            x:32
            y:326
            font.bold: true
        }
        Rectangle{
            width: 40
            height: 40
            radius: width / 2
            x:142
            y:321
            color: viewset.secondaryColor
            Text {
                text: "2"
                anchors.horizontalCenter: parent.horizontalCenter
                anchors.verticalCenter: parent.verticalCenter
                color: "white"
                font.pixelSize: 24
                font.bold: true
            }
        }


        ListView {
            id:slideshow1
            width: 326
            height: 800 - y
            x:32
            y:360

            clip: true
            spacing: 10
            model: obj_LogicContainerShop.shopPage.factorList
            orientation: ListView.vertical
            delegate:
                Item {
                width: 326
                height: 78
                Text {
                    text: model.name
                    anchors.verticalCenter: parent.verticalCenter
                    font.pixelSize: 16
                }
                Rectangle{
                    color: viewset.primaryColor
                    width: 30
                    height: 30
                    radius: 5
                    anchors.verticalCenter: parent.verticalCenter
                    anchors.right: parent.right
                    Text {
                        text: model.countInBasket
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.horizontalCenter: parent.horizontalCenter
                        color: "white"
                    }
                }
            }
        }

    }


    Component{
        id:newProductHandler
        BarcodeScanned{
            obj_LogicContainerBarcodeScanned: obj_LogicContainerShop

            onPass: {

            }

            onCancel: {

            }
        }
    }

    Component{
        id:lstProductFactor
        LstCheckProducts{
            obj_LogicContainerLstCheckProducts: obj_LogicContainerShop
            onGocheckout: {

            }
        }
    }

    Component{
        id:manualBarcodeHandler
        ManualBarcode{
            obj_LogicContainerManualBarcode: obj_LogicContainerShop
            onOk: {
                stackviewContainer.replace(newProductHandler)
            }

            onCancle: {
                if(stackviewContainer.depth == 1)
                {
                    stackviewContainer.clear()
                }
                else
                {
                    stackviewContainer.pop()
                }

            }
        }
    }
    Component{
        id:addPluItem
        AddPluItems{
            obj_LogicContainerAddPluItems: obj_LogicContainerShop
            onSeeAll: {

            }

            onBack: {

            }
        }
    }

    Component{
        id:addPluItemview
        AddPluItemsView{
            obj_LogicContainerAddPluItemsView: obj_LogicContainerShop
            onConfirm:
            {

            }

            onCancel:
            {
                stackviewContainer.pop()
            }

        }
    }
    Component{
        id:addPluItemCountedview
        AddPluItemsCountedView{
            obj_LogicContainerAddPluItemsCountedView : obj_LogicContainerShop
            onCancel: {
                stackviewContainer.pop()
            }
        }
    }

    Component {
        id: checkout
        Checkoutpage {
            obj_LogicContainerCheckoutPage: obj_LogicContainerShop
            onNfcPaymentClicked: {

            }

            onBack: {

            }
        }
    }

    Component {
        id: nfcpayment
        PaymentviaNFC {
            obj_LogicContainerPaymentNFC: obj_LogicContainerShop

        }
    }


    Component{
        id: plulist
        PLUListItems {
            obj_LogicContainerPLUListItems: obj_LogicContainerShop
            onBack: {

            }
        }
    }
    ///////////////////////////////////////////POPUPS

    RemoveProductPopUp{
        id:popUp_RemoveProducts
        obj_logicRemoveProductList: obj_LogicContainerShop
    }

    BypassPopUp{
        id:popUp_bypass
        obj_logicByPassPopup: obj_LogicContainerShop
        onOk: {
            obj_LogicContainerShop.shopPage.accept_byPassClicked()
        }
    }

    FullMessageTimer{
        id:popUp_MessageTimer
    }

    NotificationPopUp{
        id:popUp_message
    }

    NotificationPopUp{
        id:popUp_MessageNotBarcodedProduct
        message: "Please put the product you scanned into the cart!"

    }
    NotificationPopUp{
        id:popUp_MessageNoBarcodeScanned
        message: "First, take the barcode of the product in front of the barcode scanner, then put it in the cart!"
    }
    NotificationPopUp{
        id:popUpMessageNotAllowedChangeWeight
        message: "You cannot add or subtract products to the cart during checkout!"
    }
    ////////////////////////////////////////////////////


    Component{
        id: specialdealslist
        LstSpecialDeals {
            obj_LogicContainerLstSpecialDeals: obj_LogicContainerShop
            onBack: {
                if(stackviewContainer.depth == 1)
                {
                    stackviewContainer.clear()
                }
                else
                {
                    stackviewContainer.pop()
                }
            }
        }
    }

    Connections{
        target: cameraProvider
        function onNewFrameReadSignal() {
            if(checkoutPanel.visible === true){
                img_UserCapturedadsPanel1.reloadImage()
            }
            if(adsPanel.visible === true){
                img_UserCapturedadsPanel.reloadImage()
            }

            if(addPlupanel.visible === true){
                img_UserCaptured.reloadImage()
            }
        }
    }
    Connections{
        target: obj_LogicContainerShop.shopPage

        function onOpenPopupMessageTimerSignal(text){
            popUp_MessageTimer.messageText = text
            popUp_MessageTimer.open()
        }
        function onCloseAllPopUpSignal(){
            popUp_RemoveProducts.close()

            popUp_bypass.close()

            popUp_MessageTimer.close()

            popUp_message.close()

            popUp_MessageNotBarcodedProduct.close()

            popUp_MessageNoBarcodeScanned.close()

            popUpMessageNotAllowedChangeWeight.close()
        }


        function onOpenPopupMessageSignal(text){
            popUp_message.message = text
            popUp_message.open()
        }

        function onClosePopupMessageSignal(){
            popUp_message.close()
        }

        function onOpenPopupWeightNotMatchWithBarcodeSignal(){
            popUp_MessageNotBarcodedProduct.open()
        }

        function onClosePopupWeightNotMatchWithBarcodeSignal(){
            popUp_MessageNotBarcodedProduct.close()
        }

        function onOpenPopupNoBarcodeScannedSignal(){
            popUp_MessageNoBarcodeScanned.open()
        }

        function onClosePopupNoBarcodeScannedSignal(){
            popUp_MessageNoBarcodeScanned.close()
        }

        function onOpenPopupDeleteProductSignal(){
            popUp_RemoveProducts.open()
        }

        function onClosePopupDeleteProductSignal(){
            popUp_RemoveProducts.close()
        }

        function onOpenPopUpMessageNotAllowedChangeWeightSignal(){
            popUpMessageNotAllowedChangeWeight.open()
        }

        function onClosePopUpMessageNotAllowedChangeWeightSignal(){
            popUpMessageNotAllowedChangeWeight.close()
        }

        function onOpenPopupByPassSignal(){
            popUp_bypass.open()
        }

        function onClosePopupByPassSignal(){
            popUp_bypass.close()
        }

        function onClosePopUpMessageTimer(){
            popUp_MessageTimer.close()
        }

        /////////////////////////////////////

        function onShowAllOfferListSignal(){
            stackviewContainer.push(specialdealslist)
        }

        function onShowManualBarcodeSignal(){
            stackviewContainer.push(manualBarcodeHandler)
        }

        function onShowFactorListSignal(){
            stackviewContainer.push(lstProductFactor)
        }

        function onShowNewProductScannedSignal(){
            stackviewContainer.push(newProductHandler)
            slideshow.model = obj_LogicContainerShop.shopPage.suggestedList
        }

        function onClearStackViewSignal(){
            stackviewContainer.clear()
            slideshow.model = obj_LogicContainerShop.shopPage.offersList
            adsPanel.visible = true
            checkoutPanel.visible=false
            addPlupanel.visible = false
        }

        function onCloseTopStackViewSignal(){
            stackviewContainer.pop()
            //            if(stackviewContainer.depth == 1)
            //            {
            //                if(root.isfactorlistview == false)
            //                {
            //                    stackviewContainer.clear()
            //                }
            //            }
            //            else
            //            {
            //                stackviewContainer.pop()
            //            }

        }

        function onShowAddPLUItemsSignal()
        {
            adsPanel.visible = false
            checkoutPanel.visible=false
            addPlupanel.visible = true
            stackviewContainer.push(addPluItem)

        }

        function onShowWeightedPLUItemsSignal(){
            stackviewContainer.push(addPluItemview)
        }

        function onShowCountedPLUItemsSignal(){
            stackviewContainer.push(addPluItemCountedview)
        }

        function onShowCheckOutSignal(){
            adsPanel.visible = false
            checkoutPanel.visible=true
            addPlupanel.visible = false
            stackviewContainer.push(checkout)
        }

        function onShowTopBtnSignal(){
            btn_lookupbynumber.visible = true
            btn_lookupbyname.visible = true
        }

        function onHideTopBtnSignal(){
            btn_lookupbynumber.visible = false
            btn_lookupbyname.visible = false
        }

        function onShowPaymentSignal(){
            stackview.push(nfcpayment)
        }
    }
}
