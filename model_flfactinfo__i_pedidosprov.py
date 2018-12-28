# @class_declaration interna_i_pedidosprov #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactinfo import models as modelos


class interna_i_pedidosprov(modelos.mtd_i_pedidosprov, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactinfo_i_pedidosprov #
class flfactinfo_i_pedidosprov(interna_i_pedidosprov, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration i_pedidosprov #
class i_pedidosprov(flfactinfo_i_pedidosprov, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactinfo.i_pedidosprov_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
