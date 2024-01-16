import sys
from cx_Freeze import setup, Executable
 
arquivos = ['token_email.txt'] 

base = "Win32GUI" if sys.platform == "win32" else None
 

configuracao = Executable(
    script='app.py',
    icon='icone.ico', 
    base=base 
)

setup(
    name = 'Varredor de Dados que envia planilha por e-mail.', 
    version = '1.0', 
    description = 'Com esse programa, você pode varrer os dados do site especificado,'\
      ' e enviar uma planilha com eles para o e-mail que o usuário informar.',
    author = 'Jonatas L. de Sousa',            
    options = {'build_exe': {'include_files': arquivos,"include_msvcr":True}}, 
    executables = [configuracao]
)