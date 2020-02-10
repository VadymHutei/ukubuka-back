from flask_restful import Resource as Src


class Resource(Src):

    def _getParams(self, *args):
        return {p: self._args[p] for p in args if p in self._args}

    def _hasArg(self, arg):
        return arg in self._args

    def _getArg(self, arg):
        return self._args.get(arg, None)

    def _validArguments(self, validFuncs):
        forDeleting = []
        for key, value in self._args.items():
            if value is None:
                forDeleting.append(key)
                continue
            if key in validFuncs:
                if not validFuncs[key](value):
                    abort(400, message=f'Wrong {key}')
                continue
            else:
                forDeleting.append(key)
        for key in forDeleting:
            del self._args[key]
