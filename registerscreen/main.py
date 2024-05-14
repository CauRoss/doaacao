<LoginScreen>:
    name: 'criar_login'
    Image:
        source: 'logo.png'
        size_hint: (0.7, 0.7)
        pos_hint: {'center_x': 0.5, 'center_y': 0.85}
    MDLabel:
        text: 'DoaAção'
        bold: True
        halign: 'center'
        pos_hint: {'center_x': 0.5, 'center_y': 0.72}
    MDLabel:
        text: 'Login'
        font_size: dp(23)
        bold: True
        halign: 'center'
        pos_hint: {'center_x': 0.18, 'center_y': 0.47}
    MDTextField:
        hint_text: 'Email'
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        icon_right: 'email'
        size_hint_x: .8
        text_color: (3, 187, 133)
        
    MDTextField:
        hint_text: 'Senha'
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        size_hint_x: .8
        icon_right: 'lock'
        password: True
        
    MDRaisedButton:
        text: 'Login'
        text_color: 1,1,1,1
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        size_hint_x: .8
        elevation:0
        on_release: root.manager.current = 'menu_screen'
    MDTextButton:
        text: 'Ainda não tem uma conta? [u]Cadastre-se.[/u]'
        bold: True
        markup: True
        halign: 'center'
        pos_hint: {'center_x': 0.5, 'center_y': 0.09}
        font_size: dp(10)
        size_hint_x: .8
        on_release:    
            root.manager.current = 'criar_cadastro'
            root.manager.transition.direction = 'left'



<RegisterScreen>:
    name: 'criar_cadastro'
    MDIconButton:
        icon: 'arrow-left'
        theme_text_color: 'Custom'
        text_color: (0, 128, 128)
        pos_hint: {'center_x': 0.05, 'center_y': 0.97}
        on_release: 
            root.manager.current = 'criar_login'
            root.manager.transition.direction = 'right'
    Image:
        source: 'logo.png'
        size_hint: (0.7, 0.7)
        pos_hint: {'center_x': 0.5, 'center_y': 0.85}
    MDLabel:
        text: 'DoaAção'
        bold: True
        halign: 'center'
        pos_hint: {'center_x': 0.5, 'center_y': 0.72}
    MDLabel:
        text: 'Novo usuário'
        font_size: dp(23)
        bold: True
        halign: 'center'
        pos_hint: {'center_x': 0.29, 'center_y': 0.47}
    MDTextField:
        hint_text: 'Nome de usuário'
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        icon_right: 'account'
        size_hint_x: .8   
    MDTextField:
        hint_text: 'Email'
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        icon_right: 'email'
        size_hint_x: .8
    MDTextField:
        hint_text: 'Senha'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        size_hint_x: .8
        icon_right: 'lock'
        password: True
    MDRaisedButton:
        text: 'Criar conta'
        text_color: 1,1,1,1
        pos_hint: {'center_x': 0.5, 'center_y': 0.13}
        size_hint_x: .8
        elevation:0
        on_release: 
            root.manager.current = 'menu_screen'
            root.manager.transition.direction = 'left'
    MDTextButton:
        text: 'Já possui uma conta? [u]Faça login.[/u]'
        bold: True
        markup: True
        halign: 'center'
        pos_hint: {'center_x': 0.5, 'center_y': 0.09}
        font_size: dp(10)
        size_hint_x: .8
        on_release: 
            root.manager.current  = 'criar_login'
            root.manager.transition.direction = 'right'

