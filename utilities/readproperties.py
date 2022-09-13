import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class Readconfig:
    @staticmethod
    def getapplicationURL():
        url = config.get('common info','base_url')
        return url
    
    @staticmethod
    def getUsername():
        user_name = config.get('common info','user_name')
        return user_name

    @staticmethod
    def getpassword():
        password = config.get('common info','password')
        return password