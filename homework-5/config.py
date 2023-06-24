from configparser import ConfigParser


def config(filename="database.ini", section="postgresql"):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
    if not parser.has_section(section):
        raise Exception(
            'Section {0} is not found in the {1} file.'.format(section, filename))
    params = parser.items(section)
    return {param[0]: param[1] for param in params}
