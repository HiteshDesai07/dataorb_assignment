from jproperties import Properties

class Property:

    api_key = ''
    load_review_from_file = False

    def load_properties(self):
        configs = Properties()
        with open('data/application.properties', 'rb') as config_file:
            configs.load(config_file)

        prop_view = configs.items()
        for item in prop_view:
            if(item[0]=='api_key'):
                self.api_key = item[1].data
            if(item[0]=='load_review_from_file'):
                if(item[1].data=='true'):
                    self.load_review_from_file = True

test = Property()
test.load_properties()
print(test.api_key)