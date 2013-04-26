import someclass
import inspect


#Patch a class
class PatchedA():
    def patch_cls(cls, func_name):
        def patch_by_name(new_func):
            orig_func = getattr(cls, func_name)
            def patched_func(self):
                return new_func(self, orig_func)
            setattr(cls, func_name, patched_func)
        return patch_by_name

    @patch_cls(someclass.A, 'print_val')
    def print_val(self, orig_func):
        return orig_func(self) + ' Fun'


#Patch an unbound function
def patch_mod(module, func_name):
    def patch_by_name(new_func):
        orig_func = getattr(module, func_name)
        def patched_func(*args, **kwargs):
            varPassThru = inspect.getcallargs(orig_func, *args, **kwargs)
            return new_func(orig_func, varPassThru)
        setattr(module, func_name, patched_func)
    return patch_by_name

@patch_mod(someclass, 'a_func')
def a_func(orig_func, varPass):
    b = orig_func(**varPass)
    b.valueOne = "waag "
    return b
