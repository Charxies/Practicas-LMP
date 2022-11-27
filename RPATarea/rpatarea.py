import rpa
rpa.init(visual_automation=True)
rpa.url('https://github.com/login')
rpa.type('//*[@name="login"]','UsuarioRPA')
rpa.click('//*[@name="password"]')
rpa.type('//*[@name="password"]','ContraseNa')
rpa.click('//*[@name="commit"]')

