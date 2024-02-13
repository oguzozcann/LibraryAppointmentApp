from kivy.lang import Builder
from kivymd.app import MDApp
import psycopg2
from kivy.uix.screenmanager import Screen
from kivymd.uix.list import TwoLineListItem ,OneLineListItem,MDList
from kivymd.uix.pickers import MDDatePicker , MDTimePicker
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRoundFlatButton
import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime
import os
current_directory = os.path.dirname(os.path.realpath(__file__))
image_path = os.path.join(current_directory, 'kutuphane.jpg')
image_path = image_path.replace('\\', '/')
print("""{}""".format(image_path))
KV="""
MDNavigationLayout: 
    MDScreenManager:
        id: yonetici
        
        GirisScreen:
            id:GirisScreen
            name:"GirisScreen"
            manager: 'yonetici'
        
        MenuScreen:
            id:MenuScreen
            name:"MenuScreen"
            manager:'yonetici'
            FitImage:
                size_hint:(1,1)
                source: app.image_path
            MDBoxLayout:
                orientation:"vertical"
                md_bg_color:0,0,0,0.1
                MDTopAppBar:
                    md_bg_color:1,1,1,0.1
                    title:"BOS-GUI"
                    specific_text_color: "white"
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                        
                ScrollView:
                    MDList:
                        id:lista
                        md_bg_color:0,0,0,0.1 
                        
                MDFloatingActionButton:
                    icon: "plus"
                    md_bg_color: app.theme_cls.primary_color
                    pos_hint:{"center_x":.95,"center_y":.95}
                    on_press:root.ids.yonetici.current="YeniScreen"
           
        KayitScreen:
            id:kayit
            name:"KayitScreen"
            manager:'yonetici'
        
        UnuttumScreen:
            id:unuttum
            name:"UnuttumScreen"
            manager:'yonetici'

        MailOnayi:
            id:MailOnayi
            name:"MailOnayi"
            manager:'yonetici'
        
        YeniScreen:
            id:yeni
            name:"YeniScreen"
            manager:"yonetici"

            FitImage:
                size_hint:(1,1)
                source: app.image_path
                    
            MDTopAppBar:
                md_bg_color:1,1,1,0.1
                title:"BOS-GUI"
                specific_text_color: "white"
                pos_hint:{"top":1}
                left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                    
            MDFloatLayout:
                md_bg_color:0,0,0,0.1
                MDRaisedButton:
                    id:date_button
                    text:"tarih seç"
                    pos_hint:{"center_x":.18,"center_y":.8}
                    on_release:app.show_date_picker()
                    size_hint:(.3,.1)

                MDRaisedButton:
                    id:baslangic
                    text:"Rezeravasyon başı"
                    pos_hint:{"center_x":.5,"center_y":.8}
                    size_hint:(.3,.1)
                    on_release:app.show_time_picker(baslangic)
                    disabled:True
                        
                MDRaisedButton:
                    id:bitis
                    text:"Rezervasyon sonu"
                    pos_hint:{"center_x":.82,"center_y":.8}
                    size_hint:(.3,.1)
                    on_release:app.show_time_picker(bitis)
                    disabled:True
                
                MDRaisedButton:
                    id:S0000
                    text:"S0000"
                    size_hint:(.1,.1)
                    pos_hint:{"center_x":.1,"center_y":.675}
                    on_release:app.sec(S0000)
                    disabled:True
                MDRaisedButton:
                    id:S0002
                    text:"S0002"
                    size_hint:(.1,.1)
                    pos_hint:{"center_x":.1,"center_y":.55}
                    on_release:app.sec(S0002)
                    disabled:True
                MDRaisedButton:
                    id:S0004
                    text:"S0004"
                    size_hint:(.1,.1)
                    pos_hint:{"center_x":.1,"center_y":.425}
                    on_release:app.sec(S0004)
                    disabled:True
                MDRaisedButton:
                    id:S0006
                    text:"S0006"
                    size_hint:(.1,.1)
                    pos_hint:{"center_x":.1,"center_y":.3}
                    on_release:app.sec(S0006)
                    disabled:True
                MDRaisedButton:
                    id:S0008
                    text:"S0008"
                    size_hint:(.1,.1)
                    pos_hint:{"center_x":.1,"center_y":.175}
                    on_release:app.sec(S0008)
                    disabled:True
                MDRaisedButton:
                    id:S0010
                    text:"S0010"
                    size_hint:(.1,.1)
                    pos_hint:{"center_x":.1,"bottom":0}
                    on_release:app.sec(S0010)
                    disabled:True
                
                MDRaisedButton:
                    id:S0001
                    text:"S0001"
                    size_hint:(.1,.1)
                    pos_hint:{"center_x":.225,"center_y":.675}
                    on_release:app.sec(S0001)
                    disabled:True
                MDRaisedButton:
                    id:S0003
                    text:"S0003"
                    size_hint:(.1,.1)
                    pos_hint:{"center_x":.225,"center_y":.55}
                    on_release:app.sec(S0003)
                    disabled:True
                MDRaisedButton:
                    id:S0005
                    text:"S0005"
                    size_hint:(.1,.1)
                    pos_hint:{"center_x":.225,"center_y":.425}
                    on_release:app.sec(S0005)
                    disabled:True
                MDRaisedButton:
                    id:S0007
                    text:"S0007"
                    size_hint:(.1,.1)
                    pos_hint:{"center_x":.225,"center_y":.3}
                    on_release:app.sec(S0007)
                    disabled:True
                MDRaisedButton:
                    id:S0009
                    text:"S0009"
                    size_hint:(.1,.1)
                    pos_hint:{"center_x":.225,"center_y":.175}
                    on_release:app.sec(S0009)
                    disabled:True
                MDRaisedButton:
                    id:S0011
                    text:"S0011"
                    size_hint:(.1,.1)
                    pos_hint:{"center_x":.225,"bottom":0}
                    on_release:app.sec(S0011)
                    disabled:True
                
                MDRaisedButton:
                    id:S0012
                    text:"S0012"
                    size_hint:(.1,.1)
                    pos_hint:{"center_x":.4,"center_y":.675}
                    on_release:app.sec(S0012)
                    disabled:True
                MDRaisedButton:
                    id:S0014
                    text:"S0014"
                    size_hint:(.1,.1)
                    pos_hint:{"center_x":.4,"center_y":.55}
                    on_release:app.sec(S0014)
                    disabled:True
                MDRaisedButton:
                    id:S0016
                    text:"S0016"
                    size_hint:(.1,.1)
                    pos_hint:{"center_x":.4,"center_y":.425}
                    on_release:app.sec(S0016)
                    disabled:True
                MDRaisedButton:
                    id:S0018
                    text:"S0018"
                    size_hint:(.1,.1)
                    pos_hint:{"center_x":.4,"center_y":.3}
                    on_release:app.sec(S0018)
                    disabled:True
                MDRaisedButton:
                    id:S0020
                    text:"S0020"
                    size_hint:(.1,.1)
                    pos_hint:{"center_x":.4,"center_y":.175}
                    on_release:app.sec(S0020)
                    disabled:True
                MDRaisedButton:
                    id:S0022
                    text:"S0022"
                    size_hint:(.1,.1)
                    pos_hint:{"center_x":.4,"bottom":0}
                    on_release:app.sec(S0022)
                    disabled:True

                MDRaisedButton:
                    id:S0013
                    text:"S0013"
                    size_hint:(.1,.1)
                    pos_hint:{"center_x":.525,"center_y":.675}
                    on_release:app.sec(S0013)
                    disabled:True
                MDRaisedButton:
                    id:S0015
                    text:"S0015"
                    size_hint:(.1,.1)
                    pos_hint:{"center_x":.525,"center_y":.55}
                    on_release:app.sec(S0015)
                    disabled:True
                MDRaisedButton:
                    id:S0017
                    text:"S0017"
                    size_hint:(.1,.1)
                    pos_hint:{"center_x":.525,"center_y":.425}
                    on_release:app.sec(S0017)
                    disabled:True
                MDRaisedButton:
                    id:S0019
                    text:"S0019"
                    size_hint:(.1,.1)
                    pos_hint:{"center_x":.525,"center_y":.3}
                    on_release:app.sec(S0019)
                    disabled:True
                MDRaisedButton:
                    id:S0021
                    text:"S0021"
                    size_hint:(.1,.1)
                    on_release:app.sec(S0021)
                    pos_hint:{"center_x":.525,"center_y":.175}
                    disabled:True
                MDRaisedButton:
                    id:S0023
                    text:"S0023"
                    size_hint:(.1,.1)
                    on_release:app.sec(S0023)
                    pos_hint:{"center_x":.525,"bottom":0}
                    disabled:True

                MDRaisedButton:
                    id:S0024
                    text:"S0024"
                    size_hint:(.1,.1)
                    on_release:app.sec(S0024)
                    pos_hint:{"center_x":.7,"center_y":.675}
                    disabled:True
                MDRaisedButton:
                    id:S0026
                    text:"S0026"
                    size_hint:(.1,.1)
                    on_release:app.sec(S0026)
                    pos_hint:{"center_x":.7,"center_y":.55}
                    disabled:True
                MDRaisedButton:
                    id:S0028
                    text:"S0028"
                    size_hint:(.1,.1)
                    on_release:app.sec(S0028)
                    pos_hint:{"center_x":.7,"center_y":.425}
                    disabled:True
                MDRaisedButton:
                    id:S0030
                    text:"S0030"
                    size_hint:(.1,.1)
                    on_release:app.sec(S0030)
                    pos_hint:{"center_x":.7,"center_y":.3}
                    disabled:True
                MDRaisedButton:
                    id:S0032
                    text:"S0032"
                    size_hint:(.1,.1)
                    on_release:app.sec(S0032)
                    pos_hint:{"center_x":.7,"center_y":.175}
                    disabled:True
                MDRaisedButton:
                    id:S0034
                    text:"S0034"
                    size_hint:(.1,.1)
                    on_release:app.sec(S0034)
                    pos_hint:{"center_x":.7,"bottom":0}
                    disabled:True

                MDRaisedButton:
                    id:S0025
                    text:"S0025"
                    size_hint:(.1,.1)
                    on_release:app.sec(S0025)
                    pos_hint:{"center_x":.825,"center_y":.675}
                    disabled:True
                MDRaisedButton:
                    id:S0027
                    text:"S0027"
                    size_hint:(.1,.1)
                    on_release:app.sec(S0027)
                    pos_hint:{"center_x":.825,"center_y":.55}
                    disabled:True
                MDRaisedButton:
                    id:S0029
                    text:"S0029"
                    size_hint:(.1,.1)
                    on_release:app.sec(S0029)
                    pos_hint:{"center_x":.825,"center_y":.425}
                    disabled:True
                MDRaisedButton:
                    id:S0031
                    text:"S0031"
                    size_hint:(.1,.1)
                    on_release:app.sec(S0031)
                    pos_hint:{"center_x":.825,"center_y":.3}
                    disabled:True
                MDRaisedButton:
                    id:S0033
                    text:"S0033"
                    size_hint:(.1,.1)
                    on_release:app.sec(S0033)
                    pos_hint:{"center_x":.825,"center_y":.175}
                    disabled:True
                MDRaisedButton:
                    id:S0035
                    text:"S0035"
                    size_hint:(.1,.1)
                    on_release:app.sec(S0035)
                    pos_hint:{"center_x":.825,"bottom":0}
                    disabled:True

        EskiScreen:
            id:gecmis
            name:"Gecmis"
            manager:"yonetici"

            FitImage:
                size_hint:(1,1)
                source: app.image_path
                    
            MDBoxLayout:
                orientation:"vertical"
                md_bg_color:0,0,0,0.1
                MDTopAppBar:
                    md_bg_color:1,1,1,0.1
                    title:"BOS-GUI"
                    specific_text_color: "white"
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                        
                ScrollView:
                    MDList:
                        id:list
                        md_bg_color:0,0,0,0.1  

        ToplananScreen:
            id:ToplananScreen
            name:"ToplananScreen"
            manager:"yonetici"

            FitImage:
                size_hint:(1,1)
                source: app.image_path

            MDBoxLayout:
                orientation:"vertical"
                md_bg_color:0,0,0,0.1
                MDTopAppBar:
                    md_bg_color:1,1,1,0.1
                    title:"BOS-GUI"
                    specific_text_color: "white"
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                
                ScrollView:
                    MDList:
                        id:lis
                        md_bg_color:0,0,0,0.1
        
        Ayarlar:
            id:Ayarlar
            name:"Ayarlar"
            manager:"yonetici"

            FitImage:
                size_hint:(1,1)
                source: app.image_path

            MDBoxLayout:
                orientation:"vertical"
                md_bg_color:0,0,0,0.1
                MDTopAppBar:
                    md_bg_color:1,1,1,0.1
                    title:"BOS-GUI"
                    specific_text_color: "white"
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

                MDLabel:
                    text:""
                MDCard:
                    size_hint:None,None
                    size: 300, 200
                    pos_hint:{"center_x":.5,"center_y":.5}
                    md_bg_color:1,1,1,0.1
                    elevation:10
                    padding:25
                    spacing:25
                    orientation:"vertical"
                    
                    MDRoundFlatButton:
                        id:sif_degis
                        text:"Şifre Değiştir"
                        on_press: root.ids.yonetici.current="SifreDegis"
                        pos_hint:{"center_x":.5}

                    MDRoundFlatButton:
                        id:mail_degis
                        text:"E-Posta Değiştir"
                        on_press: root.ids.yonetici.current="MailDegis"
                        pos_hint:{"center_x":.5}

                    MDRoundFlatButton:
                        id:tel_degis
                        text:"Telefon Değiştir"
                        on_press: root.ids.yonetici.current="TelDegis"
                        pos_hint:{"center_x":.5}
                MDLabel:
                    text:""
        SifreDegis:
            id:SifreDegis
            name:"SifreDegis"
            manager:"yonetici"

            FitImage:
                size_hint:(1,1)
                source: app.image_path

            MDBoxLayout:
                orientation:"vertical"
                md_bg_color:0,0,0,0.1
                MDTopAppBar:
                    md_bg_color:1,1,1,0.1
                    title:"BOS-GUI"
                    specific_text_color: "white"
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                MDLabel:
                    text:""
                MDCard:
                    size_hint:None,None
                    size: 300, 250
                    pos_hint:{"center_x":.5,"center_y":.5}
                    md_bg_color:1,1,1,0.1
                    elevation:10
                    padding:25
                    spacing:25
                    orientation:"vertical"

                    ClickableTextFieldRound:
                        size_hint_x: None
                        width: "300dp"
                        hint_text: "Mevcut şifreniz"
                        pos_hint: {"center_x": .5}
                        size_hint_y: None
                        height: degis_sifre.height
                        
                        MDTextField:
                            id:degis_sifre
                            hint_text:"Mevcut şifreniz"
                            required: False
                            helper_text_mode: "on_error"
                            helper_text: "Bu Alan Zorunludur!"
                            mode:"round"
                            md_bg_color:1,1,1,0.2
                            size_hint_x:None
                            width:200
                            font_size:18
                            pos_hint:{"center_x":.5}
                            password: True
                            on_text_validate:root.ids.degis_ysifre.focus=True
                        
                        MDIconButton:
                            icon: "eye-off"
                            pos_hint: {"center_y": .5}
                            pos: degis_sifre.width , 0
                            theme_text_color: "Hint"
                            on_release:
                                self.icon = "eye" if self.icon == "eye-off" else "eye-off"
                                degis_sifre.password = False if degis_sifre.password is True else True

                    ClickableTextFieldRound:
                        size_hint_x: None
                        width: "300dp"
                        hint_text: "Yeni şifreniz"
                        pos_hint: {"center_x": .5}
                        size_hint_y: None
                        height: degis_ysifre.height
                        
                        MDTextField:
                            id:degis_ysifre
                            hint_text:"Yeni şifreniz"
                            required: False
                            helper_text_mode: "on_error"
                            helper_text: "Bu Alan Zorunludur!"
                            mode:"round"
                            md_bg_color:1,1,1,0.2
                            size_hint_x:None
                            width:200
                            font_size:18
                            pos_hint:{"center_x":.5}
                            password: True
                            on_text_validate:root.ids.degis_ysifre_tekrar.focus=True
                        
                        MDIconButton:
                            icon: "eye-off"
                            pos_hint: {"center_y": .5}
                            pos: degis_ysifre.width , 0
                            theme_text_color: "Hint"
                            on_release:
                                self.icon = "eye" if self.icon == "eye-off" else "eye-off"
                                degis_ysifre.password = False if degis_ysifre.password is True else True

                    ClickableTextFieldRound:
                        size_hint_x: None
                        width: "300dp"
                        hint_text: "Yeni şifreniz tekrar"
                        pos_hint: {"center_x": .5}
                        size_hint_y: None
                        height: degis_ysifre_tekrar.height
                        
                        MDTextField:
                            id:degis_ysifre_tekrar
                            hint_text:"Yeni şifrenizi tekrar"
                            required: False
                            helper_text_mode: "on_error"
                            helper_text: "Bu Alan Zorunludur!"
                            mode:"round"
                            md_bg_color:1,1,1,0.2
                            size_hint_x:None
                            width:200
                            font_size:18
                            pos_hint:{"center_x":.5}
                            password: True
                            on_text_validate:
                                app.yeni_sifre()
                                root.ids.degis_sifre.text=""
                                root.ids.degis_ysifre.text=""
                                root.ids.degis_ysifre_tekrar.text=""
                                root.ids.degis_sifre.error=False
                                root.ids.degis_ysifre.error=False
                                root.ids.degis_ysifre_tekrar.error=False
                        
                        MDIconButton:
                            icon: "eye-off"
                            pos_hint: {"center_y": .5}
                            pos: degis_ysifre_tekrar.width , 0
                            theme_text_color: "Hint"
                            on_release:
                                self.icon = "eye" if self.icon == "eye-off" else "eye-off"
                                degis_ysifre_tekrar.password = False if degis_ysifre_tekrar.password is True else True

                    GridLayout:
                        cols:2
                        spacing:100
                        MDRoundFlatButton:
                            text:"Geri"
                            font_size:12
                            on_press:
                                root.ids.yonetici.current="Ayarlar"
                                root.ids.degis_sifre.text=""
                                root.ids.degis_ysifre.text=""
                                root.ids.degis_ysifre_tekrar.text=""
                                root.ids.degis_sifre.error=False
                                root.ids.degis_ysifre.error=False
                                root.ids.degis_ysifre_tekrar.error=False

                        MDRoundFlatButton:
                            text:"Degistir"
                            font_size:12
                            on_press:
                                app.yeni_sifre()
                                root.ids.degis_sifre.text=""
                                root.ids.degis_ysifre.text=""
                                root.ids.degis_ysifre_tekrar.text=""
                                root.ids.degis_sifre.error=False
                                root.ids.degis_ysifre.error=False
                                root.ids.degis_ysifre_tekrar.error=False


                MDLabel:
                    text:""
        MailDegis:
            id:MailDegis
            name:"MailDegis"
            manager:"yonetici"

            FitImage:
                size_hint:(1,1)
                source: app.image_path

            MDBoxLayout:
                orientation:"vertical"
                md_bg_color:0,0,0,0.1
                MDTopAppBar:
                    md_bg_color:1,1,1,0.1
                    title:"BOS-GUI"
                    specific_text_color: "white"
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                MDLabel:
                    text:""
                MDCard:
                    size_hint:None,None
                    size: 300, 200
                    pos_hint:{"center_x":.5,"center_y":.5}
                    md_bg_color:1,1,1,0.1
                    elevation:10
                    padding:25
                    spacing:25
                    orientation:"vertical"

                    MDTextField:
                        id:yeni_posta
                        hint_text:" Yeni e-postanız"
                        required: False
                        helper_text_mode: "on_error"
                        helper_text: "Bu Alan Zorunludur!"
                        mode:"round"
                        icon_left:"email"
                        size_hint_x:None
                        width:250
                        font_size:18
                        pos_hint:{"center_x":.5}
                        on_text_validate:
                            app.yeni_mail()
                            root.ids.yeni_posta.text=""
                            root.ids.yeni_posta.error=False

                    GridLayout:
                        cols:2
                        spacing:100
                        MDRoundFlatButton:
                            text:"Geri"
                            font_size:12
                            on_press:
                                root.ids.yonetici.current="Ayarlar"
                                root.ids.yeni_posta.text=""
                                root.ids.yeni_posta.error=False
                        MDRoundFlatButton:
                            text:"Degistir"
                            font_size:12
                            on_press:
                                app.yeni_mail()
                                root.ids.yeni_posta.text=""
                                root.ids.yeni_posta.error=False
                MDLabel:
                    text:""
        TelDegis:
            id:TelDegis
            name:"TelDegis"
            manager:"yonetici"

            FitImage:
                size_hint:(1,1)
                source: app.image_path

            MDBoxLayout:
                orientation:"vertical"
                md_bg_color:0,0,0,0.1
                MDTopAppBar:
                    md_bg_color:1,1,1,0.1
                    title:"BOS-GUI"
                    specific_text_color: "white"
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                MDLabel:
                    text:""
                MDCard:
                    size_hint:None,None
                    size: 300, 200
                    pos_hint:{"center_x":.5,"center_y":.5}
                    md_bg_color:1,1,1,0.1
                    elevation:10
                    padding:25
                    spacing:25
                    orientation:"vertical"

                    MDTextField:
                        id:yeni_telefon
                        hint_text:" Yeni telefon numaranız"
                        required: False
                        helper_text_mode: "on_error"
                        helper_text: "Bu Alan Zorunludur!"
                        mode:"round"
                        icon_left:"phone"
                        size_hint_x:None
                        width:250
                        font_size:18
                        pos_hint:{"center_x":.5}
                        on_text_validate:
                            app.yeni_tel()
                            root.ids.yeni_telefon.text=""
                            root.ids.yeni_telefon.error=False
                    GridLayout:
                        cols:2
                        spacing:100
                        MDRoundFlatButton:
                            text:"Geri"
                            font_size:12
                            on_press:
                                root.ids.yonetici.current="Ayarlar"
                                root.ids.yeni_telefon.text=""
                                root.ids.yeni_telefon.error=False

                        MDRoundFlatButton:
                            text:"Degistir"
                            font_size:12
                            on_press:
                                app.yeni_tel()
                                root.ids.yeni_telefon.text=""
                                root.ids.yeni_telefon.error=False

                MDLabel:
                    text:""


    MDNavigationDrawer:
        id: nav_drawer
        radius: (0, 16, 16, 0)

        MDNavigationDrawerMenu:

            MDNavigationDrawerHeader:
                title: "Header title"
                title_color: "#0f9700"
                text: "Header text"
                spacing: "4dp"
                padding: "12dp", 0, 0, "56dp"

            DrawerClickableItem:
                icon: "home"
                text: "Ana Ekran"
                on_release:
                    root.ids.nav_drawer.set_state("close")
                    root.ids.yonetici.current = "MenuScreen"    
            
            MDNavigationDrawerDivider:

            DrawerClickableItem:
                icon: "clock"
                text: "Geçmiş Randevular"
                on_release:
                    root.ids.nav_drawer.set_state("close")
                    app.gecmis()

            DrawerClickableItem:
                icon: "bag-personal"
                text: "Toplanan Eşyalar"
                on_release:
                    root.ids.nav_drawer.set_state("close")
                    app.toplan()

            DrawerClickableItem:
                icon: "cog"
                text: "Ayarlar"
                on_release:
                    root.ids.nav_drawer.set_state("close")
                    root.ids.yonetici.current = "Ayarlar"
            
            DrawerClickableItem:
                icon: "exit-to-app"
                text: "Çıkış"
                on_release:
                    root.ids.nav_drawer.set_state("close")
                    app.cikis()

                    
<MyPop@Popup>
<DrawerClickableItem@MDNavigationDrawerItem>
    focus_color: "#0f9615"
    text_color: "#baab27"
    icon_color: "#baab27"
    ripple_color: "#20a2c9"
    selected_color: "#0f9700"


<DrawerLabelItem@MDNavigationDrawerItem>
    text_color: "#0f9700"
    icon_color: "#0f9700"
    focus_behavior: False
    selected_color: "#0f9700"
    _no_ripple_effect: True

<GirisScreen>:
    FitImage:
        size_hint:(1,1)
        source: app.image_path
    MDCard:
        size_hint:None,None
        size: 300, 400
        pos_hint:{"center_x":.5,"center_y":.5}
        md_bg_color:1,1,1,0.1
        elevation:10
        padding:25
        spacing:25
        orientation:"vertical"
        
        MDLabel:
            id:welcome_label
            text:"Hoşgeldiniz"
            font_size:20
            halign:"center"
            size_hint_y:None
            height:self.texture_size[1]
            padding_y:15

        MDTextField:
            id:user
            hint_text:"Öğrenci Numarası"
            required: False
            helper_text_mode: "on_error"
            helper_text: "Öğrenci no giriniz!"
            mode:"round"
            icon_left:"account"
            size_hint_x:None
            width:200
            font_size:18
            pos_hint:{"center_x":.5}
            on_text_validate:
                root.ids.password.focus=True
 
        ClickableTextFieldRound:
            size_hint_x: None
            width: "300dp"
            hint_text: "Şifre"
            pos_hint: {"center_x": .5, "center_y": .5}
            size_hint_y: None
            height: password.height
            
            MDTextField:
                id:password
                hint_text:"Şifre"
                required: False
                helper_text_mode: "on_error"
                helper_text: "Şifrenizi giriniz!"
                mode:"round"
                md_bg_color:1,1,1,0.2
                size_hint_x:None
                width:200
                font_size:18
                pos_hint:{"center_x":.5}
                password: True
                on_text_validate:app.gir()
            
            MDIconButton:
                icon: "eye-off"
                pos_hint: {"center_y": .5}
                pos: password.width , 0
                theme_text_color: "Hint"
                on_release:
                    self.icon = "eye" if self.icon == "eye-off" else "eye-off"
                    password.password = False if password.password is True else True

        MDRoundFlatButton:
            text:"Giriş"
            font_size:12
            pos_hint:{"center_x":.5}
            on_press: app.gir()

        MDRoundFlatButton:
            text:"Şifremi Unuttum"
            font_size:12
            pos_hint:{"center_x":.5}
            on_press: 
                app.root.ids.yonetici.current="UnuttumScreen"
                root.ids.welcome_label.text="Hoşgeldiniz"
                root.ids.welcome_label.theme_text_color="Primary"
                root.ids.user.text=""
                root.ids.password.text=""

        MDRoundFlatButton:
            text:"Kaydol"
            font_size:12
            pos_hint:{"center_x":.5}
            on_press: 
                app.root.ids.yonetici.current="KayitScreen"
                root.ids.welcome_label.text="Hoşgeldiniz"
                root.ids.welcome_label.theme_text_color="Primary"
                root.ids.user.text=""
                root.ids.password.text=""
<KayitScreen>:
    FitImage:
        size_hint:(1,1)
        source: app.image_path
    
    MDCard:
        size_hint:None,None
        size:300, 650
        pos_hint:{"center_x":.5,"center_y":.5}
        md_bg_color:1,1,1,0.1
        elevation:10
        padding:25
        spacing:25
        orientation:"vertical"
        
        MDLabel:
            id:kayit_label
            text:"KAYDOL"
            font_size:20
            halign:"center"
            size_hint_y:None 
            height:self.texture_size[1]
            #padding_y:15

        MDTextField:
            id:ono
            hint_text:"Ögrenci Numaranız"
            required: False
            helper_text_mode: "on_error"
            helper_text: "Bu Alan Zorunludur!"
            mode:"round"
            icon_left:"account"
            size_hint_x:None
            width:200
            font_size:18
            pos_hint:{"center_x":.5}
            on_text_validate: root.ids.isim.focus=True

        MDTextField:
            id:isim
            hint_text:"Adınız"
            required: False
            helper_text_mode: "on_error"
            helper_text: "Bu Alan Zorunludur!"
            mode:"round"
            size_hint_x:None
            width:200
            font_size:18
            pos_hint:{"center_x":.5}
            on_text_validate: root.ids.soyisim.focus=True

        MDTextField:
            id:soyisim
            hint_text:"Soyadınız"
            required: False
            helper_text_mode: "on_error"
            helper_text: "Bu Alan Zorunludur!"
            mode:"round"
            size_hint_x:None
            width:200
            font_size:18
            pos_hint:{"center_x":.5}
            on_text_validate: root.ids.telefon.focus=True

        MDTextField:
            id:telefon
            hint_text:"telefon numaranız"
            required: False
            helper_text_mode: "on_error"
            helper_text: "Bu Alan Zorunludur!"
            mode:"round"
            icon_left:"phone"
            size_hint_x:None
            width:200
            font_size:18
            pos_hint:{"center_x":.5}
            on_text_validate: root.ids.e_posta.focus=True

        MDTextField:
            id:e_posta
            hint_text:"e_posta adresiniz"
            required: False
            helper_text_mode: "on_error"
            helper_text: "Bu Alan Zorunludur!"
            mode:"round"
            icon_left:"email"
            size_hint_x:None
            width:200
            font_size:18
            pos_hint:{"center_x":.5}
            on_text_validate: root.ids.kayit_sifre.focus=True
       
        ClickableTextFieldRound:
            size_hint_x: None
            width: "300dp"
            hint_text: "Şifreniz"
            pos_hint: {"center_x": .5, "center_y": .5}
            size_hint_y: None
            height: kayit_sifre.height
            
            MDTextField:
                id:kayit_sifre
                hint_text:"Şifreniz"
                required: False
                helper_text_mode: "on_error"
                helper_text: "Bu Alan Zorunludur!"
                mode:"round"
                md_bg_color:1,1,1,0.2
                size_hint_x:None
                width:200
                font_size:18
                pos_hint:{"center_x":.5}
                password: True
                on_text_validate: root.ids.kayit_sifre_tekrar.focus=True
            
            MDIconButton:
                icon: "eye-off"
                pos_hint: {"center_y": .5}
                pos: kayit_sifre.width , 0
                theme_text_color: "Hint"
                on_release:
                    self.icon = "eye" if self.icon == "eye-off" else "eye-off"
                    kayit_sifre.password = False if kayit_sifre.password is True else True

        ClickableTextFieldRound:
            size_hint_x: None
            width: "300dp"
            hint_text: "Şifreniz"
            pos_hint: {"center_x": .5, "center_y": .5}
            size_hint_y: None
            height: kayit_sifre.height
            
            MDTextField:
                id:kayit_sifre_tekrar
                hint_text:"Şifrenizi tekrar girin"
                required: False
                helper_text_mode: "on_error"
                helper_text: "Bu Alan Zorunludur!"
                mode:"round"
                md_bg_color:1,1,1,0.2
                size_hint_x:None
                width:200
                font_size:18
                pos_hint:{"center_x":.5}
                password: True
                on_text_validate:app.kaydet()
            
            MDIconButton:
                icon: "eye-off"
                pos_hint: {"center_y": .5}
                pos: kayit_sifre_tekrar.width , 0
                theme_text_color: "Hint"
                on_release:
                    self.icon = "eye" if self.icon == "eye-off" else "eye-off"
                    kayit_sifre_tekrar.password = False if kayit_sifre_tekrar.password is True else True

        MDRoundFlatButton:
            text:"kaydol"
            font_size:12
            pos_hint:{"center_x":.5}
            on_press: app.kaydet()

        MDRoundFlatButton:
            text:"Zaten Kayıtlı mısınız?"
            font_size:12
            pos_hint:{"center_x":.5}
            on_press:app.root.ids.yonetici.current="GirisScreen"

<UnuttumScreen>:
    FitImage:
        size_hint:(1,1)
        source: app.image_path
    MDCard:
        size_hint:None,None
        size: 300, 300
        pos_hint:{"center_x":.5,"center_y":.5}
        md_bg_color:1,1,1,0.1
        elevation:10
        padding:25
        spacing:25
        orientation:"vertical"
        
        MDLabel:
            id:unuttum_label
            text:"Şifrenizi mi unuttunuz?"
            font_size:20
            halign:"center"
            size_hint_y:None
            height:self.texture_size[1]
            padding_y:15

        MDTextField:
            id:unuttum_user
            hint_text:"Öğrenci Numarası"
            required: False
            helper_text_mode: "on_error"
            helper_text: "Öğrenci no giriniz!"
            mode:"round"
            icon_left:"account"
            size_hint_x:None
            width:200
            font_size:18
            pos_hint:{"center_x":.5}
            on_text_validate:root.ids.unuttum_mail.focus=True

        
        MDTextField:
            id:unuttum_mail
            hint_text:"E-Posta Adresiniz"
            required: False
            helper_text_mode: "on_error"
            helper_text: "Bu Alan Zorunludur!"
            mode:"round"
            icon_left:"email"
            md_bg_color:1,1,1,0.2
            size_hint_x:None
            width:200
            font_size:18
            pos_hint:{"center_x":.5}
            on_text_validate:app.mail()

        GridLayout:
            cols:2
            spacing:70
            
            MDRoundFlatButton:
                text:"vazgeç"
                font_size:12
                pos_hint:{"center_x":.5}
                on_press:app.root.ids.yonetici.current="GirisScreen"

            MDRoundFlatButton:
                text:"mail gönder"
                font_size:12
                pos_hint:{"center_x":.5}
                on_press: app.mail()

<MailOnayi>:
    FitImage:
        size_hint:(1,1)
        source: app.image_path

    MDLabel:
        text:""
    MDCard:
        size_hint:None,None
        size: 300, 250
        pos_hint:{"center_x":.5,"center_y":.5}
        md_bg_color:1,1,1,0.1
        elevation:10
        padding:25
        spacing:25
        orientation:"vertical"

        ClickableTextFieldRound:
            size_hint_x: None
            width: "300dp"
            hint_text: "Tek kullanımlık şifreniz"
            pos_hint: {"center_x": .5}
            size_hint_y: None
            height: tek_sifre.height
                        
            MDTextField:
                id:tek_sifre
                hint_text:"Tek kullanımlık şifreniz"
                required: False
                helper_text_mode: "on_error"
                helper_text: "Bu Alan Zorunludur!"
                mode:"round"
                md_bg_color:1,1,1,0.2
                size_hint_x:None
                width:200
                font_size:18
                pos_hint:{"center_x":.5}
                password: True
                on_text_validate:root.ids.unut_ysifre.focus=True
                        
            MDIconButton:
                icon: "eye-off"
                pos_hint: {"center_y": .5}
                pos: tek_sifre.width , 0
                theme_text_color: "Hint"
                on_release:
                    self.icon = "eye" if self.icon == "eye-off" else "eye-off"
                    tek_sifre.password = False if tek_sifre.password is True else True

        ClickableTextFieldRound:
            size_hint_x: None
            width: "300dp"
            hint_text: "Yeni şifreniz"
            pos_hint: {"center_x": .5}
            size_hint_y: None
            height: unut_ysifre.height
                        
            MDTextField:
                id:unut_ysifre
                hint_text:"Yeni şifreniz"
                required: False
                helper_text_mode: "on_error"
                helper_text: "Bu Alan Zorunludur!"
                mode:"round"
                md_bg_color:1,1,1,0.2
                size_hint_x:None
                width:200
                font_size:18
                pos_hint:{"center_x":.5}
                password: True
                on_text_validate: root.ids.unut_ysifre_tekrar.focus=True
                        
            MDIconButton:
                icon: "eye-off"
                pos_hint: {"center_y": .5}
                pos: unut_ysifre.width , 0
                theme_text_color: "Hint"
                on_release:
                    self.icon = "eye" if self.icon == "eye-off" else "eye-off"
                    unut_ysifre.password = False if unut_ysifre.password is True else True

        ClickableTextFieldRound:
            size_hint_x: None
            width: "300dp"
            hint_text: "Yeni şifreniz tekrar"
            pos_hint: {"center_x": .5}
            size_hint_y: None
            height: unut_ysifre_tekrar.height
                        
            MDTextField:
                id:unut_ysifre_tekrar
                hint_text:"Yeni şifrenizi tekrar"
                required: False
                helper_text_mode: "on_error"
                helper_text: "Bu Alan Zorunludur!"
                mode:"round"
                md_bg_color:1,1,1,0.2
                size_hint_x:None
                width:200
                font_size:18
                pos_hint:{"center_x":.5}
                password: True
                on_text_validate:
                    app.unuttum_sifre()
                    root.ids.tek_sifre.text=""
                    root.ids.unut_ysifre.text=""
                    root.ids.unut_ysifre_tekrar.text=""
                    root.ids.tek_sifre.error=False
                    root.ids.unut_ysifre.error=False
                    root.ids.unut_ysifre_tekrar.error=False
                        
            MDIconButton:
                icon: "eye-off"
                pos_hint: {"center_y": .5}
                pos: unut_ysifre_tekrar.width , 0
                theme_text_color: "Hint"
                on_release:
                    self.icon = "eye" if self.icon == "eye-off" else "eye-off"
                    unut_ysifre_tekrar.password = False if unut_ysifre_tekrar.password is True else True

        GridLayout:
            cols:2
            spacing:100
            MDRoundFlatButton:
                text:"Geri"
                font_size:12
                on_press:
                    root.ids.yonetici.current="UnuttumScreen"
                    root.ids.tek_sifre.text=""
                    root.ids.unut_ysifre.text=""
                    root.ids.unut_ysifre_tekrar.text=""
                    root.ids.tek_sifre.error=False
                    root.ids.unut_ysifre.error=False
                    root.ids.unut_ysifre_tekrar.error=False

            MDRoundFlatButton:
                text:"Degistir"
                font_size:12
                on_press:
                    app.unuttum_sifre()
                    root.ids.tek_sifre.text=""
                    root.ids.unut_ysifre.text=""
                    root.ids.unut_ysifre_tekrar.text=""
                    root.ids.tek_sifre.error=False
                    root.ids.unut_ysifre.error=False
                    root.ids.unut_ysifre_tekrar.error=False
    MDLabel:
        text:""
"""
conn=psycopg2.connect("dbname=Kutuphane_Yonetim_Sistemi user=postgres password=11223344Aa.")
c=conn.cursor()

