from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,ScreenManager

from kivymd.app import MDApp
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivymd.uix.list import OneLineListItem


#don't forget to copy screen-3rd and  screen-4th in copy of these screens before running the program


KV = """
ScreenManager:
    FirstScreen:
    SecondScreen:
    ThirdScreen:
    FourthScreen:
    SecondScreenCopy1:
    ThirdScreenCopy1:
    FourthScreenCopy1:
    SecondScreenCopy2:
    ThirdScreenCopy2:
    FourthScreenCopy2:

<FirstScreen>:
    name: 'first_screen'
    MDNavigationLayout:
        MDScreenManager:
            MDScreen:

                MDBoxLayout:
                    orientation: "vertical"

                    MDTopAppBar:
                        title:"Indoor Navigation"
                        right_action_items: [["navigation-variant","Let's Navigate!"]]
                        left_action_items: 
                            [
                            [
                            "menu",
                            lambda x: nav_drawer.set_state("open"),
                            "Admins Panel"
                            ]
                            ] 

                        anchor_title: "left"
                        elevation: 4
                        shadow_color: "brown"

            
                    BoxLayout:

                        MDLabel:
                        
                            text:'Welcome!'
                            halign:'center'
                            font_style:'H4'
                            theme_text_color:'Custom'
                            pos_hint:{'center_x':0.5 , 'center_y':0} 
                            text_color:(148/255.0 ,0, 211/255.0 ,1)    

                    BoxLayout:
                        orientation: "vertical"
                        #change this padding below the make the mdrectangleflatbutton  ove up and down on the screen
                        padding: dp(170)

                        MDRectangleFlatButton:
                            text: "NEXT"
                            theme_text_color: "Custom"
                            text_color: "green"
                            line_color: "green"
                            pos_hint:{'center_x':0.5 , 'center_y':0.5} 
                            on_press: root.manager.current = 'second_screen'


        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 13, 13, 0)

           

            BoxLayout:
                orientation:'vertical'
                

                MDNavigationDrawerHeader:
                    title: "Developers "
                    title_color: "#3CB371"  
                    spacing: "1dp"
                    padding: '20dp', '8dp', 0, 0

                BoxLayout:
                    orientation:'vertical'
                    spacing:'1dp'
                    padding:'18dp' 
                              
                    Image:
                        source:"full_size.png"

                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text:'Utkarsh Tonk'
                            IconLeftWidget:
                                icon:'account'
                        OneLineIconListItem:
                            text:'Ankit Rathi'
                            IconLeftWidget:
                                icon:'account'
                        OneLineIconListItem:
                            text:'Angelina Gupta'
                            IconLeftWidget:
                                icon:'account'
                        OneLineIconListItem:
                            text:'Prakhar Kumar Srivastava'
                            IconLeftWidget:
                                icon:'account'
                        OneLineIconListItem:
                            text:'Anup Kumar'      
                            IconLeftWidget:
                                icon:'account'          

                
                
       
<SecondScreen>:
    name:'second_screen' 

    MDIconButton:
        icon: "backburger"
        pos_hint: {"center_x": 0.08, "center_y": 0.94}
        on_press: root.manager.current = 'first_screen'


    MDLabel:
        text: 'Choose Option :'
        font_style:'H5'
        halign:'center' 
        pos_hint: {"center_x": 0.5, 'center_y':0.65}

    MDBoxLayout:
        
        orientation:'horizontal'   
         
        spacing: "30dp"
        padding: "43dp"


        MDCard:
            elevation: 4
            radius: [15]
            size_hint_y: None
            size_hint_x: None
            pos_hint:{'center_x': 0.5,'center_y': 0.5}
            size: "100dp", "100dp"
           
            on_press: root.manager.current = 'third_screen'
            MDFloatLayout:
                MDIconButton:
                    icon: "account"
                    pos_hint: {"center_x": 0.5, "center_y": 0.6}

                MDLabel:
                    text: "TEACHER"
                    halign:'center'
                    size_hint_y: None
                    size_hint_x: None
                    pos_hint:{'center_x': 0.5,'center_y': 0.3}


        MDCard:
            elevation: 4
            radius: [15]
            size_hint_y: None
            size_hint_x: None
            pos_hint:{'center_x': 0.5,'center_y': 0.5}
            size: "100dp", "100dp"
            
            on_press: root.manager.current = 'fourth_screen'
            
            MDFloatLayout:
                MDIconButton:
                    icon: "office-building-marker-outline"
                    pos_hint: {"center_x": 0.5, "center_y": 0.6}

                MDLabel:
                    text: "CABIN"
                    halign:'center'
                    size_hint_y: None
                    size_hint_x: None
                    pos_hint:{'center_x': 0.5,'center_y': 0.3}               


<ThirdScreen>:
    name:'third_screen'
    MDIconButton:
        icon: "backburger"
        pos_hint: {"center_x": 0.08, "center_y": 0.94}
        on_press: root.manager.current = 'second_screen_copy_1'

    MDIconButton:
        icon: 'magnify'
        pos_hint: {"center_x": 0.0918, "center_y": 0.84}
        
    BoxLayout:
        orientation: 'vertical'
        padding: '30dp', '60dp', '20dp', '10dp'

        
        MDTextField:
            id: cabin_field
            hint_text: "Enter Faculty Name "
            helper_text: "or Select From the List Below"
            helper_text_mode: "on_focus"
            pos_hint: {'center_x':0.5, 'center_y':0.6}
            size_hint_x: None
            width: '230dp'
            on_text: root.filter_names(self.text)
        ScrollView:
            do_scroll_x: False
            MDList:
                id: name_list

                       
<FourthScreen>:
    name: 'fourth_screen'  

    MDIconButton:
        icon: "backburger"
        pos_hint: {"center_x": 0.08, "center_y": 0.94}
        on_press: root.manager.current = 'second_screen_copy_1'

    MDIconButton:
        icon: 'magnify'
        pos_hint: {"center_x": 0.0918, "center_y": 0.84}
        
    BoxLayout:
        orientation: 'vertical'
        padding: '30dp', '60dp', '20dp', '10dp'

        
        MDTextField:
            id: cabin_field
            hint_text: "Enter Cabin No. "
            helper_text: "Enter a Cabin No. from 1-89"
            helper_text_mode: "on_focus"
            pos_hint: {'center_x':0.5, 'center_y':0.6}
            size_hint_x: None
            width: '230dp'
            on_text: root.filter_names(self.text)
        ScrollView:
            do_scroll_x: False
            MDList:
                id: name_list

        

# ==================================================================================================================================  

<SecondScreenCopy1>:
    name:'second_screen_copy_1' 

    MDIconButton:
        icon: "backburger"
        pos_hint: {"center_x": 0.08, "center_y": 0.94}
        on_press: root.manager.current = 'first_screen'

    MDLabel:
        text: 'Choose Option :'
        font_style:'H5'
        halign:'center' 
        pos_hint: {"center_x": 0.5, 'center_y':0.65}

    MDBoxLayout:
        
        orientation:'horizontal'   
         
        spacing: "30dp"
        padding: "43dp"


        MDCard:
            elevation: 4
            radius: [15]
            size_hint_y: None
            size_hint_x: None
            pos_hint:{'center_x': 0.5,'center_y': 0.5}
            size: "100dp", "100dp"
           
            on_press: root.manager.current = 'third_screen_copy_1'
            MDFloatLayout:
                MDIconButton:
                    icon: "account"
                    pos_hint: {"center_x": 0.5, "center_y": 0.6}

                MDLabel:
                    text: "TEACHER"
                    halign:'center'
                    size_hint_y: None
                    size_hint_x: None
                    pos_hint:{'center_x': 0.5,'center_y': 0.3}


        MDCard:
            elevation: 4
            radius: [15]
            size_hint_y: None
            size_hint_x: None
            pos_hint:{'center_x': 0.5,'center_y': 0.5}
            size: "100dp", "100dp"
            
            on_press: root.manager.current = 'fourth_screen_copy_1'
            
            MDFloatLayout:
                MDIconButton:
                    icon: "office-building-marker-outline"
                    pos_hint: {"center_x": 0.5, "center_y": 0.6}

                MDLabel:
                    text: "CABIN"
                    halign:'center'
                    size_hint_y: None
                    size_hint_x: None
                    pos_hint:{'center_x': 0.5,'center_y': 0.3} 


# it is the first copy of screen-3rd

<ThirdScreenCopy1>:
    name:'third_screen_copy_1'

    MDIconButton:
        icon: "backburger"
        pos_hint: {"center_x": 0.08, "center_y": 0.94}
        on_press: root.manager.current = 'second_screen_copy_2'

    MDIconButton:
        icon: 'magnify'
        pos_hint: {"center_x": 0.0918, "center_y": 0.84}
        
    BoxLayout:
        orientation: 'vertical'
        padding: '30dp', '60dp', '20dp', '10dp'

        
        MDTextField:
            id: cabin_field
            hint_text: "Enter Faculty Name "
            helper_text: "or Select From the List Below"
            helper_text_mode: "on_focus"
            pos_hint: {'center_x':0.5, 'center_y':0.6}
            size_hint_x: None
            width: '230dp'
            on_text: root.filter_names(self.text)
        ScrollView:
            do_scroll_x: False
            MDList:
                id: name_list
      


# it is the first copy of screen-4th 
<FourthScreenCopy1>:
    name: 'fourth_screen_copy_1'  

    MDIconButton:
        icon: "backburger"
        pos_hint: {"center_x": 0.08, "center_y": 0.94}
        on_press: root.manager.current = 'second_screen_copy_2'

    MDIconButton:
        icon: 'magnify'
        pos_hint: {"center_x": 0.0918, "center_y": 0.84}
        
    BoxLayout:
        orientation: 'vertical'
        padding: '30dp', '60dp', '20dp', '10dp'

        
        MDTextField:
            id: cabin_field
            hint_text: "Enter Cabin No. "
            helper_text: "Enter a Cabin No. from 1-89"
            helper_text_mode: "on_focus"
            pos_hint: {'center_x':0.5, 'center_y':0.6}
            size_hint_x: None
            width: '230dp'
            on_text: root.filter_names(self.text)
        ScrollView:
            do_scroll_x: False
            MDList:
                id: name_list


# ==================================================================================================================================        

# making a 2nd copy of 2nd-screen         
            
<SecondScreenCopy2>:
    name:'second_screen_copy_2' 

    MDIconButton:
        icon: "backburger"
        pos_hint: {"center_x": 0.08, "center_y": 0.94}
        on_press: root.manager.current = 'first_screen'

    MDLabel:
        text: 'Choose Option :'
        font_style:'H5'
        halign:'center' 
        pos_hint: {"center_x": 0.5, 'center_y':0.65}

    MDBoxLayout:
        
        orientation:'horizontal'   
         
        spacing: "30dp"
        padding: "43dp"


        MDCard:
            elevation: 4
            radius: [15]
            size_hint_y: None
            size_hint_x: None
            pos_hint:{'center_x': 0.5,'center_y': 0.5}
            size: "100dp", "100dp"
           
            on_press: root.manager.current = 'third_screen_copy_2'
            MDFloatLayout:
                MDIconButton:
                    icon: "account"
                    pos_hint: {"center_x": 0.5, "center_y": 0.6}

                MDLabel:
                    text: "TEACHER"
                    halign:'center'
                    size_hint_y: None
                    size_hint_x: None
                    pos_hint:{'center_x': 0.5,'center_y': 0.3}


        MDCard:
            elevation: 4
            radius: [15]
            size_hint_y: None
            size_hint_x: None
            pos_hint:{'center_x': 0.5,'center_y': 0.5}
            size: "100dp", "100dp"
            
            on_press: root.manager.current = 'fourth_screen_copy_2'
            
            MDFloatLayout:
                MDIconButton:
                    icon: "office-building-marker-outline"
                    pos_hint: {"center_x": 0.5, "center_y": 0.6}

                MDLabel:
                    text: "CABIN"
                    halign:'center'
                    size_hint_y: None
                    size_hint_x: None
                    pos_hint:{'center_x': 0.5,'center_y': 0.3} 


                    
# it is the second copy of screen-3rd 
<ThirdScreenCopy2>:
    name:'third_screen_copy_2'

    MDIconButton:
        icon: "backburger"
        pos_hint: {"center_x": 0.08, "center_y": 0.94}
        on_press: root.manager.current = 'second_screen_copy_1'

    MDIconButton:
        icon: 'magnify'
        pos_hint: {"center_x": 0.0918, "center_y": 0.84}
        
    BoxLayout:
        orientation: 'vertical'
        padding: '30dp', '60dp', '20dp', '10dp'

        
        MDTextField:
            id: cabin_field
            hint_text: "Enter Faculty Name "
            helper_text: "or Select From the List Below"
            helper_text_mode: "on_focus"
            pos_hint: {'center_x':0.5, 'center_y':0.6}
            size_hint_x: None
            width: '230dp'
            on_text: root.filter_names(self.text)
        ScrollView:
            do_scroll_x: False
            MDList:
                id: name_list
    


# it is the second copy of screen-4th 
<FourthScreenCopy2>:
    name: 'fourth_screen_copy_2'  

    MDIconButton:
        icon: "backburger"
        pos_hint: {"center_x": 0.08, "center_y": 0.94}
        on_press: root.manager.current = 'second_screen_copy_2'

    MDIconButton:
        icon: 'magnify'
        pos_hint: {"center_x": 0.0918, "center_y": 0.84}
        
    BoxLayout:
        orientation: 'vertical'
        padding: '30dp', '60dp', '20dp', '10dp'

        
        MDTextField:
            id: cabin_field
            hint_text: "Enter Cabin No. "
            helper_text: "Enter a Cabin No. from 1-89"
            helper_text_mode: "on_focus"
            pos_hint: {'center_x':0.5, 'center_y':0.6}
            size_hint_x: None
            width: '230dp'
            on_text: root.filter_names(self.text)
        ScrollView:
            do_scroll_x: False
            MDList:
                id: name_list
          

"""
# --------------------------------------------------------------------------------------------------------------------

