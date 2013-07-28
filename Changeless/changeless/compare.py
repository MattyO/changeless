from changeless.methods import to_dict, _r_sub_dict

'''returns true if the union of dicts are the same minus the key in the ignore list'''
def fuzzyEquals(obj, other_obj, ignore=[]):
    obj = to_dict(obj)
    other_obj =to_dict(other_obj)

    refined_obj = _r_sub_dict(other_obj, obj)
    refined_other = _r_sub_dict(obj, other_obj )

    if refined_obj != refined_other:
        pass

    return refined_obj == refined_other 
