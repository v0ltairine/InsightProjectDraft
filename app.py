from flask import Flask, render_template, request


app = Flask(__name__)

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
    
    name = pick_role_model(issues, hobbies, location)
    return render_template('role_model.html', name=name)
    

def pick_role_model(issues, hobbies, location):
    if issues == "biology" and hobbies == "embroidery" and location == "pittsburgh":
        return "Kathleen C. Allen"
    elif issues == "biology" and hobbies == "embroidery" and location == "los_angeles":
        return "Samantha Baker"
    elif issues == "biology" and hobbies == "archery" and location == "pittsburgh":
        return "Katrina A. Brown"
    elif issues == "biology" and hobbies == "archery" and location == "los_angeles":
        return "Sally Jensen"
    elif issues == "math" and hobbies == "embroidery" and location == "pittsburgh":
        return "Vanessa Corday"
    elif issues == "math" and hobbies == "archery" and location == "pittsburgh":
        return "Mariah Carnegie"
    elif issues == "math" and hobbies == "embroidery" and location == "los_angeles":
        return "Helen Swanson"
    elif issues == "math" and hobbies == "archery" and location == "los_angeles":
        return "Dorothy M. Smith"
    else: 
        raise Exception