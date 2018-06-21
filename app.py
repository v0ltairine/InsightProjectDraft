from flask import Flask, render_template, request
import psycopg2
import random

app = Flask(__name__)

conn = psycopg2.connect(host = "localhost", dbname = "rolemodel", user = "marieskoczylas", port=5432)
cur = conn.cursor()

@app.route('/')
def hello_world():
	return render_template('FRMcode.html')

@app.route('/role_model', methods=['POST'])
def createrolemodel():
    location = request.values["location"]
    hobbies = request.values["hobbies"]
    issues = request.values["issues"]
    # call my nlp function with these variables (locations, hobbies, issues)
    # write a function where i pass in the answers to 3 questions and it returns the name of the role model.
    
    profiles = pick_role_model(issues, hobbies, location)
    return render_template('role_model.html', profiles=profiles)
    
def searchdb(issues, hobbies, location):
    # query the db for matches
    cur.execute("SELECT profile_id FROM profiles WHERE topics ILIKE %s AND topics ILIKE %s AND topics ILIKE %s",
        ('%'+issues+'%', '%'+hobbies+'%', '%'+location+'%'))
        #(issues, hobbies, location))
    return cur.fetchall()

def random_chooser3(profile_possibilities):
    # choose up to 3 (or list length) random profiles from list
    if len(profile_possibilities) <= 3:
        return profile_possibilities
    return random.sample(profile_possibilities, 3)

def extract_fullname_hyperlink(chosen_profile_ids):
    output = []
    for id in chosen_profile_ids:
        cur.execute("SELECT fullname, hyperlink FROM profiles WHERE profile_id = %s", (id,))
        found = cur.fetchall()
        if len(found) > 0:
            output.append({'name': found[0][0], 'link': found[0][1]})
    return output 

def pick_role_model(issues, hobbies, location):
    profile_possibilities = searchdb(issues, hobbies, location)
    chosen_profile_ids = random_chooser3(profile_possibilities)
    final_profiles = extract_fullname_hyperlink(chosen_profile_ids)
    return final_profiles #This is gonna be a dictionary for name and link.  