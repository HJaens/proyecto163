import qrcode
from apps.paciente.models import Perfilpaciente
#  Creamos un objeto codigo QR
qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size = 10,
    border = 4
)
# Podemos crear la informacion que queremos
# en el codigo de manera separada
paciente=Perfilpaciente.objets.filter(ci)

info = 'paciente'
# Agregamos la informacion
qr.add_data(info)
qr.make(fit=True)
# Creamos una imagen para el objeto código QR
imagen = qr.make_image()
# Guardemos la imagen con la extension que queramos
imagen.save('codigo2.png')