#define our first screen
class FirstScreen(Screen):
    pass

#define our second screen
class SecondScreen(Screen):
    pass

#define our Third screen
class ThirdScreen(Screen):
    names = [ 
        'pantry',
        'meeting-room',
        'arijit-maitra',
        'suchitra-rajput-chauhan',
        'ashok-suhag',
        'kavita-chawla',
        'saumya-maheshwari' ,
        'shayequa-ali',
        'anubhav-agarwal',
        'anubhav-raj-shekhar', 
        'urmi-gupta',
        'tabish-rasheed', 'rajiv-dey', 'nirupama-m.p.', 'deepti-sharma', 'ajay-kumar-sood', 'rishi-asthana', 'amarnath-bheemaraju', 'ziya-uddin', 'akhlaq-husain', 'sanmitra-barman', 'maheshwar-dwivedy', 'amiya-dash', 'ananda-burra', 'aditya-pratap-singh-rathore', 'satya-prasoon', 'neeraj-kumar-sharma', 'ranbir-singh', 'akhilendra-pratap-singh', 'sunishth-goyal', 'nallan-c.-kaushik', 'a.k.-prasada-rao', 'sushil-chandra', 'pritam-baruah', 'printing-room', 'aditya-chintapant', 'cabin-31', 'yarramaneni-sridhqrbabu', 'ashley-rockenbach', 'indrajeet-singh', 'anantha-rao', 'meeting-room(cabin-36)', 'sambhunath-bera', 'abhimanyu-rana', 'ankit-saxena', 'vikas-kathuria', 'deepak-pandit', 'anirban-chakraborti', 'r&d-cell', 'shyam-menon', 'manoj-k.-arora', 'distinguished-professor', 'school-of-management', 'jaskiran-arora', 'chirag-malik', 'richa-mishra', 'prashant-verma', 'anushree-paul', 'meeting-room(cabin-53)', 'cabin-54', 'manoj-dutta', 'ritu-chhikara', 'vaishali-sharma', 'davinder-singh', 'nandita-choudhary', 'printing-room-2', 'cabin-61', 'sarabjot-singh', 'nistha-phutela', 'gyanesh-jain', 'deepika-dixit', 'harish-puppala', 'subhangi-pandey', 'reserved-for-visiting-faculty', 'cabin-68', 'sumeet-rana', 'meeting-room', 'ruchi-garg', 'arpit-bhardwaj', 'ranjib-banerjee', 'pradesh-kumar-ary', 'jaya-ahuja', 'rik-paul', 'dipankar-das', 'yogesh-gupta', 'kiran-khatter', 'satyendr-singh', 'soharab-hossain-shaikh', 'anuj-agarwal', 'sucheta-sardar', 'sumedh-kulkarni', 'sudha-chandrasekar', 'boardroom', 'atul-mishra', 'kiran-sharma', 'devanjali-relan', 'hirdesh-kr.-pharasi', 'vishal-baloria'

    ]
    
    def on_enter(self, *args):
        self.populate_names()
        
    def populate_names(self):
        self.ids.name_list.clear_widgets()
        for name in self.names:
            self.ids.name_list.add_widget(
                OneLineListItem(text=name, on_release=self.set_name)
            )
            
    def set_name(self, instance):
        # get the selected name
        selected_name = instance.text

        # create a popup with the image of the selected person
        image_source = f"{selected_name}.png"  # assuming the image file name matches the name in the menu
        image = Image(source=image_source)
        popup = Popup(title=selected_name, content=image, size_hint=(1, 0.45))

        # open the popup
        popup.open()

        # clear the list of names
        self.ids.name_list.clear_widgets()

        # set the selected name as the text of the text field
        self.ids.cabin_field.text = selected_name
        
    def filter_names(self, text):
        filtered_names = [name for name in self.names if text.lower() in name.lower()]
        self.ids.name_list.clear_widgets()
        for name in filtered_names:
            self.ids.name_list.add_widget(
                OneLineListItem(text=name, on_release=self.set_name)
            )


