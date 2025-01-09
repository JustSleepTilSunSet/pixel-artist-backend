from flask import Flask, jsonify,request
from model.Constants import status
import os
from model.Secret import Secret;
from sqlalchemy import select
from model.database.repository.UsersRepository import User
from model.database.initdb import dbSession;
from flask_jwt_extended import create_access_token, decode_token
from datetime import timedelta
import json
def login():

    try:
        # Check the header exist token.
        session = dbSession;
        resp = request.json;
        stmt = select(User).where(User.account == resp["account"])
        result = session.execute(stmt)
        userInfo = result.scalars().first();
        if userInfo is None:
            try:
                session.add(User(account = resp["account"],password = resp["pwd"]));
                session.commit();
                userInfo = resp;
            except Exception as e:
                session.rollback();
        else:
            if resp["pwd"] != userInfo.password:
                return jsonify({'status': status["FAIL"], 'message': 'login failed',"access_token": None});

        # Generate token.
        expires = timedelta(minutes=int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES_MINUTES")))
        access_token = create_access_token(identity=json.dumps(resp), expires_delta=expires);
        # userInfo = decode_token(access_token)["sub"];
        return jsonify({'status': status["SUCCESS"], 'message': 'login success',"access_token": access_token})
    except Exception as e:
        print(str(e))
        return jsonify({'status': status["FAIL"], 'message': 'login failed.'})

def loginByGuest(): 
    try:
        session = dbSession

        secret = Secret()
        account= secret.generateRandString(16);
        password= secret.generateRandString(8);
        new_user = User(account=account, password= password)
        session.add(new_user)
        session.commit()
     
        accountInfo = {};
        accountInfo["account"] = account;
        accountInfo["password"] = password;
        # Generate token.
        expires = timedelta(minutes=int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES_MINUTES")))
        access_token = create_access_token(identity=json.dumps(accountInfo), expires_delta=expires);
        print("access_token:",access_token);
        return jsonify({'status': status["SUCCESS"], 'message': {
            "access_token": access_token
        }})
    except Exception as e:
        print(str(e))
        return jsonify({'message':"Server error"});
