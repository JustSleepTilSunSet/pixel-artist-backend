from flask import Flask, jsonify,request
from model.Constants import status
import os
from model.Secret import Secret;
from sqlalchemy.orm import sessionmaker
from model.database.repository.UsersRepository import User
from model.database.initdb import connectInitDatabase,createSession;
from flask_jwt_extended import create_access_token, decode_token
from datetime import timedelta
import json
def login():
        
    try:
        # Check the header exist token.
        isRegistered = True;
        userInfo = None;
        connectInitDatabase();
        session = createSession();

        if request.headers.get('Authorization') is not None:
            token_type, access_token = request.headers.get('Authorization').split(' ');
            if token_type == os.getenv("TOKEN_FORMAT"):
                try:
                    userInfo = decode_token(access_token)["sub"];
                    # parse user info.
                    # NOTICE: Decode and get the user account info.
                    print(userInfo);
                    isRegistered = False;
                except Exception as e:
                    print(str(e));

        if isRegistered:
            resp = request.json;
            # Inserted user setting.
            session.add(User(account = resp["account"],password = resp["pwd"]));
            session.commit();

            # Generate token.
            expires = timedelta(minutes=int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES_MINUTES")))
            access_token = create_access_token(identity=json.dumps(resp), expires_delta=expires);
            userInfo = decode_token(access_token)["sub"];

        return jsonify({'status': status["SUCCESS"], 'message': 'login success',"access_token": access_token})
    except Exception as e:
        print(str(e))
        return jsonify({'status': status["FAIL"], 'message': 'login failed.'})

def loginByGuest(): 
    try:
        connectInitDatabase();
        session = createSession()

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
