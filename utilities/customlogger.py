import logging

class Logger:
    @staticmethod
    def loggen(): 
        logger = logging.getLogger()   
        fhandler = logging.FileHandler(filename=".//Logs//automation.log")
        formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(message)s", datefmt="%m:%d:%y %I:%M:%S:%p")
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)
        return logger
    
    

