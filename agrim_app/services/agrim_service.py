from ..schemas import AgrimItem, AgrimCreate
from ..repository import AgrimRepo

agrim_repo = AgrimRepo()
class AgrimService:
    def get_info(self, info_id:int):
        print("hello")
        data = agrim_repo.get_item(info_id)

        return data
    
    def creat_info(self,info:AgrimCreate):
        data = agrim_repo.create_item(info)
        return data

