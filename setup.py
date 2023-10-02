import setuptools

with open('description.md', 'r', enconding='utf-8') as fh:
  long_descritpion=fh.read()


setuptools.setup(
  name='Mi_paquete',
  version='0.1.0',
  author='Sonia',
  #author_email='sonia@gmail.com',
  description='mi primer paquete de funciones',
  long_description= long_description, #variable creada en las lineas superiores. long description lee al archivo description.md
  long_description_content_type='text/markdown',
  #url=repositorio del paquete,
  #project_url={'bug tracker':url}, url adicionales, ejemplo un bug tracker. 
  license='MIT',
  packages=['Mi_paquete'] #nombre del paquete que debe coincidir con el nombre del directorio
  install_requiers=['requests'] #liberia adicional que instala con mi paquete.


)