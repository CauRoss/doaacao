<SplashScreen>
    name: 'tela de carregamento'
    Image:
        source: 'logo.png'
        size_hint: (0.9, 0.9)
        pos_hint: {'center_x': 0.5, 'center_y': 0.55}
    MDLabel:
        text: 'DoaAção'
        bold: True
        halign: 'center'
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        font_size: dp(30)
    

<LoginScreen>:
    name: 'criar_login'
    Image:
        source: 'logo.png'
        size_hint: (0.7, 0.7)
        pos_hint: {'center_x': 0.5, 'center_y': 0.85}
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
        source: 'logo.png' #nessa propriedade eu indico de onde essa imagem está vindo
        size_hint: (0.7, 0.7)   #nessa aqui eu ajusto o tamanho da imagem
        pos_hint: {'center_x': 0.5, 'center_y': 0.85} #já nessa,  eu ajusto sua posição na tela
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
                            pos_hint: {'center_x': 0.5, 'center_y': 0.967}
                            elevation: 0 
                        MDTextField:
                            hint_text: 'Pesquisar por campanhas'
                            mode: 'round'
                            padding: 10
                            size_hint_x: 0.9
                            pos_hint: {'center_x': 0.5, 'center_y': 0.953}  
                            icon_left: 'magnify'
                        MDCard:
                            style: 'elevated'
                            size_hint: (0.87, 0.27)    
                            pos_hint: {'center_x': 0.5, 'center_y': 0.75}
                            FitImage:
                                source: 'eee.jpg'
                                allow_stretch: True
                                keep_ratio: False
                                radius: 15
                        MDFillRoundFlatButton:
                            text: 'Crie sua campanha já!'
                            text_color: 1,1,1,1
                            pos_hint: {'center_x': 0.5, 'center_y': 0.655}
                            size_hint_x: .8
                            elevation: 0

                    MDBottomNavigationItem:
                        name: 'segunda tela'
                        id: 'criar campanha'
                        text: 'Criar'
                        icon: 'plus'
                        halign: 'center'
                        MDTopAppBar:
                            pos_hint: {'center_x': 0.5, 'center_y': 0.967}
                            elevation: 0
                        MDLabel:
                            text: 'Criar'
                            bold: True
                            halign: 'center'
                            font_size: dp(20)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.955}
                            theme_text_color: 'Custom'
                            text_color: 1, 1, 1, 1


                    MDBottomNavigationItem:
                        name: 'terceira tela'
                        text: 'Perfil'
                        icon: 'account'
                        halign: 'center'

                        Image:
                            source: 'conta.png'
                            size_hint: (0.4, 0.4)
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
                                pos_hint: {'center_x': 0.5, 'center_y': 0.27}
                                OneLineAvatarIconListItem:
                                    text: 'Minhas campanhas'
                                    on_release: 
                                        root.manager.current = 'minhas_campanhas'
                                        root.manager.transition.direction = 'left'
                                    IconLeftWidget:
                                        icon: 'campanha.png'
                                        on_release: 
                                            root.manager.current = 'minhas_doacoes'
                                            root.manager.transition.direction = 'left'
                                OneLineAvatarIconListItem:
                                    text: 'Minhas doações'
                                    on_release: 
                                        root.manager.current = 'minhas_doacoes'
                                        root.manager.transition.direction = 'left'
                                    IconLeftWidget:
                                        icon: 'doacao.png'
                                        on_release: 
                                            root.manager.current = 'minhas_doacoes'
                                            root.manager.transition.direction = 'left'
               
                                OneLineAvatarIconListItem:
                                    text: 'Favoritos'
                                    on_release: 
                                        root.manager.current = 'favoritos'
                                        root.manager.transition.direction = 'left'
                                    IconLeftWidget:
                                        icon: 'star'
                                        on_release: 
                                            root.manager.current = 'configuracoes'
                                            root.manager.transition.direction = 'left'
                                OneLineAvatarIconListItem:
                                    text: 'Configurações'
                                    on_release: 
                                        root.manager.current = 'configuracoes'
                                        root.manager.transition.direction = 'left'
                                    IconLeftWidget:
                                        icon: 'cog'
                                        on_release: 
                                            root.manager.current = 'configuracoes'
                                            root.manager.transition.direction = 'left'
                                OneLineAvatarIconListItem:
                                    text: 'Logout'
                                    on_release: app.show_alert_dialog()
                                    IconLeftWidget:
                                        icon: 'logout'
                                        on_release: app.show_alert_dialog()

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
        source: 'conta.png'
        size_hint: (0.4, 0.40)
        pos_hint: {'center_x': 0.5, 'center_y': 0.85}
    MDLabel:
        text: 'Novo nome de usuário:'
        font_size: dp(12)
        bold: True
        halign: 'center'
        pos_hint: {'center_x': 0.35, 'center_y': 0.65}
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

