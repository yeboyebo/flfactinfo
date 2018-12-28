# @class_declaration interna_i_facturasprov #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactinfo import models as modelos


class interna_i_facturasprov(modelos.mtd_i_facturasprov, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactinfo_i_facturasprov #
class flfactinfo_i_facturasprov(interna_i_facturasprov, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration i_facturasprov #
class i_facturasprov(flfactinfo_i_facturasprov, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactinfo.i_facturasprov_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
