# @class_declaration interna_i_reciboscli #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactinfo import models as modelos


class interna_i_reciboscli(modelos.mtd_i_reciboscli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactinfo_i_reciboscli #
class flfactinfo_i_reciboscli(interna_i_reciboscli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration i_reciboscli #
class i_reciboscli(flfactinfo_i_reciboscli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactinfo.i_reciboscli_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
