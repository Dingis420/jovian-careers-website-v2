from sqlalchemy import create_engine, text

# create variable to store the path to the database
db_connection_string = "mysql+pymysql://z1hsj6pqe13r94eghox9:pscale_pw_MvDxmQ7UneccuqCTKl3dVVXOTsiKKu6bUlJWVSNe8H@aws.connect.psdb.cloud/joviancareers?charset=utf8mb4"
# use engine object to connect to a pre-existing database
engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  }
)
    
  