#define our fourth screen
class FourthScreen(Screen):

    names = [ 
        'cabin-1',
        'cabin-2',
        'cabin-3',
        'cabin-4',
        'cabin-5',
        'cabin-6',
        'cabin-7',
        'cabin-8',
        'cabin-9',
        'cabin-10',
        'cabin-11',
        'cabin-12',
        'cabin-13',
        'cabin-14',
        'cabin-15',
        'cabin-16',
        'cabin-17',
        'cabin-18',
        'cabin-19',
        'cabin-20',
        'cabin-21',
        'cabin-22',
        'cabin-23',
        'cabin-24',
        'cabin-25',
        'cabin-26',
        'cabin-27',
        'cabin-28',
        'cabin-29',
        'cabin-30',
        'cabin-31',
        'cabin-32',
        'cabin-33',
        'cabin-34',
        'cabin-35',
        'cabin-36',
        'cabin-37',
        'cabin-38',
        'cabin-39',
        'cabin-40',
        'cabin-41',
        'cabin-42',
        'cabin-43',
        'cabin-44',
        'cabin-45',
        'cabin-46',
        'cabin-47',
        'cabin-48',
        'cabin-49',
        'cabin-50',
        'cabin-51',
        'cabin-52',
        'cabin-53',
        'cabin-54',
        'cabin-55',
        'cabin-56',
        'cabin-57',
        'cabin-58',
        'cabin-59',
        'cabin-60',
        'cabin-61',
        'cabin-62',
        'cabin-63',
        'cabin-64',
        'cabin-65',
        'cabin-66',
        'cabin-67',
        'cabin-68',
        'cabin-69',
        'cabin-60',
        'cabin-71',
        'cabin-72',
        'cabin-73',
        'cabin-74',
        'cabin-75',
        'cabin-76',
        'cabin-77',
        'cabin-78',
        'cabin-79',
        'cabin-80',
        'cabin-81',
        'cabin-82',
        'cabin-83',
        'cabin-84',
        'cabin-85',
        'cabin-86',
        'cabin-87',
        'cabin-88',
        'cabin-89',
    ]
    
    def on_enter(self, *args):
        self.populate_names()
        
    def populate_names(self):
        self.ids.name_list.clear_widgets()
        for name in self.names:
            self.ids.name_list.add_widget(
                OneLineListItem(text=name, on_release=self.set_name)
            )
            
    def set_name(self, instance):
        # get the selected name
        selected_name = instance.text

        # create a popup with the image of the selected person
        image_source = f"{selected_name}.png"  # assuming the image file name matches the name in the menu
        image = Image(source=image_source)
        popup = Popup(title=selected_name, content=image, size_hint=(1, 0.45))

        # open the popup
        popup.open()

        # clear the list of names
        self.ids.name_list.clear_widgets()

        # set the selected name as the text of the text field
        self.ids.cabin_field.text = selected_name
        
    def filter_names(self, text):
        filtered_names = [name for name in self.names if text.lower() in name.lower()]
        self.ids.name_list.clear_widgets()
        for name in filtered_names:
            self.ids.name_list.add_widget(
                OneLineListItem(text=name, on_release=self.set_name)
            )




