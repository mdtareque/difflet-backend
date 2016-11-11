from subprocess import call

def get_call_array(command='ls',**kwargs):
    callarray = [command]
    for k, v in kwargs.items():
        #callarray.append("--" + k)
        if v:
            callarray.append(str(v))
    print callarray
    return callarray

call(get_call_array("python", name="flickr.py parrot"))

