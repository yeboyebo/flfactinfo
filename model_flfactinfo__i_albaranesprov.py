# @class_declaration interna_i_albaranesprov #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactinfo import models as modelos


class interna_i_albaranesprov(modelos.mtd_i_albaranesprov, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactinfo_i_albaranesprov #
class flfactinfo_i_albaranesprov(interna_i_albaranesprov, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration i_albaranesprov #
class i_albaranesprov(flfactinfo_i_albaranesprov, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactinfo.i_albaranesprov_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