# --------------------------------------------------------------------------------------------------------------------

#define our first copy of second screen
class SecondScreenCopy1(Screen):
    pass

#define our first copy of third screen
class ThirdScreenCopy1(Screen):
    names = [ 
        'pantry',
        'meeting-room',
        'arijit-maitra',
        'suchitra-rajput-chauhan',
        'ashok-suhag',
        'kavita-chawla',
        'saumya-maheshwari' ,
        'shayequa-ali',
        'anubhav-agarwal',
        'anubhav-raj-shekhar', 
        'urmi-gupta',
        'tabish-rasheed', 'rajiv-dey', 'nirupama-m.p.', 'deepti-sharma', 'ajay-kumar-sood', 'rishi-asthana', 'amarnath-bheemaraju', 'ziya-uddin', 'akhlaq-husain', 'sanmitra-barman', 'maheshwar-dwivedy', 'amiya-dash', 'ananda-burra', 'aditya-pratap-singh-rathore', 'satya-prasoon', 'neeraj-kumar-sharma', 'ranbir-singh', 'akhilendra-pratap-singh', 'sunishth-goyal', 'nallan-c.-kaushik', 'a.k.-prasada-rao', 'sushil-chandra', 'pritam-baruah', 'printing-room', 'aditya-chintapant', 'cabin-31', 'yarramaneni-sridhqrbabu', 'ashley-rockenbach', 'indrajeet-singh', 'anantha-rao', 'meeting-room(cabin-36)', 'sambhunath-bera', 'abhimanyu-rana', 'ankit-saxena', 'vikas-kathuria', 'deepak-pandit', 'anirban-chakraborti', 'r&d-cell', 'shyam-menon', 'manoj-k.-arora', 'distinguished-professor', 'school-of-management', 'jaskiran-arora', 'chirag-malik', 'richa-mishra', 'prashant-verma', 'anushree-paul', 'meeting-room(cabin-53)', 'cabin-54', 'manoj-dutta', 'ritu-chhikara', 'vaishali-sharma', 'davinder-singh', 'nandita-choudhary', 'printing-room-2', 'cabin-61', 'sarabjot-singh', 'nistha-phutela', 'gyanesh-jain', 'deepika-dixit', 'harish-puppala', 'subhangi-pandey', 'reserved-for-visiting-faculty', 'cabin-68', 'sumeet-rana', 'meeting-room', 'ruchi-garg', 'arpit-bhardwaj', 'ranjib-banerjee', 'pradesh-kumar-ary', 'jaya-ahuja', 'rik-paul', 'dipankar-das', 'yogesh-gupta', 'kiran-khatter', 'satyendr-singh', 'soharab-hossain-shaikh', 'anuj-agarwal', 'sucheta-sardar', 'sumedh-kulkarni', 'sudha-chandrasekar', 'boardroom', 'atul-mishra', 'kiran-sharma', 'devanjali-relan', 'hirdesh-kr.-pharasi', 'vishal-baloria'

    ]
    
    def on_enter(self, *args):
        self.populate_names()
        
    def populate_names(self):
        self.ids.name_list.clear_widgets()
        for name in self.names:
            self.ids.name_list.add_widget(
                OneLineListItem(text=name, on_release=self.set_name)
            )
            
    def set_name(self, instance):
        # get the selected name
        selected_name = instance.text

        # create a popup with the image of the selected person
        image_source = f"{selected_name}.png"  # assuming the image file name matches the name in the menu
        image = Image(source=image_source)
        popup = Popup(title=selected_name, content=image, size_hint=(1, 0.45))

        # open the popup
        popup.open()

        # clear the list of names
        self.ids.name_list.clear_widgets()

        # set the selected name as the text of the text field
        self.ids.cabin_field.text = selected_name
        
    def filter_names(self, text):
        filtered_names = [name for name in self.names if text.lower() in name.lower()]
        self.ids.name_list.clear_widgets()
        for name in filtered_names:
            self.ids.name_list.add_widget(
                OneLineListItem(text=name, on_release=self.set_name)
            )

    
       

