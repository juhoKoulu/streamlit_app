import pandas as pd
df = pd.read_csv(r"C:\Users\juho\Downloads\ad_viz_plotval_data.csv")

from sshtunnel import SSHTunnelForwarder
from sqlalchemy import create_engine

# SSH and MySQL configuration 
ssh_host = "86.50.22.33"
ssh_port = 22
ssh_username = "ubuntu"
ssh_private_key = r"C:\Users\juho\Documents\projektit\OAMK\LinuxAdmin\linux.pem"
mysql_user = "root"  # MySQL user matching the SSH username
mysql_db = "co_concentration"
mysql_port = 3306
mysql_password = "juho"

# Start the SSH tunnel 
tunnel = SSHTunnelForwarder(
	(ssh_host, ssh_port),  # Remote server address and SSH port
	ssh_username='ubuntu',
	ssh_pkey=ssh_private_key,
	remote_bind_address=('127.0.0.1', 3306),
	set_keepalive=10  # Keep the tunnel alive with a 60-second interval
) 
tunnel.start()
print(f"Tunnel established on port: {tunnel.local_bind_port}")

# Connect through the local port forwarded by the SSH tunnel
engine = create_engine(
		f"mysql+pymysql://{mysql_user}:{mysql_password}@127.0.0.1:{tunnel.local_bind_port}/{mysql_db}",
    pool_recycle=10,  # Recycle connections after 10s
    pool_pre_ping=True,  # Check the connection before using it
) 
 
# Move CSV to MySQL
table_name = "co_table"
df.to_sql(table_name, con=engine, if_exists="replace", index=False)

print(f"CSV data loaded into table '{table_name}' successfully.")

# Close tunnel
tunnel.stop()