<MenuScreen>:
    name: 'menu_screen'
    MDNavigationLayout:
        ScreenManager:
            Screen:
                MDBottomNavigation:
                    background_color: 1, 1, 1, 1
                    selected_color_background: 'teal'
                    text_color_active: 'lightgray'

                    MDBottomNavigationItem:
                        name: 'primeira tela'
                        text: 'Home'
                        icon: 'home'
                        halign: 'center'
                        MDTopAppBar:
                            pos_hint: {'center_x': 0.5, 'center_y': 0.967}  # Posiciona a barra de topo no topo da tela
                            elevation: 0  # Ajusta a elevação (sombreamento) da barra de topo
                            MDIconButton:
                                icon: 'dots-vertical'
                                theme_text_color: 'Custom'
                                text_color: 1,1,1,1
                                pos_hint: {'center_x': 0.96, 'center_y': 0.99}

                        MDLabel:
                            text: 'Home'
                            halign: 'center'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.96}
                            bold: True
                            font_size: dp(20)
                            theme_text_color: 'Custom'
                            text_color: 1,1,1,1
                        MDFloatLayout:
                            
                            MDCard:
                                style: "elevated"
                                paddind: '4dp'
                                size_hint: None, None
                                size: '320dp', '170dp'
                                pos_hint: {'center_x': 0.5, 'center_y': 0.77}
                                FitImage:
                                    source: 'eee.jpg'
                                    size_hint: (1.0, 1.0)
                                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                                    radius: 10
                                    allow_stretch: True
                                    keep_ratio: False


                                    
                    
                    MDBottomNavigationItem:
                        name: 'segunda tela'
                        text: 'Explorar'
                        icon: 'magnify'
                        halign: 'center'
                        MDTopAppBar:
                            pos_hint: {'center_x': 0.5, 'center_y': 0.967}
                            elevation: 0 


                    MDBottomNavigationItem:
                        name: 'terceira tela'
                        text: 'Perfil'
                        icon: 'account'
                        halign: 'center'

                        Image:
                            source: '3135823.png'
                            size_hint: (0.4, 0.40)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.85}
                        
                        
                        MDFillRoundFlatButton:
                            text: '    Editar perfil    '
                            bold: True
                            text_color: 1,1,1,1
                            pos_hint: {'center_x': 0.5, 'center_y': 0.68}
                            size_hint_x: .2
                            elevation: 0
                            on_release: 
                                root.manager.current = 'editar_perfil'
                                root.manager.transition.direction = 'left'
                        MDFloatLayout:
                            
                            MDList:
                                pos_hint: {'center_x': 0.5, 'center_y': 0.35}
                                OneLineAvatarIconListItem:
                                    text: 'Minhas campanhas'
                                    IconLeftWidget:
                                        icon: 'campanha.png'
                                OneLineAvatarIconListItem:
                                    text: 'Minhas doações'
                                    IconLeftWidget:
                                        icon: 'doacao.png'
               
                                OneLineAvatarIconListItem:
                                    text: 'Favoritos'
                                    IconLeftWidget:
                                        icon: 'star'
                                OneLineAvatarIconListItem:
                                    text: 'Configurações'
                                    IconLeftWidget:
                                        icon: 'cog'

<EditarPerfil>
    name: 'editar_perfil'
    MDIconButton:
        icon: 'arrow-left'
        theme_text_color: 'Custom'
        text_color: (0, 128, 128)
        pos_hint: {'center_x': 0.05, 'center_y': 0.97}
        on_release: 
            root.manager.current = 'menu_screen'
            root.manager.transition.direction = 'right'
    Image:
        source: '3135823.png'
        size_hint: (0.4, 0.40)
        pos_hint: {'center_x': 0.5, 'center_y': 0.85}
    MDLabel:
        text: 'Novo nome de usuário:'
        font_size: dp(12)
        bold: True
        halign: 'center'
        pos_hint: {'center_x': 0.33, 'center_y': 0.65}
    MDTextField:
        hint_text: 'Nome de usuário'
        mode: 'round'
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        icon_right: 'account'
        size_hint_x: .8
    MDLabel:
        text: 'Novo email:'
        font_size: dp(12)
        bold: True
        halign: 'center'
        pos_hint: {'center_x': 0.25, 'center_y': 0.55}   
    MDTextField:
        hint_text: 'Email'
        mode: 'round'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        icon_right: 'email'
        size_hint_x: .8
    MDLabel:
        text: 'Nova senha:'
        font_size: dp(12)
        bold: True
        halign: 'center'
        pos_hint: {'center_x': 0.25, 'center_y': 0.45}  
    MDTextField:
        hint_text: 'Senha'
        mode: 'round'
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        size_hint_x: .8
        icon_right: 'lock'
        password: True
    MDRaisedButton:
        text: 'Confirmar alterações'
        text_color: 1,1,1,1
        pos_hint: {'center_x': 0.5, 'center_y': 0.13}
        size_hint_x: .8
        elevation:0
        on_release: 
            root.manager.current = 'menu_screen'
            root.manager.transition.direction = 'right'              
                                

                                              