#define our first copy of fourth screen
class FourthScreenCopy1(Screen):

    names = [ 
        'cabin-1',
        'cabin-2',
        'cabin-3',
        'cabin-4',
        'cabin-5',
        'cabin-6',
        'cabin-7',
        'cabin-8',
        'cabin-9',
        'cabin-10',
        'cabin-11',
        'cabin-12',
        'cabin-13',
        'cabin-14',
        'cabin-15',
        'cabin-16',
        'cabin-17',
        'cabin-18',
        'cabin-19',
        'cabin-20',
        'cabin-21',
        'cabin-22',
        'cabin-23',
        'cabin-24',
        'cabin-25',
        'cabin-26',
        'cabin-27',
        'cabin-28',
        'cabin-29',
        'cabin-30',
        'cabin-31',
        'cabin-32',
        'cabin-33',
        'cabin-34',
        'cabin-35',
        'cabin-36',
        'cabin-37',
        'cabin-38',
        'cabin-39',
        'cabin-40',
        'cabin-41',
        'cabin-42',
        'cabin-43',
        'cabin-44',
        'cabin-45',
        'cabin-46',
        'cabin-47',
        'cabin-48',
        'cabin-49',
        'cabin-50',
        'cabin-51',
        'cabin-52',
        'cabin-53',
        'cabin-54',
        'cabin-55',
        'cabin-56',
        'cabin-57',
        'cabin-58',
        'cabin-59',
        'cabin-60',
        'cabin-61',
        'cabin-62',
        'cabin-63',
        'cabin-64',
        'cabin-65',
        'cabin-66',
        'cabin-67',
        'cabin-68',
        'cabin-69',
        'cabin-60',
        'cabin-71',
        'cabin-72',
        'cabin-73',
        'cabin-74',
        'cabin-75',
        'cabin-76',
        'cabin-77',
        'cabin-78',
        'cabin-79',
        'cabin-80',
        'cabin-81',
        'cabin-82',
        'cabin-83',
        'cabin-84',
        'cabin-85',
        'cabin-86',
        'cabin-87',
        'cabin-88',
        'cabin-89',
    ]
    
    def on_enter(self, *args):
        self.populate_names()
        
    def populate_names(self):
        self.ids.name_list.clear_widgets()
        for name in self.names:
            self.ids.name_list.add_widget(
                OneLineListItem(text=name, on_release=self.set_name)
            )
            
    def set_name(self, instance):
        # get the selected name
        selected_name = instance.text

        # create a popup with the image of the selected person
        image_source = f"{selected_name}.png"  # assuming the image file name matches the name in the menu
        image = Image(source=image_source)
        popup = Popup(title=selected_name, content=image, size_hint=(1, 0.45))

        # open the popup
        popup.open()

        # clear the list of names
        self.ids.name_list.clear_widgets()

        # set the selected name as the text of the text field
        self.ids.cabin_field.text = selected_name
        
    def filter_names(self, text):
        filtered_names = [name for name in self.names if text.lower() in name.lower()]
        self.ids.name_list.clear_widgets()
        for name in filtered_names:
            self.ids.name_list.add_widget(
                OneLineListItem(text=name, on_release=self.set_name)
            )


