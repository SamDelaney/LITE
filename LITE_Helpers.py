import ntpath

class TextHelper:
    @staticmethod
    def pruneFileName(path):
        # basename removes directories from path
        filename = ntpath.basename(path).split('.') 
        return filename[0]# return the filename without the filetype
        
        
