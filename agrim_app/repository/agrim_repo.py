from .main_repo import AppCRUD , AppRepo
from ..schemas import AgrimCreate, AgrimItem
from ..models import AgrimInfo

class AgrimRepo(AppCRUD):
    def create_item(self,info: AgrimCreate) -> AgrimInfo:
        agrim_info = AgrimInfo(name = info.name, address = info.address, balance = info.balance)
        self.db.add(agrim_info)
        self.db.commit()
        self.db.refresh(agrim_info)
        return agrim_info
    
    def get_item(self, info_id: int) ->AgrimInfo:
        agrim_info = self.db.query(AgrimInfo).filter(AgrimInfo.id == info_id).first()
        return agrim_info if agrim_info else None