# --------------------------------------------------------------------------------------------------------------------


#define our second copy of second screen
class SecondScreenCopy2(Screen):
    pass

#define our second copy of third screen
class ThirdScreenCopy2(Screen):
   
    names = [ 
        'pantry',
        'meeting-room',
        'arijit-maitra',
        'suchitra-rajput-chauhan',
        'ashok-suhag',
        'kavita-chawla',
        'saumya-maheshwari' ,
        'shayequa-ali',
        'anubhav-agarwal',
        'anubhav-raj-shekhar', 
        'urmi-gupta',
        'tabish-rasheed', 'rajiv-dey', 'nirupama-m.p.', 'deepti-sharma', 'ajay-kumar-sood', 'rishi-asthana', 'amarnath-bheemaraju', 'ziya-uddin', 'akhlaq-husain', 'sanmitra-barman', 'maheshwar-dwivedy', 'amiya-dash', 'ananda-burra', 'aditya-pratap-singh-rathore', 'satya-prasoon', 'neeraj-kumar-sharma', 'ranbir-singh', 'akhilendra-pratap-singh', 'sunishth-goyal', 'nallan-c.-kaushik', 'a.k.-prasada-rao', 'sushil-chandra', 'pritam-baruah', 'printing-room', 'aditya-chintapant', 'cabin-31', 'yarramaneni-sridhqrbabu', 'ashley-rockenbach', 'indrajeet-singh', 'anantha-rao', 'meeting-room(cabin-36)', 'sambhunath-bera', 'abhimanyu-rana', 'ankit-saxena', 'vikas-kathuria', 'deepak-pandit', 'anirban-chakraborti', 'r&d-cell', 'shyam-menon', 'manoj-k.-arora', 'distinguished-professor', 'school-of-management', 'jaskiran-arora', 'chirag-malik', 'richa-mishra', 'prashant-verma', 'anushree-paul', 'meeting-room(cabin-53)', 'cabin-54', 'manoj-dutta', 'ritu-chhikara', 'vaishali-sharma', 'davinder-singh', 'nandita-choudhary', 'printing-room-2', 'cabin-61', 'sarabjot-singh', 'nistha-phutela', 'gyanesh-jain', 'deepika-dixit', 'harish-puppala', 'subhangi-pandey', 'reserved-for-visiting-faculty', 'cabin-68', 'sumeet-rana', 'meeting-room', 'ruchi-garg', 'arpit-bhardwaj', 'ranjib-banerjee', 'pradesh-kumar-ary', 'jaya-ahuja', 'rik-paul', 'dipankar-das', 'yogesh-gupta', 'kiran-khatter', 'satyendr-singh', 'soharab-hossain-shaikh', 'anuj-agarwal', 'sucheta-sardar', 'sumedh-kulkarni', 'sudha-chandrasekar', 'boardroom', 'atul-mishra', 'kiran-sharma', 'devanjali-relan', 'hirdesh-kr.-pharasi', 'vishal-baloria'

    ]
    
    def on_enter(self, *args):
        self.populate_names()
        
    def populate_names(self):
        self.ids.name_list.clear_widgets()
        for name in self.names:
            self.ids.name_list.add_widget(
                OneLineListItem(text=name, on_release=self.set_name)
            )
            
    def set_name(self, instance):
        # get the selected name
        selected_name = instance.text

        # create a popup with the image of the selected person
        image_source = f"{selected_name}.png"  # assuming the image file name matches the name in the menu
        image = Image(source=image_source)
        popup = Popup(title=selected_name, content=image, size_hint=(1, 0.45))

        # open the popup
        popup.open()

        # clear the list of names
        self.ids.name_list.clear_widgets()

        # set the selected name as the text of the text field
        self.ids.cabin_field.text = selected_name
        
    def filter_names(self, text):
        filtered_names = [name for name in self.names if text.lower() in name.lower()]
        self.ids.name_list.clear_widgets()
        for name in filtered_names:
            self.ids.name_list.add_widget(
                OneLineListItem(text=name, on_release=self.set_name)
            )


