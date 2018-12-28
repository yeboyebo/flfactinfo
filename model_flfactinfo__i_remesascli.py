# @class_declaration interna_i_remesascli #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactinfo import models as modelos


class interna_i_remesascli(modelos.mtd_i_remesascli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactinfo_i_remesascli #
class flfactinfo_i_remesascli(interna_i_remesascli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration i_remesascli #
class i_remesascli(flfactinfo_i_remesascli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactinfo.i_remesascli_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
