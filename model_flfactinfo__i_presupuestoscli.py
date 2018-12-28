# @class_declaration interna_i_presupuestoscli #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactinfo import models as modelos


class interna_i_presupuestoscli(modelos.mtd_i_presupuestoscli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactinfo_i_presupuestoscli #
class flfactinfo_i_presupuestoscli(interna_i_presupuestoscli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration i_presupuestoscli #
class i_presupuestoscli(flfactinfo_i_presupuestoscli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactinfo.i_presupuestoscli_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