#define our second copy of fourth screen
class FourthScreenCopy2(Screen):
    names = [ 
        'cabin-1',
        'cabin-2',
        'cabin-3',
        'cabin-4',
        'cabin-5',
        'cabin-6',
        'cabin-7',
        'cabin-8',
        'cabin-9',
        'cabin-10',
        'cabin-11',
        'cabin-12',
        'cabin-13',
        'cabin-14',
        'cabin-15',
        'cabin-16',
        'cabin-17',
        'cabin-18',
        'cabin-19',
        'cabin-20',
        'cabin-21',
        'cabin-22',
        'cabin-23',
        'cabin-24',
        'cabin-25',
        'cabin-26',
        'cabin-27',
        'cabin-28',
        'cabin-29',
        'cabin-30',
        'cabin-31',
        'cabin-32',
        'cabin-33',
        'cabin-34',
        'cabin-35',
        'cabin-36',
        'cabin-37',
        'cabin-38',
        'cabin-39',
        'cabin-40',
        'cabin-41',
        'cabin-42',
        'cabin-43',
        'cabin-44',
        'cabin-45',
        'cabin-46',
        'cabin-47',
        'cabin-48',
        'cabin-49',
        'cabin-50',
        'cabin-51',
        'cabin-52',
        'cabin-53',
        'cabin-54',
        'cabin-55',
        'cabin-56',
        'cabin-57',
        'cabin-58',
        'cabin-59',
        'cabin-60',
        'cabin-61',
        'cabin-62',
        'cabin-63',
        'cabin-64',
        'cabin-65',
        'cabin-66',
        'cabin-67',
        'cabin-68',
        'cabin-69',
        'cabin-60',
        'cabin-71',
        'cabin-72',
        'cabin-73',
        'cabin-74',
        'cabin-75',
        'cabin-76',
        'cabin-77',
        'cabin-78',
        'cabin-79',
        'cabin-80',
        'cabin-81',
        'cabin-82',
        'cabin-83',
        'cabin-84',
        'cabin-85',
        'cabin-86',
        'cabin-87',
        'cabin-88',
        'cabin-89',
    ]
    
    def on_enter(self, *args):
        self.populate_names()
        
    def populate_names(self):
        self.ids.name_list.clear_widgets()
        for name in self.names:
            self.ids.name_list.add_widget(
                OneLineListItem(text=name, on_release=self.set_name)
            )
            
    def set_name(self, instance):
        # get the selected name
        selected_name = instance.text

        # create a popup with the image of the selected person
        image_source = f"{selected_name}.png"  # assuming the image file name matches the name in the menu
        image = Image(source=image_source)
        popup = Popup(title=selected_name, content=image, size_hint=(1, 0.45))

        # open the popup
        popup.open()

        # clear the list of names
        self.ids.name_list.clear_widgets()

        # set the selected name as the text of the text field
        self.ids.cabin_field.text = selected_name
        
    def filter_names(self, text):
        filtered_names = [name for name in self.names if text.lower() in name.lower()]
        self.ids.name_list.clear_widgets()
        for name in filtered_names:
            self.ids.name_list.add_widget(
                OneLineListItem(text=name, on_release=self.set_name)
            )


# --------------------------------------------------------------------------------------------------------------------


sm = ScreenManager()
sm.add_widget(FirstScreen(name='first_screen'))
sm.add_widget(SecondScreen(name='second_screen'))
sm.add_widget(ThirdScreen(name='third_screen'))
sm.add_widget(FourthScreen(name='fourth_screen'))
sm.add_widget(SecondScreenCopy1(name='second_screen_copy_1'))
sm.add_widget(ThirdScreenCopy1(name='third_screen_copy_1'))
sm.add_widget(FourthScreenCopy1(name='fourth_screen_copy_1')) 
sm.add_widget(SecondScreenCopy2(name='second_screen_copy_2'))
sm.add_widget(ThirdScreenCopy2(name='third_screen_copy_2'))
sm.add_widget(FourthScreenCopy2(name='fourth_screen_copy_2')) 






class DemoApp(MDApp):
    def build(self):
        self.icon= 'app-logo.png'
        self.title='INS'
        self.theme_cls.primary_palette = "Cyan"
        screen = Builder.load_string(KV)
        return screen
    

if __name__ == '__main__':
    DemoApp().run()
