from flask import Flask, jsonify,request
from model.Constants import status
import os
from model.Secret import Secret;
from sqlalchemy.orm import sessionmaker
from model.database.repository.UsersRepository import User
from model.database.initdb import connectInitDatabase;

def login():
    resp = request.json
    try:
        print(jsonify(resp))
        engine = connectInitDatabase();
        Session = sessionmaker(bind=engine)
        session = Session()
        isVaild = session.query(User).filter_by(account = resp["account"]).first();

        if isVaild:
            print("User exists.")
        else:
            print("User does not exist.")
            return jsonify({'status': status["FAIL"], 'message': 'login failed.'})

        print(isVaild);
        return jsonify({'status': status["SUCCESS"], 'message': 'login success'})
    except Exception as e:
        print(str(e))
        return jsonify({'status': status["FAIL"], 'message': 'login failed.'})

def loginByGuest():
    try:
        engine = connectInitDatabase();
        Session = sessionmaker(bind=engine)
        session = Session()

        secret = Secret()
        account= secret.generateRandString(16);
        password= secret.generateRandString(8);
        new_user = User(account=account, password= password)
        session.add(new_user)
        session.commit()

        return jsonify({'status': status["SUCCESS"], 'message': {
            "account":account,
            "password":password
        }})
    except Exception as e:
        print(str(e))
        return jsonify({'message':"Server error"});
