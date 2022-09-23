from operation_class import *

sequencial = 1 #input("")
contract_tp = 1 #input("")
dt_contract = 1 #input("")	
moeda = 1 #input("")
val_princ = 1 #input("")
financier_bank = 1 #input("")
start_dt = 1 #input("")
end_dt = 1 #input("")
company = 1 #input("")
bill_tp = 1 #input("")
inter_terc = 1 #input("")
counterparty = 1 #input("")
    
divida = debt(sequencial,contract_tp,dt_contract,moeda,val_princ,financier_bank,start_dt,end_dt,company,bill_tp,inter_terc,counterparty)

print(divida.user)
print(divida.register)