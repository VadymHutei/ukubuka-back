from flask_restful import Resource as Rsrc, reqparse, abort


class Resource(Rsrc):

    def __init__(self):
        self._parser = reqparse.RequestParser(
            trim=True,
            bundle_errors=False
        )
        self._validation_methods = {}

    def _getParams(self, *args):
        return {p: self._args[p] for p in args if p in self._args}

    def _hasArg(self, arg):
        return arg in self._args

    def _getArg(self, arg):
        return self._args.get(arg, None)

    def _validateArguments(self):
        forDeleting = []
        for key, value in self._args.items():
            if value is None:
                forDeleting.append(key)
                continue
            if key not in self._validation_methods:
                forDeleting.append(key)
                continue
            if not self._validation_methods[key](value):
                abort(400, message=f'Wrong {key}')
        for key in forDeleting:
            del self._args[key]
