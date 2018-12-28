# @class_declaration interna_i_facturascli #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactinfo import models as modelos


class interna_i_facturascli(modelos.mtd_i_facturascli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactinfo_i_facturascli #
class flfactinfo_i_facturascli(interna_i_facturascli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration i_facturascli #
class i_facturascli(flfactinfo_i_facturascli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactinfo.i_facturascli_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
