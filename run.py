import os
try:
 os.mkdir('result')
except:pass
if _name_ == "_main_":
        try:
                _import_("gassken").AORECGANTENG()
        except Exception as e:
                exit(str(e))
