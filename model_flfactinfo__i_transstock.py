# @class_declaration interna_i_transstock #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactinfo import models as modelos


class interna_i_transstock(modelos.mtd_i_transstock, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactinfo_i_transstock #
class flfactinfo_i_transstock(interna_i_transstock, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration i_transstock #
class i_transstock(flfactinfo_i_transstock, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactinfo.i_transstock_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
