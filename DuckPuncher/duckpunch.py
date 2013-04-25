import someclass
import inspect


#Patch a class
class PatchedA():
    def patch_cls(cls, func_name):
        def patch_by_name(new_func):
            old_func = getattr(cls, func_name)

            def patched_func(self):
                return new_func(self, old_func)
            setattr(cls, func_name, patched_func)
        return patch_by_name

    @patch_cls(someclass.A, 'print_val')
    def print_val(self, orig_func):
        return orig_func(self) + ' Fun'


#Patch an unbound function
def patch_mod(module, func_name):
    def patch_by_name(new_func):
        old_func = getattr(module, func_name)
        old_args = inspect.getargspec(old_func)[0]

        def patched_func(varone, vartwo):
            return new_func(old_func, varone, vartwo)
        setattr(module, func_name, patched_func)
    return patch_by_name


def functionBuilder(value_to_print):
    def _function():
        print value_to_print
    return _function


@patch_mod(someclass, 'a_func')
def a_func_patched(orig_func, varone, vartwo):
    b = orig_func(varone, vartwo)
    b.valueOne = "waag "
    return b
