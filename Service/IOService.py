class IOService:
    @staticmethod
    def get_data_from_file(file_path):
        file = open(file_path)
        data=file.read()
        file.close()
        return data.split('\n')

    def save_lst_to_file(self,file_path,lst):
        f=open(file_path,'a')
        for item in lst:
            f.write(str(item))
        f.close()

