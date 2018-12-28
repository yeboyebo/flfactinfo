# @class_declaration interna_i_albaranescli #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactinfo import models as modelos


class interna_i_albaranescli(modelos.mtd_i_albaranescli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactinfo_i_albaranescli #
class flfactinfo_i_albaranescli(interna_i_albaranescli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration i_albaranescli #
class i_albaranescli(flfactinfo_i_albaranescli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactinfo.i_albaranescli_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
