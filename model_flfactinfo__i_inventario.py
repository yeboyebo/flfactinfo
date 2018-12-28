# @class_declaration interna_i_inventario #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactinfo import models as modelos


class interna_i_inventario(modelos.mtd_i_inventario, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactinfo_i_inventario #
class flfactinfo_i_inventario(interna_i_inventario, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration i_inventario #
class i_inventario(flfactinfo_i_inventario, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactinfo.i_inventario_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
