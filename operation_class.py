from msilib.schema import Class
import getpass
from datetime import date, datetime

class debt:
    def __init__(self,sequencial,contract_tp,dt_contract,moeda,val_princ,financier_bank,start_dt,end_dt,company,bill_tp,inter_terc,counterparty):
        self.sequencial=sequencial
        self.contract_tp = contract_tp	
        self.dt_contract = dt_contract	
        self.moeda = moeda	 
        self.val_princ = val_princ	
        self.financier_bank = financier_bank	
        self.start_dt = start_dt	
        self.end_dt = end_dt
        self.company = company	
        self.bill_tp = bill_tp	
        self.inter_terc = inter_terc
        self.counterparty = counterparty	
        self.user = getpass.getuser()
        self.register = datetime.now().strftime('%m-%d-%Y %H:%M')
        
    