class ClickableTextFieldRound(MDRelativeLayout):
    pass
class GirisScreen(Screen):
    pass
class MenuScreen(Screen):
    pass
class KayitScreen(Screen):
    pass
class UnuttumScreen(Screen):
    pass
class YeniScreen(Screen):
    pass
class EskiScreen(Screen):
    pass
class ToplananScreen(Screen):
    pass
class Ayarlar(Screen):
    pass
class SifreDegis(Screen):
    pass
class MailDegis(Screen):
    pass
class TelDegis(Screen):
    pass
class MailOnayi(Screen):
    pass

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette="Green"
        self.image_path=image_path
        self.root_widget = Builder.load_string(KV)
        return self.root_widget
    # giriş ekranı fonksiyonları
    def gir(self):
        if self.root.ids.GirisScreen.ids.user.text=="" :
            self.root.ids.GirisScreen.ids.user.error=True
        
        elif self.root.ids.GirisScreen.ids.password.text=="":
            self.root.ids.GirisScreen.ids.password.error=True
        
        else:
            u = self.root.ids.GirisScreen.ids.user.text
            p = self.root.ids.GirisScreen.ids.password.text
            sorgu = "SELECT * FROM ogrenci WHERE ono = %s AND sifre = %s"

            try:
                c.execute(sorgu, (u, p))
                sonuc = c.fetchone()
                self.root.ids.GirisScreen.ids.user.helper_text = "Öğrenci Numarası Giriniz"
                self.root.ids.GirisScreen.ids.user.error = False
                if sonuc:
                    global no
                    no = int(u)
                    sorgu = "SELECT * FROM randevu WHERE ono=%s AND tarih>=CURRENT_DATE"
                    c.execute(sorgu, (u,))
                    sonuc = c.fetchall()

                    for record in sonuc:
                        recor = record
                        item = TwoLineListItem(text=f'{record[1]}', secondary_text=f'{record[2]} {record[3]} -> {record[4]}')
                        item.bind(on_release=lambda instance, recor=recor: self.ayrintilar(instance, recor))
                        self.root.ids.lista.add_widget(item)

                    self.root.ids.GirisScreen.ids.user.text = ""
                    self.root.ids.GirisScreen.ids.password.text = ""
                    self.root.ids.GirisScreen.ids.welcome_label.text = "Hoşgeldiniz"
                    self.root.ids.GirisScreen.ids.welcome_label.theme_text_color = "Primary"
                    self.root.ids.yonetici.current = 'MenuScreen'
                else:
                    self.root.ids.GirisScreen.ids.welcome_label.theme_text_color = "Error"
                    self.root.ids.GirisScreen.ids.welcome_label.text = "Ö.no veya Şifre Yanlış"

            except psycopg2.Error as pg_error:
                self.root.ids.GirisScreen.ids.user.helper_text = "Geçersiz Öğrenci Numarası"
                self.root.ids.GirisScreen.ids.user.error = True
                print("PostgreSQL Hatası:", pg_error)

            else:
                print("try bloğu hatasız çalıştı, else bloğuna girildi.")

            
    #kayıt ekranın fonksiyonları
   
    def kaydet(self):
        if self.root.ids.kayit.ids.ono.text=="":
            self.root.ids.kayit.ids.ono.error=True
       
        elif self.root.ids.kayit.ids.isim.text=="":
            self.root.ids.kayit.ids.isim.error=True
       
        elif self.root.ids.kayit.ids.soyisim.text=="":
            self.root.ids.kayit.ids.soyisim.error=True
       
        elif self.root.ids.kayit.ids.telefon.text=="":
            self.root.ids.kayit.ids.telefon.error=True

        elif self.root.ids.kayit.ids.e_posta.text=="":
            self.root.ids.kayit.ids.e_posta.error=True
        
        elif self.root.ids.kayit.ids.kayit_sifre.text=="":
            self.root.ids.kayit.ids.kayit_sifre.error=True
        
        elif self.root.ids.kayit.ids.kayit_sifre_tekrar.text=="":
            self.root.ids.kayit.ids.kayit_sifre_tekrar.error=True
        
        elif self.root.ids.kayit.ids.kayit_sifre_tekrar.text!=self.root.ids.kayit.ids.kayit_sifre.text:
            self.root.ids.kayit.ids.kayit_sifre_tekrar.helper_text="bu alan şifre ile aynı olmalı!"
            self.root.ids.kayit.ids.kayit_sifre_tekrar.error=True
       
        else:
            ono=self.root.ids.kayit.ids.ono.text
            isim=self.root.ids.kayit.ids.isim.text
            soyisim=self.root.ids.kayit.ids.soyisim.text
            tel=self.root.ids.kayit.ids.telefon.text
            posta=self.root.ids.kayit.ids.e_posta.text
            sifre=self.root.ids.kayit.ids.kayit_sifre.text
            
            data=[(ono,isim,soyisim,tel,posta,sifre)]
            insert="INSERT INTO ogrenci (ono,isim,soyisim,telefon,e_posta,sifre) VALUES(%s,%s,%s,%s,%s,%s)"
            
            try:
                self.root.ids.kayit.ids.kayit_label.theme_text_color="Primary"
                c.executemany(insert,data)
                conn.commit()
                self.root.ids.kayit.ids.kayit_label.theme_text_color="Primary"
                self.root.ids.GirisScreen.ids.welcome_label.text="Kayıt Başarılı"
                self.root.ids.yonetici.current= 'GirisScreen'
            except psycopg2.IntegrityError:
                self.root.ids.kayit.ids.kayit_label.theme_text_color="Error"
                self.root.ids.kayit.ids.kayit_label.text="ZATEN KAYITLISINIZ"
            except psycopg2.Error:
                self.root.ids.kayit.ids.kayit_label.theme_text_color="Error"
                self.root.ids.kayit.ids.kayit_label.text="Geçerli değerler girin"
            finally:    
                self.root.ids.kayit.ids.ono.text=""
                self.root.ids.kayit.ids.isim.text=""
                self.root.ids.kayit.ids.soyisim.text=""
                self.root.ids.kayit.ids.telefon.text=""
                self.root.ids.kayit.ids.e_posta.text=""
                self.root.ids.kayit.ids.kayit_sifre.text=""
    
    #şifre unuttum ekranı fonksiyonları
    def mail(self):
        if self.root.ids.unuttum.ids.unuttum_user.text=="" :
            self.root.ids.unuttum.ids.unuttum_user.error=True
        
        elif self.root.ids.unuttum.ids.unuttum_mail.text=="":
            self.root.ids.unuttum.ids.unuttum_mail.error=True
        
        else:
            global u
            u=self.root.ids.unuttum.ids.unuttum_user.text
            p=self.root.ids.unuttum.ids.unuttum_mail.text
            sorgu="SELECT * FROM ogrenci WHERE ono = %s AND e_posta= %s"
            c.execute(sorgu,(u,p))
            sonuc=c.fetchone()
            if sonuc:
                gonderen_email = "kutuphane926@gmail.com"
                gonderen_sifre = "wiqa ibbf aisa gmcz"
                alici_email = p

                # Gmail'in SMTP sunucu bilgileri
                smtp_sunucu = "smtp.gmail.com"
                smtp_port = 587

                # E-posta başlık ve içerik
                konu = "Kütüphane Yönetim Sistemi Tek Kullanımlık Şifre"
                tek_kullanimlik = ''.join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=6))
                icerik = f"Şifreniz: {tek_kullanimlik}"
                
                # MIMEText nesnesini oluştur
                email_icerik = MIMEText(icerik, "plain")

                # MIMEMultipart nesnesini oluştur
                mesaj = MIMEMultipart()
                mesaj.attach(email_icerik)

                # E-posta başlıklarını ayarla
                mesaj["From"] = gonderen_email
                mesaj["To"] = alici_email
                mesaj["Subject"] = konu

                # SMTP bağlantısı oluştur ve e-postayı gönder
                try:
                    # SMTP sunucusuna bağlan
                    server = smtplib.SMTP(smtp_sunucu, smtp_port)
                    server.starttls()
                    
                    # Gmail uygulama şifresini kullanarak giriş yapın
                    server.login(gonderen_email, gonderen_sifre)

                    # E-postayı gönder
                    server.sendmail(gonderen_email, alici_email, mesaj.as_string())

                    # SMTP bağlantısını kapat
                    server.quit()
                    query="UPDATE ogrenci SET mail_kodu=%s WHERE ono=%s"
                    c.execute(query,(tek_kullanimlik,u))
                    conn.commit()
                    self.root.ids.yonetici.current="MailOnayi"
                except Exception as e:
                    self.root.ids.unuttum.ids.unuttum_label.theme_text_color="Error"
                    self.root.ids.unuttum.ids.unuttum_label.text=f'"E-posta gönderme hatası: {e}'

            else:
                self.root.ids.unuttum.ids.unuttum_label.theme_text_color="Error"
                self.root.ids.unuttum.ids.unuttum_label.text="Ö.no veya E-Posta Yanlış"

    def unuttum_sifre(self):
        if self.root.ids.MailOnayi.ids.tek_sifre.text=="":
             self.root.ids.MailOnayi.ids.tek_sifre.error=True
        elif self.root.ids.MailOnayi.ids.unut_ysifre.text=="":
             self.root.ids.MailOnayi.ids.unut_ysifre.error=True
        elif self.root.ids.MailOnayi.ids.unut_ysifre_tekrar.text=="":
             self.root.ids.MailOnayi.ids.unut_ysifre_tekrar.error=True
        else:
            tek=self.root.ids.MailOnayi.ids.tek_sifre.text
            sorgu="SELECT * FROM ogrenci WHERE ono=%s AND mail_kodu=%s"
            global u
            c.execute(sorgu,(u,tek))
            son=c.fetchone()
            if son:
                if self.root.ids.MailOnayi.ids.unut_ysifre.text==self.root.ids.MailOnayi.ids.unut_ysifre_tekrar.text:
                    yeni=self.root.ids.MailOnayi.ids.unut_ysifre_tekrar.text
                    sor="UPDATE ogrenci SET sifre=%s WHERE ono=%s"
                    c.execute(sor,(yeni,u))
                    conn.commit()
                    self.root.ids.MailOnayi.ids.tek_sifre.text=""
                    self.root.ids.MailOnayi.ids.unut_ysifre.text=""
                    self.root.ids.MailOnayi.ids.unut_ysifre_tekrar.text=""
                    self.root.ids.yonetici.current = "GirisScreen"
                else:
                    self.root.ids.MailOnayi.ids.unut_ysifre_tekrar.helper_text="bu alan şifre ile aynı olmalı!"
                    self.root.ids.MailOnayi.ids.unut_ysifre_tekrar.error=True
            else:
                self.root.ids.MailOnayi.ids.tek_sifre.helper_text="şifre hatalı!"
                self.root.ids.MailOnayi.ids.tek_sifre.error=True
    
    #MenuScreen Fonksiyonları
    dialog=None
    def ayrintilar(self, instance,recor):
        md_list = MDList()
        list_items = [
            OneLineListItem(text=f'sandalye: {recor[1]}'),
            OneLineListItem(text=f'tarih:  {recor[2]}'),
            OneLineListItem(text=f'başlangıç: {recor[3]}'),
            OneLineListItem(text=f'bitiş: {recor[4]}')
        ]
        for it in list_items:
            md_list.add_widget(it)

        self.dialog = MDDialog(
            title="Randevu ayrıntıları",
            type="custom",
            content_cls=md_list,
            buttons=[
                MDRoundFlatButton(
                    text="Geri Dön", text_color=self.theme_cls.primary_color, on_release=self.dialog_kapa),
                MDRoundFlatButton(
                    text="Randevuyu Sil", text_color=self.theme_cls.primary_color, on_release=lambda x, rec=recor: self.rand_sil(x, rec))  
            ]
        )
        self.dialog.open()
    
    def dialog_kapa(self,obj):
        self.dialog.dismiss()
    
    def rand_sil(self,obj,rec):
        sorgu="DELETE FROM randevu WHERE ono=%s AND sandalye_id=%s AND tarih=%s AND baslangic=%s AND bitis=%s"
        c.execute(sorgu,(rec[0],rec[1],rec[2],rec[3],rec[4]))
        conn.commit()
        for widget in list(reversed(self.root.ids.lista.children)):
            print(f"Widget: {widget}, Text: {widget.text}, Secondary: {widget.secondary_text} " )
            if isinstance(widget, TwoLineListItem):
                if  (widget.text == f'{rec[1]}' and widget.secondary_text==f'{rec[2]} {rec[3]} -> {rec[4]}'):
                    print("Removing Widget")
                    self.root.ids.lista.remove_widget(widget)
                    self.dialog.dismiss()
                    return
    
    #Yeni Randevu Fonksiyonları
    def show_date_picker(self):
        date_dialog=MDDatePicker()
        date_dialog.bind(on_save=self.on_save,on_cancel=self.on_cancel)
        date_dialog.open()
    
    def on_save(self , instance, value,date_range):
        if value<datetime.date.today():
            self.root.ids.date_button.text="Hatalı Tarih"
            self.root.ids.baslangic.disabled=True
            self.root.ids.bitis.disabled=True
        else:
            self.root.ids.date_button.text = str(value)
            self.root.ids.baslangic.disabled=False
            
    def on_cancel(self,instance,value):
        pass
    
    def show_time_picker(self,item):
        time_dialog=MDTimePicker()
        time_dialog.bind(on_cancel=self.iptal, time=lambda instance, time: self.saat_sec(item, instance, time))
        time_dialog.open()
    
    def saat_sec(self, item, instance, selected_time):
        if datetime.datetime.strptime(self.root.ids.date_button.text, '%Y-%m-%d').date()==datetime.date.today() and selected_time<datetime.datetime.now().time() and item==self.root.ids.baslangic:
            item.text="Hatalı saat"
            self.root.ids.bitis.disabled=True

        elif  item==self.root.ids.bitis and datetime.datetime.strptime(self.root.ids.baslangic.text, '%H:%M').time()>=selected_time :
            item.text="Hatalı saat"
        else:
            formatted_time = selected_time.strftime("%H:%M")
            item.text =  formatted_time
            self.root.ids.bitis.disabled=False
        if self.root.ids.bitis.text!="Hatalı saat" and self.root.ids.bitis.text!="Rezervasyon sonu":
            global no
            tarih=datetime.datetime.strptime(self.root.ids.date_button.text, '%Y-%m-%d').date()
            bas=datetime.datetime.strptime(self.root.ids.baslangic.text, '%H:%M').time()
            bit=datetime.datetime.strptime(self.root.ids.bitis.text, '%H:%M').time()
            for i in range(36):
                sid=f'S{i:04d}'
                soru="SELECT * FROM randevu WHERE sandalye_id=%s AND tarih=%s AND baslangic<%s AND (bitis>%s OR (toplanma_saati IS NOT NULL AND toplanma_saati>%s))"
                c.execute(soru,(sid,tarih,bit,bas,bas))
                cevap=c.fetchone()
                if not cevap:
                    button = getattr(self.root.ids,sid)
                    button.disabled = False
    
    def iptal(self,instance,time):
        pass
    def sec(self,item):
        md_list = MDList()
        list_items = [
            OneLineListItem(text=f'sandalye: {item.text}'),
            OneLineListItem(text=f'tarih:  {self.root.ids.date_button.text}'),
            OneLineListItem(text=f'başlangıç: {self.root.ids.baslangic.text}'),
            OneLineListItem(text=f'bitiş: {self.root.ids.bitis.text}'),
        ]
        for it in list_items:
            md_list.add_widget(it)

        self.dialog = MDDialog(
            title="Randevu ayrıntıları",
            type="custom",
            content_cls=md_list,
            buttons=[
                MDRoundFlatButton(
                    text="Geri Dön", text_color=self.theme_cls.primary_color, on_release=self.dialog_kapa),
                MDRoundFlatButton(
                    text="Onayla", text_color=self.theme_cls.primary_color ,on_release=lambda x,ite=item :self.ekle(x,ite))  
            ]
        )
        self.dialog.open()
    def ekle(self,obj,item):
        merak="INSERT INTO randevu VALUES(%s,%s,%s,%s,%s)"
        global no
        yer=item.text
        gun=datetime.datetime.strptime(self.root.ids.date_button.text, '%Y-%m-%d').date()
        basi=datetime.datetime.strptime(self.root.ids.baslangic.text, '%H:%M').time()
        biti=datetime.datetime.strptime(self.root.ids.bitis.text, '%H:%M').time()
        c.execute(merak,(no,yer,gun,basi,biti))
        conn.commit()
        self.dialog.dismiss()
        self.root.ids.lista.clear_widgets()
        sorgu = "SELECT * FROM randevu WHERE ono=%s AND tarih>=CURRENT_DATE"
        c.execute(sorgu,(no,))
        sonuc = c.fetchall()
        for record in sonuc:
            recor = record
            item = TwoLineListItem(text=f'{record[1]}', secondary_text=f'{record[2]} {record[3]} -> {record[4]}')
            item.bind(on_release=lambda instance, recor=recor: self.ayrintilar(instance, recor))
            self.root.ids.lista.add_widget(item)
        self.root.ids.bitis.disabled=True
        self.root.ids.baslangic.disabled=True
        self.root.ids.date_button.text="tarih seç"
        for i in range(36):
            sid=f'S{i:04d}'
            button = getattr(self.root.ids,sid)
            button.disabled = True
        self.root.ids.yonetici.current="MenuScreen"

   #Geçmiş randevular sayfası 
    def gecmis(self):
        sorgu="SELECT * FROM randevu WHERE ono=%s AND tarih<=CURRENT_DATE"
        global no
        c.execute(sorgu,(no,))
        sonuc=c.fetchall()
        for record in sonuc:
            item=TwoLineListItem(text=f'{record[1]}', secondary_text=f'{record[2]} {record[3]} -> {record[4]}')
            item.bind(on_release=lambda x, record=record: self.gecmis_ayrintilar(record))
            self.root.ids.list.add_widget(item)
        self.root.ids.yonetici.current = "Gecmis"
    
    def gecmis_ayrintilar(self, record):
        md_list = MDList()
        list_items = [
            OneLineListItem(text=f'sandalye: {record[1]}'),
            OneLineListItem(text=f'tarih:  {record[2]}'),
            OneLineListItem(text=f'başlangıç: {record[3]}'),
            OneLineListItem(text=f'bitiş: {record[4]}'),
            OneLineListItem(text=f'eşyalar toplandı: {record[5]}'),
            OneLineListItem(text=f'güvenlik kodu: {record[6]}'),
        ]
        for it in list_items:
            md_list.add_widget(it)

        self.dialog = MDDialog(
            title="Randevu ayrıntıları",
            type="custom",
            content_cls=md_list,
            buttons=[
                MDRoundFlatButton(
                    text="Geri Dön", text_color=self.theme_cls.primary_color, on_release=self.dialog_kapa)
            ]
        )
        self.dialog.open()

    #toplanan eşyalar ekranı
    def toplan(self):
        sorgu="SELECT * FROM randevu WHERE ono=%s AND toplanma_saati is not NULL"
        global no
        c.execute(sorgu,(no,))
        sonuc=c.fetchall()
        for record in sonuc:
            item=TwoLineListItem(text=f'{record[6]}', secondary_text=f'{record[2]} {record[5]}')
            item.bind(on_release=lambda x, record=record: self.gecmis_ayrintilar(record))
            self.root.ids.lis.add_widget(item)
        self.root.ids.yonetici.current = "ToplananScreen"
    
    #Ayarlar ekranının içindeki özellikler
    def yeni_tel(self):
        if self.root.ids.yeni_telefon.text!="":
            tel=int(self.root.ids.yeni_telefon.text)
            global no
            sorgu="UPDATE ogrenci SET telefon=%s WHERE ono=%s"
            c.execute(sorgu,(tel,no))
            conn.commit()
            self.root.ids.yeni_telefon.text=""
            self.root.ids.yonetici.current = "Ayarlar"
    
    def yeni_mail(self):
        if self.root.ids.yeni_posta.text!="":
            posta=self.root.ids.yeni_posta.text
            global no
            sorgu="UPDATE ogrenci SET e_posta=%s WHERE ono=%s"
            c.execute(sorgu,(posta,no))
            conn.commit()
            self.root.ids.yeni_posta.text=""
            self.root.ids.yonetici.current = "Ayarlar"

    def yeni_sifre(self):
        if self.root.ids.degis_sifre.text=="":
             self.root.ids.degis_sifre.error=True
        elif self.root.ids.degis_ysifre.text=="":
             self.root.ids.degis_ysifre.error=True
        elif self.root.ids.degis_ysifre_tekrar.text=="":
             self.root.ids.degis_ysifre_tekrar.error=True
        else:
            mevcut=self.root.ids.degis_sifre.text
            global no
            sorgu="SELECT * FROM ogrenci WHERE ono=%s AND sifre=%s"
            c.execute(sorgu,(no,mevcut))
            son=c.fetchone()
            if son:
                if self.root.ids.degis_ysifre.text==self.root.ids.degis_ysifre_tekrar.text:
                    yeni=self.root.ids.degis_ysifre_tekrar.text
                    sor="UPDATE ogrenci SET sifre=%s WHERE ono=%s"
                    c.execute(sor,(yeni,no))
                    conn.commit()
                    self.root.ids.degis_sifre.text=""
                    self.root.ids.degis_ysifre.text=""
                    self.root.ids.degis_ysifre_tekrar.text=""
                    self.root.ids.yonetici.current = "Ayarlar"
                else:
                    self.root.ids.degis_ysifre_tekrar.helper_text="bu alan şifre ile aynı olmalı!"
                    self.root.ids.degis_ysifre_tekrar.error=True
            else:
                self.root.ids.degis_sifre.helper_text="şifre hatalı!"
                self.root.ids.degis_sifre.error=True
                
    #çıkış fonksiyonu
    def cikis(self):
        global no
        no = ""
        self.root.ids.yonetici.current = "GirisScreen"
        self.root.ids.lista.clear_widgets()

if __name__ == '__main__':
    MainApp().run()