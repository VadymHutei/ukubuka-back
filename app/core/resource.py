from flask_restful import Resource as Rsrc, reqparse, abort


class Resource(Rsrc):

    def __init__(self):
        self._parser = reqparse.RequestParser(
            trim=True,
            bundle_errors=False
        )
        self._args = {}
        self._transform_methods = {}
        self._validation_methods = {}

    def _getArguments(self, *args):
        if not args:
            return self._args
        return {p: self._args[p] for p in args if p in self._args}

    def _hasArg(self, arg):
        return arg in self._args

    def _getArg(self, arg):
        return self._args.get(arg, None)

    def _parseArguments(self):
        self._args = self._parser.parse_args()

    def _transformArguments(self):
        for arg, method in self._transform_methods.items():
            if arg in self._args:
                if type(self._args[arg]) is list:
                    self._args[arg] = tuple(map(
                        lambda x: method(x),
                        self._args[arg]
                    ))
                elif type(self._args[arg]) is str:
                    self._args[arg] = method(self._args[arg])

    def _validateArgument(self, key, value):
        def validate(value, method):
            if value is None:
                return
            if not method(value):
                abort(400, message=f'Wrong {key}')
        if type(value) is tuple:
            for v in value:
                if type(v) is tuple:
                    for i, x in enumerate(v):
                        validate(x, self._validation_methods[key][i])
                    return
                validate(v, self._validation_methods[key])
            return
        validate(value, self._validation_methods[key])

    def _validateArguments(self):
        forDeleting = []
        for key, value in self._args.items():
            if key not in self._validation_methods:
                forDeleting.append(key)
                continue
            self._validateArgument(key, value)
        for key in forDeleting:
            del self._args[key]
