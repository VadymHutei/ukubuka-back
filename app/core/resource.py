from flask_restful import Resource as Src


class Resource(Src):

    def _getParams(self, *args) -> list:
        return {param: self._args[param] for param in args if param in self._args}

    def _argsContains(self, arg) -> bool:
        return arg in self._args

    def _getArg(self, arg):
        return self._args.get(arg, None)
