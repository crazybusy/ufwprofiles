import os, sys
import configparser
from simple_parameters import simple_parameters


def main():
    directory = "/etc/ufw/applications.d/"
    params = simple_parameters.SimpleParser('ufwprofiles.json')
    options, args = params.resolve_parameters(sys.argv)

    if options.appname is None and options.title is None:
        print("No title specified for the app")
        return 
    
    if options.appname is not None:
        configfile_name = options.appname
    else:
        configfile_name = options.title
           
    if os.path.isfile(configfile_name):
        print("File {} already exist. Choose a different name."
              .format(configfile_name))    
    elif options.ports is None:
        print("No ports specified for the app")    
    else:
        # Create the configuration file as it doesn't exist yet
        cfgfile = open(
            os.path.join(directory, configfile_name), 'w')

        # Add content to the file
        Config = configparser.ConfigParser()
        Config.add_section(configfile_name)
        if options.title is not None:        
            Config.set(configfile_name, 'title', options.title)
        else:
            Config.set(configfile_name, 'title', options.appname)
        Config.set(configfile_name, 'description', options.description)
        Config.set(configfile_name, 'ports', options.ports)

        Config.write(cfgfile)
        cfgfile.close()

if __name__ == '__main__':
	main()
