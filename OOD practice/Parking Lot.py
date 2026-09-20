
# OOD: Parking Slot 
# Clarify: 分配策略 first-fit 从level0开始顺序扫描；计费 按小时向上取整 Car 5/h Motor 3/h Truck 10/h

from dataclasses import dataclass
from enum import Enum
from typing import List, Dict, Optional
import math

# 两个枚举class 有车辆类型+停车slot类型
class VehicleType(Enum):
    MOTORCYCLE = 1 # int只是一个占位符 也可以写MOTORCYCLE = auto()
    CAR = 2
    TRUCK = 3

class SpotType(Enum):
    MOTOR = 1
    COMPACT = 2
    LARGE = 3

# 数据class 车、停车位
@dataclass(frozen=True)
class Vehicle:
    plate:str
    vtype: VehicleType

@dataclass # dataclass会自动生成init和对象比较以及debug等
class Spot:
    spot_id:str
    stype:SpotType
    occupied_by: Optional[str] = None # store plate

    # 这个spot是否可以停这辆车？
    def can_fit(self, vehicle: Vehicle) -> bool:

        # 摩托车可以停任何地点
        if vehicle.vtype == VehicleType.MOTORCYCLE:
            return True

        if vehicle.vtype == VehicleType.CAR:
            return self.stype in {SpotType.COMPACT, SpotType.LARGE}
        
        if vehicle.vtype == VehicleType.TRUCK:
            return self.stype == SpotType.LARGE
        
        return False
    
    # 可以用这个is_free检查占用
    def is_free(self) -> bool:
        return self.occupied_by is None
    
    def park(self, vehicle:Vehicle) -> None:
        if not self.is_free():
            raise Exception("Spot already occupied")
        self.occupied_by = vehicle.plate
    
    def leave(self) -> None:
        self.occupied_by = None
        
# 这是行为很多的对象 不用dataclass 这更像是一个service/maganer对象
# 它的重点是行为不是数据
class Level:

    def __init__(self, level_id:str, spots: List[Spot]):
        self.level_id = level_id
        self.spots = spots
        
    def find_spot(self, vehicle:Vehicle) -> Optional[Spot]:

        # 暂时一个一个找spot
        for spot in self.spots:
            if spot.is_free() and spot.can_fit(vehicle):
                return spot
            
        return None
    
    # 用于检查停车场状态的API 每种车位有几个空
    def free_count(self) -> Dict[SpotType, int]: 

        counts = {
            SpotType.MOTORCYCLE: 0,
            SpotType.COMPACT: 0,
            SpotType.LARGE: 0
        }

        for spot in self.spots:
            if spot.is_free():
                counts[spot.stype] += 1

        return counts

@dataclass
class Ticket:

    ticket_id: str
    plate: str
    vtype: VehicleType
    level_id: str
    spot_id: str
    start_ts: float


class ParkingLot:
    # Simple hourly pricing
    RATES = {
        VehicleType.MOTORCYCLE: 3,
        VehicleType.CAR: 5,
        VehicleType.TRUCK: 10,
    }
    def __init__(self, levels: List[Level]):
        self.levels = levels
        self.tickets_count = 0
        self.tickets: Dict[int, Ticket] = {} # 通过ticket_id找ticket
        self.level_dict = {level.level_id: level for level in levels}
    
    # 入场：找车位 -> 占用 -> 生成票; 如果同时入场，在这加一个lock
    def park(self, vehicle: Vehicle, start_ts: float) -> Optional[Ticket]: 

        spot = None
        level_id = None
        
        for level in self.levels:
            spot = level.find_spot(vehicle)
            # 从第一层往上找 先找到就占用
            if spot:
                level_id = level.level_id
                break
        
        if not spot:
            return None

        spot.park(vehicle)
        self.tickets_count += 1
        ticket_id = self.tickets_count

        # 生成ticket
        ticket = Ticket(
            ticket_id=ticket_id,
            plate=vehicle.plate,
            vtype=vehicle.vtype,
            level_id=level_id,
            spot_id=spot.spot_id,
            start_ts=start_ts
        )

        self.tickets[ticket.ticket_id] = ticket
        return ticket
        
    # 出场：用 ticket 找到 spot -> 释放 -> 计费
    def leave(self, ticket_id: str, leave_ts: float) -> int: 

        ticket = self.tickets[ticket_id]

        # 释放停车空间
        # 找到对应 level 
        level = self.level_dict[ticket.level_id]

        # 找到对应 spot 这也可以在spot里优化成一个字典
        spot = None
        for s in level.spots:
            if s.spot_id == ticket.spot_id:
                spot = s
                break

        spot.leave()

        # 计费
        start_ts = ticket.start_ts
        hours = math.ceil((leave_ts - start_ts) / 3600)

        rate = self.RATES[ticket.vtype]
        fee = hours * rate

        # 删除ticket 不删也行
        del self.tickets[ticket_id]

        return fee

