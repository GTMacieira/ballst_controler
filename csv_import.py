import csv, sqlite3

con = sqlite3.connect("ball_control.db") # change to 'sqlite:///your_filename.db'
cur = con.cursor()
# cur.execute("""CREATE TABLE ballests (
# 	id INTEGER NOT NULL,
# 	sequencial VARCHAR(20) NOT NULL,
# 	novo_sequencial VARCHAR(20) NULL,
# 	cliente VARCHAR(100) NOT NULL,
# 	dt_embarque DATE NOT NULL,
# 	dt_recebimento DATE NOT NULL,
# 	fatura VARCHAR(100) NOT NULL,
# 	moeda VARCHAR(5) NOT NULL,
# 	val_fatura FLOAT NOT NULL,
# 	utilizacao_fatura FLOAT NOT NULL,
# 	val_utilizado_fatura FLOAT NOT NULL,
# 	val_util_convert_brl FLOAT NOT NULL,
# 	val_util_convert_eur FLOAT NOT NULL,
# 	val_util_convert_usd FLOAT NOT NULL,
# 	tp_contrato VARCHAR(10) NOT NULL,
# 	sd_due VARCHAR(500) NOT NULL,
# 	ch_acesso_re VARCHAR(500) NULL,
# 	obs VARCHAR(500) NULL,
# 	total_parcial VARCHAR(10) NOT NULL,
# 	user VARCHAR(20) NOT NULL,
# 	register DATETIME NOT NULL,
# 	PRIMARY KEY ("id")
# )
# ;""")


with open('C:/Users/CSO5007/Desktop/python_projects/ballst_controler/recursos/DB_Lastros_CSV.csv','r') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['sequencial'], i['novo_sequencial'],i['cliente'], i['dt_embarque'],i['dt_recebimento'], i['fatura'], i['moeda'], i[' valfatura '],i['utilizacao_fatura'], i[' val_utilizado_fatura '], i[' val_util_convert_brl '], i[' val_util_convert_eur '], i[' val_util_convert_usd '], i['tp_contrato'], i['sd_due'], i['ch_acesso_re'], i['obs'], i['total_parcial'],  i['user'], i['register']) for i in dr]
    cur.executemany("INSERT INTO ballests (sequencial, novo_sequencial, cliente, dt_embarque, dt_recebimento, fatura, moeda, val_fatura, utilizacao_fatura, val_utilizado_fatura, val_util_convert_brl, val_util_convert_eur, val_util_convert_usd, tp_contrato, sd_due, ch_acesso_re, obs, total_parcial, user, register) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
    con.commit()
    con.close()

