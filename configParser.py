from configparser import DEFAULTSECT, RawConfigParser

class UnicodeConfigParser(RawConfigParser):
 
    def __init__(self, *args, **kwargs):
        RawConfigParser.__init__(self, *args, **kwargs)
 
    def write(self, fp):
        if self._defaults:
            fp.write("[%s]\n" % DEFAULTSECT)
            for (key, value) in self._defaults.items():
                fp.write("%s = %s\n" % (key, str(value).replace('\n', '\n\t')))
            fp.write("\n")
        for section in self._sections:
            fp.write("[%s]\n" % section)
            for (key, value) in self._sections[section].items():
                if key != "__name__":
                    fp.write("%s = %s\n" %
                             (key, str(value).replace('\n','\n\t')))
            fp.write("\n")
 
    # This function is needed to override default lower-case conversion
    # of the parameter's names. They will be saved 'as is'.
    def optionxform(self, strOut):
        return strOut