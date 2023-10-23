def validar_archivo (request, campo):
    #   por defecto el (request.data) no se puede modificar pero esta es una forma de modificarla no muy elegante
    request._mutable = True
    #   aca se le asigna Nona el primer data si el tipo de dato que le llega es un str y sino lo deja como esta
    request[campo] = None if type (request[campo]) == str else request [campo]
    #   despues se tiene que volber a bloquearla
    request._mutable = False

    return request