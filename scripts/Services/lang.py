from xml.dom import minidom
from xml.etree import ElementTree as ET
import json


from PySide2.QtCore import QObject, Signal, Property, Slot, QThread


class languageReader(QObject):
    

    def __init__(self,namefile):
        # print(namefile)
        f = open( "/home/aptinet/files/"+ str(namefile)+".json", "r")
        s= f.read()
        self.lst = json.loads(s)
        super().__init__()



    def get_txt_welcome(self):
        return str(self.lst["txt_welcome"])
    
    txt_welcome = Property(str,get_txt_welcome)

    def get_txt_Toaquickshoppingexperience(self):
        return str(self.lst["txt_To_a_quick_shopping_experience"])
    
    txt_To_a_quick_shopping_experience =Property (str,get_txt_Toaquickshoppingexperience)

    def get_btn_Enter_Phone_Number(self):
        return str(self.lst["btn_Enter_Phone_Number"])
    
    def get_btn_Scan_MemberShop_Cart(self):
        return str(self.lst["btn_Scan_MemberShop_Cart"])
    
    def get_btn_Help(self):
        return str(self.lst["btn_Help"])
    
    def get_btn_Continue(self):
        return str(self.lst["btn_Continue"])
    
    def get_btn_Lookup_By_Name(self):
        return str(self.lst["btn_Lookup_By_Name"])
    
    def get_btn_Lookup_By_Number(self):
        return str(self.lst["btn_Lookup_By_Number"])
    
    def get_txt_To_add_an_item_scan_its_barcode_or_tap_the_Lookup_By_Number(self):
        return str(self.lst["txt_To_add_an_item_scan_its_barcode_or_tap_the_Lookup_By_Number"])
    
    def get_txt_Loading(self):
        return str(self.lst["txt_Loading"])
    
    def get_txt_ENTER_Lookup_CODE(self):
        return str(self.lst["txt_ENTER_Lookup_CODE"])
    
    def get_txt_Special_Deals(self):
        return str(self.lst["txt_Special_Deals"])
    
    def get_btn_more(self):
        return str(self.lst["btn_more"])
    
    def get_txt_My_Cart(self):
        return str(self.lst["txt_My_Cart"])
    
    def get_mess_Please_put_the_product_you_scanned_into_the_cart(self):
        return str(self.lst["mess_Please_put_the_product_you_scanned_into_the_cart"])
    
    def get_mess_First_take_the_barcode_of_the_product_in_front_of_the_barcode_scanner_then_put_it_in_the_cart(self):
        return str(self.lst["mess_First_take_the_barcode_of_the_product_in_front_of_the_barcode_scanner_then_put_it_in_the_cart"])
    
    def get_mess_You_cannot_add_or_subtract_products_to_the_cart_during_checkout(self):
        return str(self.lst["mess_You_cannot_add_or_subtract_products_to_the_cart_during_checkout"])
    
    def get_txt_Please_hold_your_phone(self):
        return str(self.lst["txt_Please_hold_your_phone"])
    
    def get_txt_near_the_display(self):
        return str(self.lst["txt_near_the_display"])
    
    def get_txt_until_you_see_a_check_mark(self):
        return str(self.lst["txt_until_you_see_a_check_mark"])
    
    def get_txt_What_are_NFC_payments_NFC_technology_powers_contactless_payments_via_mobile_wallets_like_Apple_Pay_and_Google_Pay_as_well_as_contactless_cards(self):
        return str(self.lst["txt_What_are_NFC_payments_NFC_technology_powers_contactless_payments_via_mobile_wallets_like_Apple_Pay_and_Google_Pay_as_well_as_contactless_cards"])
    
    def get_txt_Please_scan_the_Loyalty_card_or_Enter_Loyalty_Code(self):
        return str(self.lst["txt_Please_scan_the_Loyalty_card_or_Enter_Loyalty_Code"])
    
    def get_btn_Enter_Loyalty_Card(self):
        return str(self.lst["btn_Enter_Loyalty_Card"])
    
    def get_txt_Please_enter_your_loyalty_code(self):
        return str(self.lst["txt_Please_enter_your_loyalty_code"])
    
    def get_txt_Loyalty_Code(self):
        return str(self.lst["txt_Loyalty_Code"])
    
    def get_txt_Required_Tips(self):
        return str(self.lst["txt_Required_Tips"])
    
    def get_txt_Stop_and_remove_the_product_from_the_cart(self):
        return str(self.lst["txt_Stop_and_remove_the_product_from_the_cart"])
    
    def get_txt_After_see_the_window_scan_its_barcode_of_the_selected_product_to_remove(self):
        return str(self.lst["txt_After_see_the_window_scan_its_barcode_of_the_selected_product_to_remove"])
    
    def get_txt_If_you_are_sure_to_remove_the_product_press_the_confirmation_button(self):
        return str(self.lst["txt_If_you_are_sure_to_remove_the_product_press_the_confirmation_button"])
    
    def get_btn_I_got_it(self):
        return str(self.lst["btn_I_got_it"])
    
    def get_txt_Guide_to_add_product_to_cart(self):
        return str(self.lst["txt_Guide_to_add_product_to_cart"])

    def get_txt_Guide_to_remove_product_from_cart(self):
        return str(self.lst["txt_Guide_to_remove_product_from_cart"])
    
    def get_txt_scan_its_barcode_of_the_selected_product(self):
        return str(self.lst["txt_scan_its_barcode_of_the_selected_product"])
    
    def get_txt_You_have_sec_to_view_product_information_and_put_in_the_cart(self):
        return str(self.lst["txt_You_have_sec_to_view_product_information_and_put_in_the_cart"])
    
    def get_txt_Continue_after_you_hear_the_notification_sound(self):
        return str(self.lst["txt_Continue_after_you_hear_the_notification_sound"])
    
    def get_txt_Make_sure_the_cart_is_empty(self):
        return str(self.lst["txt_Make_sure_the_cart_is_empty"])
    
    def get_txt_Dont_move_the_cart_when_add_or_remove_products(self):
        return str(self.lst["txt_Dont_move_the_cart_when_add_or_remove_products"])
    
    def get_txt_Add_or_remove_products_one_by_one(self):
        return str(self.lst["txt_Add_or_remove_products_one_by_one"])
    
    def get_txt_Get_Started(self):
        return str(self.lst["txt_Get_Started"])
    
    def get_txt_Please_enter_your_Phone_Number(self):
        return str(self.lst["txt_Please_enter_your_Phone_Number"])
    
    def get_txt_Phone_Number(self):
        return str(self.lst["txt_Phone_Number"])
    
    def get_txt_You_good_to_go(self):
        return str(self.lst["txt_You_good_to_go"])
    
    def get_txt_Thanks_for_shopping_with_us(self):
        return str(self.lst["txt_Thanks_for_shopping_with_us"])
    
    def get_btn_Send_Email(self):
        return str(self.lst["btn_Send_Email"])
    
    def get_txt_How_would_you_rate_your_shopping_experience(self):
        return str(self.lst["txt_How_would_you_rate_your_shopping_experience"])
    
    def get_txt_Enter_your_Email_Address(self):
        return str(self.lst["txt_Enter_your_Email_Address"])
    
    def get_txt_enter_Email(self):
        return str(self.lst["txt_enter_Email"])
    
    def get_txt_Cancel(self):
        return str(self.lst["txt_Cancel"])
    
    def get_txt_Enter(self):
        return str(self.lst["txt_Enter"])
    
    def get_txt_Email(self):
        return str(self.lst["txt_Email"])
    
    def get_txt_Poor(self):
        return str(self.lst["txt_Poor"])
    
    def get_txt_Infficient(self):
        return str(self.lst["txt_Infficient"])
    
    def get_txt_Adequate(self):
        return str(self.lst["txt_Adequate"])
    
    def get_txt_Good(self):
        return str(self.lst["txt_Good"])
    
    def get_txt_Great(self):
        return str(self.lst["txt_Great"])
    
    def get_txt_Excellent(self):
        return str(self.lst["txt_Excellent"])
    
    def get_txt_Perfect(self):
        return str(self.lst["txt_Perfect"])
    
    def get_txt_Fantastic(self):
        return str(self.lst["txt_Fantastic"])
    
    def get_txt_Change_Unit(self):
        return str(self.lst["txt_Change_Unit"])
    
    def get_txt_weight(self):
        return str(self.lst["txt_weight"])
    
    def get_txt_Enter_Weight(self):
        return str(self.lst["txt_Enter_Weight"])
    
    def get_txt_How_to_Calibrating(self):
        return str(self.lst["txt_How_to_Calibrating"])
    
    def get_txt_Select(self):
        return str(self.lst["txt_Select"])
    
    def get_txt_unit(self):
        return str(self.lst["txt_unit"])
    
    def get_txt_put_weight(self):
        return str(self.lst["txt_put_weight"])
    
    def get_txt_in_the_cart(self):
        return str(self.lst["txt_in_the_cart"])
    
    def get_txt_Hold_to(self):
        return str(self.lst["txt_Hold_to"])
    
    def get_txt_realize(self):
        return str(self.lst["txt_realize"])
    
    def get_btn_Hold_to_Realize(self):
        return str(self.lst["btn_Hold_to_Realize"])
    
    def get_btn_Save(self):
        return str(self.lst["btn_Save"])
    
    def get_txt_Software_Version(self):
        return str(self.lst["txt_Software_Version"])
    
    def get_txt_Update(self):
        return str(self.lst["txt_Update"])
    
    def get_btn_Change(self):
        return str(self.lst["btn_Change"])
    
    def get_txt_Tax_Value(self):
        return str(self.lst["txt_Tax_Value"])
    
    def get_txt_Calibration_Date(self):
        return str(self.lst["txt_Calibration_Date"])
    
    def get_txt_Expired(self):
        return str(self.lst["txt_Expired"])
    
    def get_txt_Insert_Tax(self):
        return str(self.lst["txt_Insert_Tax"])
    
    def get_btn_Weight_Sensor(self):
        return str(self.lst["btn_Weight_Sensor"])
    
    def get_btn_Scanner(self):
        return str(self.lst["btn_Scanner"])
    
    def get_btn_Lights(self):
        return str(self.lst["btn_Lights"])
    
    def get_btn_Sound(self):
        return str(self.lst["btn_Sound"])
    
    def get_txt_Please_scan_the_item_barcode(self):
        return str(self.lst["txt_Please_scan_the_item_barcode"])
    
    def get_btn_Upload(self):
        return str(self.lst["btn_Upload"])
    
    def get_btn_Download(self):
        return str(self.lst["btn_Download"])
    
    def get_btn_Download_Pictures(self):
        return str(self.lst["btn_Download_Pictures"])
    
    def get_btn_Server(self):
        return str(self.lst["btn_Server"])
    
    def get_btn_Wi_Fi(self):
        return str(self.lst["btn_Wi_Fi"])
    
    def get_btn_Calibrate(self):
        return str(self.lst["btn_Calibrate"])
    
    def get_btn_Device_Test(self):
        return str(self.lst["btn_Device_Test"])
    
    def get_btn_Cart_Info(self):
        return str(self.lst["btn_Cart_Info"])
    
    def get_btn_Turn_Off(self):
        return str(self.lst["btn_Turn_Off"])
    
    def get_btn_Restart_Device(self):
        return str(self.lst["btn_Restart_Device"])
    
    def get_txt_is_available(self):
        return str(self.lst["txt_is_available"])
    
    def get_btn_Download_and_install(self):
        return str(self.lst["btn_Download_and_install"])
    
    def get_txt_Please_put_the_weight_in_cart(self):
        return str(self.lst["txt_Please_put_the_weight_in_cart"])
    
    def get_btn_Confirm(self):
        return str(self.lst["btn_Confirm"])
    
    def get_btn_close(self):
        return str(self.lst["btn_close"])
    
    def get_txt_Enter_the_Password(self):
        return str(self.lst["txt_Enter_the_Password"])
    
    def get_txt_enter_Password(self):
        return str(self.lst["txt_enter_Password"])
    
    def get_txt_join(self):
        return str(self.lst["txt_join"])
    
    def get_txt_Are_you_sure_to_remove_the_products(self):
        return str(self.lst["txt_Are_you_sure_to_remove_the_products"])
    
    def get_txt_How_to_add_Lookup(self):
        return str(self.lst["txt_How_to_add_Lookup"])
    
    def get_txt_Enter_product_code(self):
        return str(self.lst["txt_Enter_product_code"])
    
    def get_txt_Add_to_Cart(self):
        return str(self.lst["txt_Add_to_Cart"])
    
    def get_txt_Confirm_Wt_or_Qty(self):
        return str(self.lst["txt_Confirm_Wt_or_Qty"])
    
    def get_txt_Recomended(self):
        return str(self.lst["txt_Recomended"])
    
    def get_btn_See_All(self):
        return str(self.lst["btn_See_All"])
    
    def get_btn_Back(self):
        return str(self.lst["btn_Back"])
    
    def get_txt_Quantity(self):
        return str(self.lst["txt_Quantity"])
    
    def get_txt_Total_Price(self):
        return str(self.lst["txt_Total_Price"])
    
    def get_txt_Place_selected_item_in_cart(self):
        return str(self.lst["txt_Place_selected_item_in_cart"])
    
    def get_txt_Please_dont_move(self):
        return str(self.lst["txt_Please_dont_move"])
    
    def get_txt_You_have_seconds_to_put_the_item_in_the_cart(self):
        return str(self.lst["txt_You_have_seconds_to_put_the_item_in_the_cart"])
    
    def get_txt_Cart_Subtotal(self):
        return str(self.lst["txt_Cart_Subtotal"])
    
    def get_txt_Tax(self):
        return str(self.lst["txt_Tax"])
    
    def get_txt_Savings(self):
        return str(self.lst["txt_Savings"])
    
    def get_txt_Enter_Discount_Code(self):
        return str(self.lst["txt_Enter_Discount_Code"])
    
    def get_btn_Apply(self):
        return str(self.lst["btn_Apply"])
    
    def get_txt_Total(self):
        return str(self.lst["txt_Total"])
    
    def get_txt_Payment(self):
        return str(self.lst["txt_Payment"])
    
    def get_txt_Payment_Via_QR(self):
        return str(self.lst["txt_Payment_Via_QR"])
    
    def get_txt_You_cant(self):
        return str(self.lst["txt_You_cant"])
    
    def get_txt_Please(self):
        return str(self.lst["txt_Please"])
    
    def get_txt_Items(self):
        return str(self.lst["txt_Items"])
    
    def get_txt_Saving(self):
        return str(self.lst["txt_Saving"])
    
    def get_txt_Subtotal(self):
        return str(self.lst["txt_Subtotal"])
    
    def get_btn_Checkout(self):
        return str(self.lst["btn_Checkout"])
    
    def get_txt_Please_enter_the_item_barcode(self):
        return str(self.lst["txt_Please_enter_the_item_barcode"])
    
    def get_txt_Lookup_Items(self):
        return str(self.lst["txt_Lookup_Items"])

    def get_txt_each(self):
        return str(self.lst["txt_each"])

    def get_txt_Qty(self):
        return str(self.lst["txt_Qty"])

    def get_txt_Wt(self):
        return str(self.lst["txt_Wt"])

    def get_sign_currency(self):
        return str(self.lst["sign_currency"])

    btn_Enter_Phone_Number = Property(str,get_btn_Enter_Phone_Number)
    btn_Scan_MemberShop_Cart = Property(str,get_btn_Scan_MemberShop_Cart)
    btn_Help = Property(str,get_btn_Help)
    btn_Continue = Property(str,get_btn_Continue)
    btn_Lookup_By_Name = Property(str,get_btn_Lookup_By_Name)
    btn_Lookup_By_Number = Property(str,get_btn_Lookup_By_Number)
    txt_To_add_an_item_scan_its_barcode_or_tap_the_Lookup_By_Number = Property(str,get_txt_To_add_an_item_scan_its_barcode_or_tap_the_Lookup_By_Number)
    txt_Loading = Property(str,get_txt_Loading)
    txt_ENTER_Lookup_CODE = Property(str,get_txt_ENTER_Lookup_CODE)
    txt_Special_Deals = Property(str,get_txt_Special_Deals)
    btn_more = Property(str,get_btn_more)
    txt_My_Cart = Property(str,get_txt_My_Cart)
    mess_Please_put_the_product_you_scanned_into_the_cart = Property(str,get_mess_Please_put_the_product_you_scanned_into_the_cart)
    mess_First_take_the_barcode_of_the_product_in_front_of_the_barcode_scanner_then_put_it_in_the_cart = Property(str,get_mess_First_take_the_barcode_of_the_product_in_front_of_the_barcode_scanner_then_put_it_in_the_cart)
    mess_You_cannot_add_or_subtract_products_to_the_cart_during_checkout = Property(str,get_mess_You_cannot_add_or_subtract_products_to_the_cart_during_checkout)
    txt_Please_hold_your_phone = Property(str,get_txt_Please_hold_your_phone)
    txt_near_the_display = Property(str,get_txt_near_the_display)
    txt_until_you_see_a_check_mark = Property(str,get_txt_until_you_see_a_check_mark)
    txt_What_are_NFC_payments_NFC_technology_powers_contactless_payments_via_mobile_wallets_like_Apple_Pay_and_Google_Pay_as_well_as_contactless_cards = Property(str,get_txt_What_are_NFC_payments_NFC_technology_powers_contactless_payments_via_mobile_wallets_like_Apple_Pay_and_Google_Pay_as_well_as_contactless_cards)
    txt_Please_scan_the_Loyalty_card_or_Enter_Loyalty_Code = Property(str,get_txt_Please_scan_the_Loyalty_card_or_Enter_Loyalty_Code)
    btn_Enter_Loyalty_Card = Property(str,get_btn_Enter_Loyalty_Card)
    txt_Please_enter_your_loyalty_code = Property(str,get_txt_Please_enter_your_loyalty_code)
    txt_Loyalty_Code = Property(str,get_txt_Loyalty_Code)
    txt_Required_Tips = Property(str,get_txt_Required_Tips)
    txt_Stop_and_remove_the_product_from_the_cart = Property(str,get_txt_Stop_and_remove_the_product_from_the_cart)
    txt_After_see_the_window_scan_its_barcode_of_the_selected_product_to_remove = Property(str,get_txt_After_see_the_window_scan_its_barcode_of_the_selected_product_to_remove)
    txt_If_you_are_sure_to_remove_the_product_press_the_confirmation_button = Property(str,get_txt_If_you_are_sure_to_remove_the_product_press_the_confirmation_button)
    btn_I_got_it = Property(str,get_btn_I_got_it)
    txt_Guide_to_add_product_to_cart = Property(str,get_txt_Guide_to_add_product_to_cart)
    txt_Guide_to_remove_product_from_cart = Property(str,get_txt_Guide_to_remove_product_from_cart)
    txt_scan_its_barcode_of_the_selected_product = Property(str,get_txt_scan_its_barcode_of_the_selected_product)
    txt_You_have_sec_to_view_product_information_and_put_in_the_cart = Property(str,get_txt_You_have_sec_to_view_product_information_and_put_in_the_cart)
    txt_Continue_after_you_hear_the_notification_sound = Property(str,get_txt_Continue_after_you_hear_the_notification_sound)
    txt_Make_sure_the_cart_is_empty = Property(str,get_txt_Make_sure_the_cart_is_empty)
    txt_Dont_move_the_cart_when_add_or_remove_products = Property(str,get_txt_Dont_move_the_cart_when_add_or_remove_products)
    txt_Add_or_remove_products_one_by_one = Property(str,get_txt_Add_or_remove_products_one_by_one)
    txt_Get_Started = Property(str,get_txt_Get_Started)
    txt_Please_enter_your_Phone_Number = Property(str,get_txt_Please_enter_your_Phone_Number)
    txt_Phone_Number = Property(str,get_txt_Phone_Number)
    txt_You_good_to_go = Property(str,get_txt_You_good_to_go)
    txt_Thanks_for_shopping_with_us = Property(str,get_txt_Thanks_for_shopping_with_us)
    btn_Send_Email = Property(str,get_btn_Send_Email)
    txt_How_would_you_rate_your_shopping_experience = Property(str,get_txt_How_would_you_rate_your_shopping_experience)
    txt_Enter_your_Email_Address = Property(str,get_txt_Enter_your_Email_Address)
    txt_enter_Email = Property(str,get_txt_enter_Email)
    txt_Cancel = Property(str,get_txt_Cancel)
    txt_Enter = Property(str,get_txt_Enter)
    txt_Email = Property(str,get_txt_Email)
    txt_Poor = Property(str,get_txt_Poor)
    txt_Infficient = Property(str,get_txt_Infficient)
    txt_Adequate = Property(str,get_txt_Adequate)
    txt_Good = Property(str,get_txt_Good)
    txt_Great = Property(str,get_txt_Great)
    txt_Excellent = Property(str,get_txt_Excellent)
    txt_Perfect = Property(str,get_txt_Perfect)
    txt_Fantastic = Property(str,get_txt_Fantastic)
    txt_Change_Unit = Property(str,get_txt_Change_Unit)
    txt_weight = Property(str,get_txt_weight)
    txt_Enter_Weight = Property(str,get_txt_Enter_Weight)
    txt_How_to_Calibrating = Property(str,get_txt_How_to_Calibrating)
    txt_Select = Property(str,get_txt_Select)
    txt_unit = Property(str,get_txt_unit)
    txt_put_weight = Property(str,get_txt_put_weight)
    txt_in_the_cart = Property(str,get_txt_in_the_cart)
    txt_Hold_to = Property(str,get_txt_Hold_to)
    txt_realize = Property(str,get_txt_realize)
    btn_Hold_to_Realize = Property(str,get_btn_Hold_to_Realize)
    btn_Save = Property(str,get_btn_Save)
    txt_Software_Version = Property(str,get_txt_Software_Version)
    txt_Update = Property(str,get_txt_Update)
    btn_Change = Property(str,get_btn_Change)
    txt_Tax_Value = Property(str,get_txt_Tax_Value)
    txt_Calibration_Date = Property(str,get_txt_Calibration_Date)
    txt_Expired = Property(str,get_txt_Expired)
    txt_Insert_Tax = Property(str,get_txt_Insert_Tax)
    btn_Weight_Sensor = Property(str,get_btn_Weight_Sensor)
    btn_Scanner = Property(str,get_btn_Scanner)
    btn_Lights = Property(str,get_btn_Lights)
    btn_Sound = Property(str,get_btn_Sound)
    txt_Please_scan_the_item_barcode = Property(str,get_txt_Please_scan_the_item_barcode)
    btn_Upload = Property(str,get_btn_Upload)
    btn_Download = Property(str,get_btn_Download)
    btn_Download_Pictures = Property(str,get_btn_Download_Pictures)
    btn_Server = Property(str,get_btn_Server)
    btn_Wi_Fi = Property(str,get_btn_Wi_Fi)
    btn_Calibrate = Property(str,get_btn_Calibrate)
    btn_Device_Test = Property(str,get_btn_Device_Test)
    btn_Cart_Info = Property(str,get_btn_Cart_Info)
    btn_Turn_Off = Property(str,get_btn_Turn_Off)
    btn_Restart_Device = Property(str,get_btn_Restart_Device)
    txt_is_available = Property(str,get_txt_is_available)
    btn_Download_and_install = Property(str,get_btn_Download_and_install)
    txt_Please_put_the_weight_in_cart = Property(str,get_txt_Please_put_the_weight_in_cart)
    btn_Confirm = Property(str,get_btn_Confirm)
    btn_close = Property(str,get_btn_close)
    txt_Enter_the_Password = Property(str,get_txt_Enter_the_Password)
    txt_enter_Password = Property(str,get_txt_enter_Password)
    txt_join = Property(str,get_txt_join)
    txt_Are_you_sure_to_remove_the_products = Property(str,get_txt_Are_you_sure_to_remove_the_products)
    txt_How_to_add_Lookup = Property(str,get_txt_How_to_add_Lookup)
    txt_Enter_product_code = Property(str,get_txt_Enter_product_code)
    txt_Add_to_Cart = Property(str,get_txt_Add_to_Cart)
    txt_Confirm_Wt_or_Qty = Property(str,get_txt_Confirm_Wt_or_Qty)
    txt_Recomended = Property(str,get_txt_Recomended)
    btn_See_All = Property(str,get_btn_See_All)
    btn_Back = Property(str,get_btn_Back)
    txt_Quantity = Property(str,get_txt_Quantity)
    txt_Total_Price = Property(str,get_txt_Total_Price)
    txt_Place_selected_item_in_cart = Property(str,get_txt_Place_selected_item_in_cart)
    txt_Please_dont_move = Property(str,get_txt_Please_dont_move)
    txt_You_have_seconds_to_put_the_item_in_the_cart = Property(str,get_txt_You_have_seconds_to_put_the_item_in_the_cart)
    txt_Cart_Subtotal = Property(str,get_txt_Cart_Subtotal)
    txt_Tax = Property(str,get_txt_Tax)
    txt_Savings = Property(str,get_txt_Savings)
    txt_Enter_Discount_Code = Property(str,get_txt_Enter_Discount_Code)
    btn_Apply = Property(str,get_btn_Apply)
    txt_Total = Property(str,get_txt_Total)
    txt_Payment = Property(str,get_txt_Payment)
    txt_Payment_Via_QR = Property(str,get_txt_Payment_Via_QR)
    txt_You_cant = Property(str,get_txt_You_cant)
    txt_Please = Property(str,get_txt_Please)
    txt_Items = Property(str,get_txt_Items)
    txt_Saving = Property(str,get_txt_Saving)
    txt_Subtotal = Property(str,get_txt_Subtotal)
    btn_Checkout = Property(str,get_btn_Checkout)
    txt_Please_enter_the_item_barcode = Property(str,get_txt_Please_enter_the_item_barcode)
    txt_each = Property(str,get_txt_each)
    txt_Qty = Property(str,get_txt_Qty)
    txt_Wt = Property(str,get_txt_Wt)
    sign_currency = Property(str,get_sign_currency)

