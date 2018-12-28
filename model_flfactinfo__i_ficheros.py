# @class_declaration interna_i_ficheros #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactinfo import models as modelos


class interna_i_ficheros(modelos.mtd_i_ficheros, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactinfo_i_ficheros #
class flfactinfo_i_ficheros(interna_i_ficheros, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration i_ficheros #
class i_ficheros(flfactinfo_i_ficheros, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactinfo.i_ficheros_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