<MinhasCampanhas>
    name: 'minhas_campanhas'
    MDTopAppBar:
        pos_hint: {'center_x': 0.5, 'center_y': 0.967}
        elevation: 0
        MDIconButton:
            icon: 'arrow-left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            pos_hint: {'center_x': 0.05, 'center_y': 0.97}
            on_release: 
                root.manager.current = 'menu_screen'
                root.manager.transition.direction = 'right'
    MDLabel:
        text: 'Suas campanhas'
        bold: True
        halign: 'center'
        font_size: dp(20)
        pos_hint: {'center_x': 0.5, 'center_y': 0.955}
        theme_text_color: 'Custom'
        text_color: 1, 1, 1 ,1

<MinhasDoacoes>
    name: 'minhas_doacoes'
    MDTopAppBar:
        pos_hint: {'center_x': 0.5, 'center_y': 0.967}
        elevation: 0
        MDIconButton:
            icon: 'arrow-left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            pos_hint: {'center_x': 0.05, 'center_y': 0.97}
            on_release: 
                root.manager.current = 'menu_screen'
                root.manager.transition.direction = 'right'
    MDLabel:
        text: 'Suas doações'
        bold: True
        halign: 'center'
        font_size: dp(20)
        pos_hint: {'center_x': 0.5, 'center_y': 0.955}
        theme_text_color: 'Custom'
        text_color: 1, 1, 1 ,1

<Favoritos>
    name: 'favoritos'
    MDTopAppBar:
        pos_hint: {'center_x': 0.5, 'center_y': 0.967}
        elevation: 0
        MDIconButton:
            icon: 'arrow-left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            pos_hint: {'center_x': 0.05, 'center_y': 0.97}
            on_release: 
                root.manager.current = 'menu_screen'
                root.manager.transition.direction = 'right'
    MDLabel:
        text: 'Favoritos'
        bold: True
        halign: 'center'
        font_size: dp(20)
        pos_hint: {'center_x': 0.5, 'center_y': 0.955}
        theme_text_color: 'Custom'
        text_color: 1, 1, 1 ,1

<Configuracoes>
    name: 'configuracoes'
    MDTopAppBar:
        pos_hint: {'center_x': 0.5, 'center_y': 0.967}
        elevation: 0
        MDIconButton:
            icon: 'arrow-left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            pos_hint: {'center_x': 0.05, 'center_y': 0.97}
            on_release: 
                root.manager.current = 'menu_screen'
                root.manager.transition.direction = 'right'
    MDLabel:
        text: 'Configurações'
        bold: True
        halign: 'center'
        font_size: dp(20)
        pos_hint: {'center_x': 0.5, 'center_y': 0.955}
        theme_text_color: 'Custom'
        text_color: 1, 1, 1 ,1
    MDList:
        pos_hint: {'center_x': 0.5, 'center_y': 0.859}
        OneLineListItem:
            text: 'Tema escuro'
        OneLineListItem:
            text: 'Fale conosco'
    MDSwitch:
        pos_hint: {'center_x': 0.85, 'center_y': 0.88}
