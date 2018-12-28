# @class_declaration interna_i_pedidoscli #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactinfo import models as modelos


class interna_i_pedidoscli(modelos.mtd_i_pedidoscli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactinfo_i_pedidoscli #
class flfactinfo_i_pedidoscli(interna_i_pedidoscli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration i_pedidoscli #
class i_pedidoscli(flfactinfo_i_pedidoscli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactinfo.i_pedidoscli_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
