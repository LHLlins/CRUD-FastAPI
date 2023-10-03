from datetime import datetime
from pydantic import BaseModel


class MedicoesSchemas(BaseModel):
  
    gateway_id: str
    gateway_name: str
    number_of_registered_sensors:int
    valid_configurations:bool
    percentual_valid_configurations_perc:float
    expected_measurements:float
    signal_mean_value:float
    signal_status: str
    signal_issue:float
    elapsed_time_since_last_measurement :datetime
    measurement_status: str
    one_hour_groups:int


    class Config:
        orm_model = True
     
       