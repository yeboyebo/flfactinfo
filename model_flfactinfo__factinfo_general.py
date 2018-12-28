# @class_declaration interna_factinfo_general #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactinfo import models as modelos


class interna_factinfo_general(modelos.mtd_factinfo_general, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactinfo_factinfo_general #
class flfactinfo_factinfo_general(interna_factinfo_general, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration factinfo_general #
class factinfo_general(flfactinfo_factinfo_general, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactinfo.factinfo_general_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
