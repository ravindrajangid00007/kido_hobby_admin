from admin_panal import create_app

app = create_app()

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:ravindra@database-1.cnnmnb9m4bjr.ap-south-1.rds.amazonaws.com/KIDO_ADMIN_DATABASE'
    app.run(debug=True ,port=8000)